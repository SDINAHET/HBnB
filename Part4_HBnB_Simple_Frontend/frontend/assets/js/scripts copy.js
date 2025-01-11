document.addEventListener("DOMContentLoaded", () => {
  // Données statiques
  const places = [
    {
      id: "765a38e6-c131-4315-8e9c-28ac88424634",
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
      id: "5c66b5f9-74a7-4767-8f5b-7d2b153b6057",
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
      id: "3f477fd8-fc69-47f1-8c22-12dc4db86099",
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
      id: "13e66193-3e0b-493d-bca2-94252343a5e3",
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
      id: "377822b5-1601-43d9-866d-15db7932579f",
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

  // Récupère l'ID du lieu (si présent) depuis l'URL
  const urlParams = new URLSearchParams(window.location.search);
  const placeId = urlParams.get("id");

  // Affiche soit la liste des lieux, soit les détails d'un lieu
  if (placeId) {
    renderPlaceDetails(places, placeId);
  } else {
    renderPlaceList(places);
  }

  // Initialise le formulaire de connexion (si présent sur la page)
  setupLoginForm();
  // Initialise le bouton de déconnexion (si présent sur la page)
  setupLogoutButton();

  // Initialise le bouton "Add Review" sur place.html (si présent)
  const addReviewButton = document.getElementById("add-review-button");
  if (addReviewButton) {
    addReviewButton.addEventListener("click", () => {
      const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";
      const placeIdParam = new URLSearchParams(window.location.search).get("id");
      if (isLoggedIn) {
        window.location.href = `add-review.html?id=${placeIdParam}`;
      } else {
        alert("You must be logged in to add a review!");
        const redirectUrl = encodeURIComponent(`add-review.html?id=${placeIdParam}`);
        window.location.href = `login.html?redirect=${redirectUrl}`;
      }
    });
  }
});




/**
 * Affiche la liste des lieux sur la page index.html.
 */
function renderPlaceList(places) {
  const placeList = document.querySelector(".place-list");
  const maxPriceFilter = document.getElementById("max-price");
  if (!placeList) return;

  function displayPlaces(list) {
    placeList.innerHTML = "";
    list.forEach((place) => {
      const card = document.createElement("div");
      card.className = "place-card";
      card.innerHTML = `
        <h2>${place.name}</h2>
        <p>Price per night: $${place.price}</p>
        <button class="details-btn" data-id="${place.id}">View Details</button>
      `;
      placeList.appendChild(card);
    });

    // Chaque bouton "View Details" redirige vers place.html?id=...
    document.querySelectorAll(".details-btn").forEach((btn) => {
      btn.addEventListener("click", (e) => {
        const pid = e.target.getAttribute("data-id");
        window.location.href = `place.html?id=${pid}`;
      });
    });
  }

  // Premier affichage : tous les lieux
  displayPlaces(places);

  // Filtre par prix maximal
  if (maxPriceFilter) {
    maxPriceFilter.addEventListener("change", (e) => {
      const value = e.target.value;
      const maxPrice = value === "all" ? Infinity : parseInt(value, 10);
      const filtered = places.filter((p) => p.price <= maxPrice);
      displayPlaces(filtered);
    });
  }
}

/**
 * Affiche les détails d'un lieu sur la page place.html.
 */
function renderPlaceDetails(places, placeId) {
  const place = places.find((p) => p.id == placeId);
  if (!place) {
    document.body.innerHTML = "<h1>Place not found</h1>";
    return;
  }

  const title = document.getElementById("place-title");
  const host = document.getElementById("place-host");
  const price = document.getElementById("place-price");
  const description = document.getElementById("place-description");
  const amenities = document.getElementById("place-amenities");
  const reviewsSection = document.getElementById("reviews-section");

  if (title) title.textContent = place.name;
  if (host) host.textContent = place.host;
  if (price) price.textContent = place.price;
  if (description) description.textContent = place.description;
  if (amenities) amenities.textContent = place.amenities;

  if (reviewsSection) {
    reviewsSection.innerHTML = "";
    place.reviews.forEach((review) => {
      const div = document.createElement("div");
      div.className = "review";
      div.innerHTML = `
        <p><strong>${review.author}:</strong></p>
        <p>${review.comment}</p>
        <p>Rating: ${"★".repeat(review.rating)}${"☆".repeat(5 - review.rating)}</p>
      `;
      reviewsSection.appendChild(div);
    });
  }
}

/**
 * Initialise le formulaire de connexion.
 */
function setupLoginForm() {
  const loginForm = document.getElementById("login-form");
  if (!loginForm) return;

  loginForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();

    // Exemples d'utilisateurs autorisés
    const users = { "admin@hbnb.com": "admin1234" };

    if (users[email] && users[email] === password) {
      localStorage.setItem("isLoggedIn", "true");
      localStorage.setItem("userEmail", email);
      alert("Login successful!");

      const redirectUrl = new URLSearchParams(window.location.search).get("redirect");
      window.location.href = redirectUrl ? decodeURIComponent(redirectUrl) : "index.html";
    } else {
      alert("Invalid email or password. Please try again.");
    }
  });document.addEventListener("DOMContentLoaded", () => {
    // const places = [
    //   {
    //     id: 1,
    //     name: "Beautiful Beach House",
    //     host: "John Doe",
    //     price: 150,
    //     description: "A beautiful beach house with amazing views...",
    //     amenities: "WiFi, Pool, Air Conditioning",
    //     reviews: [
    //       { author: "Jane Smith", comment: "Great place to stay!", rating: 4 },
    //       { author: "Robert Brown", comment: "Amazing location and very comfortable.", rating: 5 },
    //     ],
    //   },
    //   {
    //     id: 2,
    //     name: "Cozy Cabin",
    //     host: "Alice Johnson",
    //     price: 100,
    //     description: "A warm and inviting cabin in the woods.",
    //     amenities: "Fireplace, Hiking Trails, Mountain View",
    //     reviews: [
    //       { author: "Emma Wilson", comment: "So cozy and quiet!", rating: 5 },
    //     ],
    //   },
    //   {
    //     id: 3,
    //     name: "Modern Apartment",
    //     host: "Chris Lee",
    //     price: 200,
    //     description: "A sleek and stylish city apartment with modern amenities.",
    //     amenities: "Smart TV, High-Speed WiFi, Gym Access",
    //     reviews: [
    //       { author: "Liam Martinez", comment: "Perfect for business travel.", rating: 4 },
    //     ],
    //   },
    // ];

    const urlParams = new URLSearchParams(window.location.search);
    const placeId = parseInt(urlParams.get("id"), 10);

    if (!placeId) {
      alert("Invalid Place ID");
      window.location.href = "index.html";
      return;
    }

    const place = places.find((p) => p.id === placeId);

    if (!place) {
      alert("Place not found!");
      window.location.href = "index.html";
      return;
    }

    // Charger les détails du lieu
    document.getElementById("place-title").textContent = place.name;
    document.getElementById("place-host").textContent = place.host;
    document.getElementById("place-price").textContent = place.price;
    document.getElementById("place-description").textContent = place.description;
    document.getElementById("place-amenities").textContent = place.amenities;

    // Charger les avis
    const reviewsSection = document.getElementById("reviews-section");
    if (place.reviews.length > 0) {
      place.reviews.forEach((review) => {
        const reviewCard = document.createElement("div");
        reviewCard.className = "review-card";
        reviewCard.innerHTML = `
          <p><strong>${review.author}:</strong></p>
          <p>${review.comment}</p>
          <p>Rating: ${"★".repeat(review.rating)}${"☆".repeat(5 - review.rating)}</p>
        `;
        reviewsSection.appendChild(reviewCard);
      });
    } else {
      reviewsSection.innerHTML = "<p>No reviews yet.</p>";
    }

    // Ajouter un bouton ou formulaire d'ajout d'avis
    const addReviewContainer = document.getElementById("add-review-container");
    const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";

    if (isLoggedIn) {
      const addReviewForm = document.createElement("form");
      addReviewForm.className = "add-review form";
      addReviewForm.innerHTML = `
        <h2>Add a Review</h2>
        <label for="review-comment">Your review:</label>
        <textarea id="review-comment" name="review" required></textarea>

        <label for="review-rating">Rating:</label>
        <select id="review-rating" name="rating" required>
          <option value="1">1 Star</option>
          <option value="2">2 Stars</option>
          <option value="3">3 Stars</option>
          <option value="4">4 Stars</option>
          <option value="5">5 Stars</option>
        </select>

        <button type="submit">Submit Review</button>
      `;

      addReviewForm.addEventListener("submit", (e) => {
        e.preventDefault();

        const comment = document.getElementById("review-comment").value.trim();
        const rating = parseInt(document.getElementById("review-rating").value, 10);

        if (!comment || !rating) {
          alert("Please fill out all fields!");
          return;
        }

        // Simuler l'ajout de la review
        console.log("New Review Submitted:", { comment, rating });
        alert("Review submitted successfully!");
        window.location.reload();
      });

      addReviewContainer.appendChild(addReviewForm);
    } else {
      const addReviewButton = document.createElement("button");
      addReviewButton.className = "button add-review";
      addReviewButton.textContent = "Add Review";
      addReviewButton.addEventListener("click", () => {
        const redirectUrl = encodeURIComponent(`add-review.html?id=${placeId}`);
        window.location.href = `login.html?redirect=${redirectUrl}`;
      });

      addReviewContainer.appendChild(addReviewButton);
    }
  });

}

/**
 * Gère la déconnexion.
 */
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
