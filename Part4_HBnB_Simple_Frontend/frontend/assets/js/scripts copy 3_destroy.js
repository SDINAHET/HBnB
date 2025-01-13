// document.addEventListener("DOMContentLoaded", () => {
//   // Données statiques
//   const places = [
//     {
//       id: "765a38e6-c131-4315-8e9c-28ac88424634",
//       name: "Beautiful Beach House",
//       host: "John Doe",
//       price: 150,
//       description: "A beautiful beach house with amazing views...",
//       amenities: "WiFi, Pool, Air Conditioning",
//       reviews: [
//         { author: "Jane Smith", comment: "Great place to stay!", rating: 4 },
//         { author: "Robert Brown", comment: "Amazing location and very comfortable.", rating: 5 },
//       ],
//     },
//     {
//       id: "5c66b5f9-74a7-4767-8f5b-7d2b153b6057",
//       name: "Cozy Cabin",
//       host: "Alice Johnson",
//       price: 100,
//       description: "A warm and inviting cabin in the woods.",
//       amenities: "Fireplace, Hiking Trails, Mountain View",
//       reviews: [
//         { author: "Emma Wilson", comment: "So cozy and quiet!", rating: 5 },
//       ],
//     },
//     {
//       id: "3f477fd8-fc69-47f1-8c22-12dc4db86099",
//       name: "Modern Apartment",
//       host: "Chris Lee",
//       price: 200,
//       description: "A sleek and stylish city apartment with modern amenities.",
//       amenities: "Smart TV, High-Speed WiFi, Gym Access",
//       reviews: [
//         { author: "Liam Martinez", comment: "Perfect for business travel.", rating: 4 },
//       ],
//     },
//     {
//       id: "13e66193-3e0b-493d-bca2-94252343a5e3",
//       name: "Rustic Lakehouse",
//       host: "Laura White",
//       price: 180,
//       description: "A charming lakehouse with a beautiful view of the sunset.",
//       amenities: "Boat Dock, Fireplace, Private Garden",
//       reviews: [
//         { author: "Michael Scott", comment: "Absolutely stunning and relaxing!", rating: 5 },
//         { author: "Pam Beesly", comment: "Perfect place for a getaway.", rating: 4 },
//       ],
//     },
//     {
//       id: "377822b5-1601-43d9-866d-15db7932579f",
//       name: "Penthouse Suite",
//       host: "David Beckham",
//       price: 350,
//       description: "A luxurious penthouse with panoramic city views.",
//       amenities: "Private Pool, Rooftop Bar, 24/7 Butler Service",
//       reviews: [
//         { author: "Victoria Beckham", comment: "Luxury at its finest!", rating: 5 },
//         { author: "Elton John", comment: "Absolutely worth it!", rating: 5 },
//       ],
//     },
//   ];

//     const urlParams = new URLSearchParams(window.location.search);
//     const placeId = urlParams.get("id");

//     if (placeId) {
//       renderPlaceDetails(places, placeId);
//     } else {
//       renderPlaceList(places);
//     }

//     setupLoginForm();
//     setupLogoutButton();

//     const addReviewButton = document.getElementById("add-review-button");
//     if (addReviewButton) {
//       addReviewButton.addEventListener("click", () => {
//         const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";
//         if (isLoggedIn) {
//           window.location.href = `add-review.html?id=${placeId}`;
//         } else {
//           alert("You must be logged in to add a review!");
//           const redirectUrl = encodeURIComponent(`add-review.html?id=${placeId}`);
//           window.location.href = `login.html?redirect=${redirectUrl}`;
//         }
//       });
//     }
//   });

document.addEventListener("DOMContentLoaded", () => {
  const apiBaseUrl = "http://127.0.0.1:5000/api/v1"; // Base URL for the backend API
  let places = [];

  // Fetch places from the backend API
  async function fetchPlaces() {
    try {
      const response = await fetch(`${apiBaseUrl}/places`); // GET request to the API
      if (!response.ok) {
        throw new Error(`Error fetching places: ${response.statusText}`);
      }
      places = await response.json(); // Store fetched places globally
      console.log("Places fetched:", places); // Log to verify fetched data
      renderPlaceList(places); // Display fetched places
    } catch (error) {
      console.error("Error fetching places:", error);
      alert("Failed to fetch places. Please try again later.");
    }
  }

  // Render the list of places
  function renderPlaceList(places) {
    const placeList = document.querySelector(".place-list");
    const maxPriceFilter = document.getElementById("max-price");

    if (!placeList) return;

    // Display the filtered or full list of places
    function displayPlaces(list) {
      placeList.innerHTML = ""; // Clear the list before adding new elements
      list.forEach((place) => {
        const card = document.createElement("div");
        card.className = "place-card";
        card.innerHTML = `
          <h2>${place.name}</h2>
          <p>Price per night: ${place.price}€</p>
          <button class="details-btn" data-id="${place.id}">View Details</button>
        `;
        placeList.appendChild(card);
      });

      // Add event listeners to the "View Details" buttons
      document.querySelectorAll(".details-btn").forEach((btn) => {
        btn.addEventListener("click", (e) => {
          const pid = e.target.getAttribute("data-id");
          window.location.href = `place.html?id=${pid}`;
        });
      });
    }

    displayPlaces(places); // Display all places initially

    // Add filtering by max price
    if (maxPriceFilter) {
      maxPriceFilter.addEventListener("change", (e) => {
        const maxPrice = e.target.value === "all" ? Infinity : parseInt(e.target.value, 10);
        const filtered = places.filter((place) => place.price <= maxPrice);
        displayPlaces(filtered);
      });
    }
  }

  // Render the details of a specific place
  function renderPlaceDetails(places, placeId) {
    const place = places.find((p) => p.id === placeId);
    if (!place) {
      document.body.innerHTML = "<h1>Place not found</h1>";
      return;
    }

    document.getElementById("place-title").textContent = place.name;
    document.getElementById("place-host").textContent = place.host;
    document.getElementById("place-price").textContent = `${place.price}€`;
    document.getElementById("place-description").textContent = place.description;
    document.getElementById("place-amenities").textContent = place.amenities;

    const reviewsSection = document.getElementById("reviews-section");
    reviewsSection.innerHTML = place.reviews
      .map(
        (review) => `
        <div class="review">
          <p><strong>${review.author}:</strong></p>
          <p>${review.comment}</p>
          <p>Rating: ${"★".repeat(review.rating)}${"☆".repeat(5 - review.rating)}</p>
        </div>
      `
      )
      .join("");
  }

  // Fetch and display places on page load
  fetchPlaces();

  // Login form setup
  function setupLoginForm() {
    const loginForm = document.getElementById("login-form");
    if (!loginForm) return;

    loginForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const email = document.getElementById("email").value.trim();
      const password = document.getElementById("password").value.trim();

      // Mock user authentication
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

  // Logout button setup
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
});
