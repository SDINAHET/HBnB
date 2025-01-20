document.addEventListener("DOMContentLoaded", async () => {
  try {
    checkAuthentication();
    const places = await fetchPlaces();
    renderPlaceList(places);
    setupPriceFilter(places);
  } catch (error) {
    console.error("Error initializing the page:", error);
    document.querySelector(".place-list").innerHTML =
      "<p>Failed to load places. Please try again later.</p>";
  }
});

/**
 * Check user authentication and control the visibility of the login link.
 */
function checkAuthentication() {
  const token = getCookie("token");
  const loginLink = document.getElementById("login-link");
  const logoutButton = document.getElementById("logout-button");

  if (!token) {
    loginLink.style.display = "block";
    logoutButton.style.display = "none";
  } else {
    loginLink.style.display = "none";
    logoutButton.style.display = "block";
    logoutButton.addEventListener("click", () => {
      document.cookie = "token=; Max-Age=0; path=/";
      alert("You have been logged out.");
      window.location.href = "login.html";
    });
  }
}

/**
 * Get the value of a cookie by its name.
 * @param {string} name - Name of the cookie.
 * @returns {string|null} Value of the cookie or null if not found.
 */
function getCookie(name) {
  const cookies = document.cookie.split("; ");
  for (let cookie of cookies) {
    const [key, value] = cookie.split("=");
    if (key === name) return value;
  }
  return null;
}

/**
 * Fetch places from the API.
 * Publicly accessible without requiring a token.
 * @returns {Array} List of places.
 */
async function fetchPlaces() {
  const response = await fetch("http://127.0.0.1:5000/api/v1/places/", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });
  if (!response.ok) {
    throw new Error("Failed to fetch places");
  }
  const data = await response.json();
  return data.places || []; // Adjust based on expected response structure
}

/**
 * Render the list of places dynamically.
 * @param {Array} places - List of places to render.
 */
function renderPlaceList(places) {
  const placeListEl = document.querySelector(".place-list");
  placeListEl.innerHTML = "";
  if (!places.length) {
    placeListEl.innerHTML = "<p>No places available.</p>";
    return;
  }
  places.forEach((place) => {
    const card = document.createElement("div");
    card.className = "place-card";
    card.innerHTML = `
      <h2>${place.title}</h2>
      <p>Price: ${place.price}€</p>
      <button class="view-details" data-id="${place.id}">View Details</button>
    `;
    placeListEl.appendChild(card);
  });

  document.querySelectorAll(".view-details").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      const placeId = e.target.getAttribute("data-id");
      window.location.href = `place.html?id=${placeId}`;
    });
  });
}

/**
 * Set up the max price filter.
 * @param {Array} places - Original list of places.
 */
function setupPriceFilter(places) {
  const maxPriceFilter = document.getElementById("max-price");
  maxPriceFilter.addEventListener("change", (e) => {
    const maxPrice =
      e.target.value === "all" ? Infinity : parseInt(e.target.value, 10);
    const filteredPlaces = places.filter(
      (place) => place.price <= maxPrice
    );
    renderPlaceList(filteredPlaces);
  });
}
