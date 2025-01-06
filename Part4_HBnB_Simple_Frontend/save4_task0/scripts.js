document.addEventListener("DOMContentLoaded", () => {
  // Définition des données statiques pour les lieux
  const places = [
    {
      id: 1,
      name: "Beautiful Beach House",
      host: "John Doe",
      price: 150,
      description: "A beautiful beach house with amazing views...",
      amenities: "WiFi, Pool, Air Conditioning",
      reviews: [
        { author: "Jane Smith", comment: "Great place to stay!", rating: 4 },
        { author: "Robert Brown", comment: "Amazing location and very comfortable.", rating: 5 },
      ],
    },
    {
      id: 2,
      name: "Cozy Cabin",
      host: "Alice Johnson",
      price: 100,
      description: "A warm and inviting cabin in the woods.",
      amenities: "Fireplace, Hiking Trails, Mountain View",
      reviews: [
        { author: "Emma Wilson", comment: "So cozy and quiet!", rating: 5 },
      ],
    },
    {
      id: 3,
      name: "Modern Apartment",
      host: "Chris Lee",
      price: 200,
      description: "A sleek and stylish city apartment with modern amenities.",
      amenities: "Smart TV, High-Speed WiFi, Gym Access",
      reviews: [
        { author: "Liam Martinez", comment: "Perfect for business travel.", rating: 4 },
      ],
    },
    {
      id: 4,
      name: "Rustic Lakehouse",
      host: "Laura White",
      price: 180,
      description: "A charming lakehouse with a beautiful view of the sunset.",
      amenities: "Boat Dock, Fireplace, Private Garden",
      reviews: [
        { author: "Michael Scott", comment: "Absolutely stunning and relaxing!", rating: 5 },
        { author: "Pam Beesly", comment: "Perfect place for a getaway.", rating: 4 },
      ],
    },
    {
      id: 5,
      name: "Penthouse Suite",
      host: "David Beckham",
      price: 350,
      description: "A luxurious penthouse with panoramic city views.",
      amenities: "Private Pool, Rooftop Bar, 24/7 Butler Service",
      reviews: [
        { author: "Victoria Beckham", comment: "Luxury at its finest!", rating: 5 },
        { author: "Elton John", comment: "Absolutely worth it!", rating: 5 },
      ],
    },
  ];

  // Récupération de l'ID de la page (place.html ou index.html)
  const urlParams = new URLSearchParams(window.location.search);
  const placeId = urlParams.get("id");

  // Vérification de la page à afficher
  if (placeId) {
    renderPlaceDetails(places, placeId);
  } else {
    renderPlaceList(places);
  }

  // Initialisation du formulaire de connexion
  setupLoginForm();
});

/**
 * Affiche les détails d'un lieu sur la page place.html.
 */
function renderPlaceDetails(places, placeId) {
  const place = places.find((p) => p.id == placeId);

  if (!place) {
    document.body.innerHTML = "<h1>Place not found</h1>";
    return;
  }

  // Vérification des éléments DOM avant de les manipuler
  const placeTitle = document.getElementById("place-title");
  const placeHost = document.getElementById("place-host");
  const placePrice = document.getElementById("place-price");
  const placeDescription = document.getElementById("place-description");
  const placeAmenities = document.getElementById("place-amenities");
  const reviewsSection = document.getElementById("reviews-section");

  if (placeTitle) placeTitle.textContent = place.name;
  if (placeHost) placeHost.textContent = place.host;
  if (placePrice) placePrice.textContent = `$${place.price}`;
  if (placeDescription) placeDescription.textContent = place.description;
  if (placeAmenities) placeAmenities.textContent = place.amenities;

  if (reviewsSection) {
    reviewsSection.innerHTML = ""; // Clear existing reviews
    place.reviews.forEach((review) => {
      const reviewDiv = document.createElement("div");
      reviewDiv.className = "review";
      reviewDiv.innerHTML = `
        <p><strong>${review.author}:</strong></p>
        <p>${review.comment}</p>
        <p>Rating: ${"★".repeat(review.rating)}${"☆".repeat(5 - review.rating)}</p>
      `;
      reviewsSection.appendChild(reviewDiv);
    });
  }
}

/**
 * Affiche la liste des lieux sur la page index.html.
 */
function renderPlaceList(places) {
  const placeList = document.querySelector(".place-list");
  const maxPriceFilter = document.getElementById("max-price");

  if (!placeList) return;

  function displayPlaces(filteredPlaces) {
    placeList.innerHTML = ""; // Clear existing list
    filteredPlaces.forEach((place) => {
      const card = document.createElement("div");
      card.className = "place-card";
      card.innerHTML = `
        <h2>${place.name}</h2>
        <p>Price per night: $${place.price}</p>
        <button class="details-btn" data-id="${place.id}">View Details</button>
      `;
      placeList.appendChild(card);
    });

    // Add event listeners to buttons
    document.querySelectorAll(".details-btn").forEach((button) => {
      button.addEventListener("click", (e) => {
        const placeId = e.target.getAttribute("data-id");
        window.location.href = `place.html?id=${placeId}`;
      });
    });
  }

  // Initial rendering
  displayPlaces(places);

  // Filtering by price
  if (maxPriceFilter) {
    maxPriceFilter.addEventListener("change", (e) => {
      const maxPrice = e.target.value === "all" ? Infinity : parseInt(e.target.value, 10);
      const filteredPlaces = places.filter((place) => place.price <= maxPrice);
      displayPlaces(filteredPlaces);
    });
  }
}

/**
 * Initialise le formulaire de connexion sur la page login.html.
 */
function setupLoginForm() {
  const users = { "admin@hbnb.com": "admin1234" };
  const loginForm = document.getElementById("login-form");

  if (loginForm) {
    loginForm.addEventListener("submit", (e) => {
      e.preventDefault();

      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;

      if (users[email] && users[email] === password) {
        localStorage.setItem("isLoggedIn", "true");
        localStorage.setItem("userEmail", email);
        alert("Login successful!");
        window.location.href = "index.html";
      } else {
        alert("Invalid email or password. Please try again.");
      }
    });
  }
}
