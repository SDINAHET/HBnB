let places = [];

document.addEventListener("DOMContentLoaded", async () => {
  try {
    const response = await fetch("/api/v1/places");
    if (!response.ok) {
      throw new Error("Failed to fetch places");
    }

    places = await response.json();
    renderPlaceList(places);
    setupPriceFilter(places);
  } catch (error) {
    console.error("Error fetching places:", error);
  }
});

function renderPlaceList(places) {
  const placeListEl = document.querySelector(".place-list");
  placeListEl.innerHTML = "";

  places.forEach((place) => {
    const card = document.createElement("div");
    card.className = "place-card";
    card.innerHTML = `
      <h2>${place.name}</h2>
      <p>${place.description}</p>
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

function setupPriceFilter(places) {
  const maxPriceFilter = document.getElementById("max-price");
  if (maxPriceFilter) {
    maxPriceFilter.addEventListener("change", (e) => {
      const maxPrice = e.target.value === "all" ? Infinity : parseInt(e.target.value, 10);
      const filteredPlaces = places.filter((place) => place.price <= maxPrice);
      renderPlaceList(filteredPlaces);
    });
  }
}



  function renderPlaceDetails(places, placeId) {
    const place = places.find((p) => p.id === placeId);
    if (!place) {
      document.body.innerHTML = "<h1>Place not found</h1>";
      return;
    }

    document.getElementById("place-title").textContent = place.name;
    document.getElementById("place-host").textContent = place.host;
    document.getElementById("place-price").textContent = `${place.price}€`; // Ajout du symbole €
    document.getElementById("place-description").textContent = place.description;
    document.getElementById("place-amenities").textContent = place.amenities;

    const reviewsSection = document.getElementById("reviews-section");
    reviewsSection.innerHTML = place.reviews.map(
      (review) => `
        <div class="review">
          <p><strong>${review.author}:</strong></p>
          <p>${review.comment}</p>
          <p>Rating: ${"★".repeat(review.rating)}${"☆".repeat(5 - review.rating)}</p>
        </div>
      `
    ).join("");
  }

  function setupLoginForm() {
    const loginForm = document.getElementById("login-form");
    if (!loginForm) return;

    loginForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const email = document.getElementById("email").value.trim();
      const password = document.getElementById("password").value.trim();

      const users = { "admin@hbnb.com": "admin1234" };
      if (users[email] === password) {
        localStorage.setItem("isLoggedIn", "true");
        localStorage.setItem("userEmail", email);
        alert("Login successful!");

        const redirectUrl = new URLSearchParams(window.location.search).get("redirect");
        window.location.href = redirectUrl ? decodeURIComponent(redirectUrl) : "index.html";
      } else {
        alert("Invalid email or password. Please try again.");
      }
    });
  }

  function setupLogoutButton() {
    const logoutButton = document.getElementById("logout-button");
    if (!logoutButton) return;

    logoutButton.addEventListener("click", () => {
      localStorage.removeItem("isLoggedIn");
      localStorage.removeItem("userEmail");
      alert("You have been logged out!");
      window.location.href = "login.html";
    });
  }
