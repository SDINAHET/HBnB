// /*
//   This is a SAMPLE FILE to get you started.
//   Please, follow the project instructions to complete the tasks.
// */

// document.addEventListener("DOMContentLoaded", () => {
//   /* DO SOMETHING */
// // });
//   // Redirection des boutons "View Details"
//   const detailButtons = document.querySelectorAll(".details-btn");
//   detailButtons.forEach((button) => {
//     button.addEventListener("click", () => {
//       window.location.href = "place.html"; // Rediriger vers place.html
//     });
//   });

//   // Filtrage des places par prix
//   const maxPriceFilter = document.getElementById("max-price");
//   const placeCards = document.querySelectorAll(".place-card");

//   maxPriceFilter.addEventListener("change", (e) => {
//     const maxPrice = e.target.value === "all" ? Infinity : parseInt(e.target.value);

//     placeCards.forEach((card) => {
//       const priceText = card.querySelector("p").textContent;
//       const price = parseInt(priceText.match(/\$([0-9]+)/)[1]);

//       card.style.display = price <= maxPrice ? "block" : "none";
//     });
//   });
// });

// document.getElementById("login-form").addEventListener("submit", (e) => {
//   e.preventDefault();
//   const email = document.getElementById("email").value;
//   const password = document.getElementById("password").value;

//   console.log("Email:", email);
//   console.log("Password:", password);

//   // Remplacez par une requête à votre API pour authentifier l'utilisateur
//   alert("Login successful (logic to be implemented)");
// });



// document.addEventListener("DOMContentLoaded", () => {
//   // Place data
//   const places = [
//     {
//       name: "Beautiful Beach House",
//       price: 200,
//       details: "A stunning beachside retreat perfect for relaxation.",
//     },
//     {
//       name: "Cozy Mountain Cabin",
//       price: 150,
//       details: "Escape to the mountains with breathtaking views.",
//     },
//     {
//       name: "Modern City Apartment",
//       price: 100,
//       details: "Experience city life in a sleek, modern space.",
//     }
//   ];

//   // Populate place cards
//   const placeList = document.querySelector(".place-list");

//   places.forEach((place) => {
//     const card = document.createElement("div");
//     card.className = "place-card";
//     card.style.margin = "20px";
//     card.style.padding = "10px";
//     card.style.border = "1px solid #ddd";
//     card.style.borderRadius = "10px";

//     card.innerHTML = `
//       <h2>${place.name}</h2>
//       <p>Price: $${place.price}/night</p>
//       <p>${place.details}</p>
//       <button class="details-btn">View Details</button>
//     `;

//     placeList.appendChild(card);
//   });

//   // Redirect "View Details" buttons
//   const detailButtons = document.querySelectorAll(".details-btn");
//   detailButtons.forEach((button) => {
//     button.addEventListener("click", () => {
//       window.location.href = "place.html"; // Redirect to place.html
//     });
//   });

//   // Filter places by price
//   const maxPriceFilter = document.getElementById("max-price");
//   maxPriceFilter.addEventListener("change", (e) => {
//     const maxPrice = e.target.value === "all" ? Infinity : parseInt(e.target.value);

//     document.querySelectorAll(".place-card").forEach((card, index) => {
//       const price = places[index].price;
//       card.style.display = price <= maxPrice ? "block" : "none";
//     });
//   });

//   // Login form submission
//   const loginForm = document.getElementById("login-form");
//   if (loginForm) {
//     loginForm.addEventListener("submit", (e) => {
//       e.preventDefault();
//       const email = document.getElementById("email").value;
//       const password = document.getElementById("password").value;

//       console.log("Email:", email);
//       console.log("Password:", password);

//       // Replace with your authentication logic
//       alert("Login successful (logic to be implemented)");
//     });
//   }
// });


// document.addEventListener("DOMContentLoaded", () => {
//   // Récupère l'ID du lieu depuis l'URL
//   const urlParams = new URLSearchParams(window.location.search);
//   const placeId = urlParams.get("id");

//   // Exemple de données pour les lieux
//   const places = [
//     {
//       id: 1,
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
//       id: 2,
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
//       id: 3,
//       name: "Modern Apartment",
//       host: "Chris Lee",
//       price: 200,
//       description: "A sleek and stylish city apartment with modern amenities.",
//       amenities: "Smart TV, High-Speed WiFi, Gym Access",
//       reviews: [
//         { author: "Liam Martinez", comment: "Perfect for business travel.", rating: 4 },
//       ],
//     },
//   ];

// document.addEventListener("DOMContentLoaded", () => {
//   // // Exemple de données pour vos cartes
//   //   const places = [
//   //     { name: "Beautiful Beach House", price: "$150", description: "A stunning beachside retreat." },
//   //     { name: "Cozy Cabin", price: "$100", description: "A warm and inviting cabin in the woods." },
//   //     { name: "Modern Apartment", price: "$200", description: "A sleek city apartment with amenities." }
//   //   ];

//   // Récupérez le conteneur des cartes
//   const places = [
//     {
//       id: 1,
//       name: "Beautiful Beach House",
//       price: 150,
//       // details: "A stunning beachside retreat perfect for relaxation.",
//     },
//     {
//       id: 2,
//       name: "Cozy Cabin",
//       price: 100,
//       // details: "A warm and inviting cabin in the woods.",
//     },
//     {
//       id: 3,
//       name: "Modern Apartment",
//       price: 200,
//       // details: "A sleek and stylish city apartment with modern amenities.",
//     },
//   ];

//   const placeList = document.querySelector(".place-list");
//   const maxPriceFilter = document.getElementById("max-price");

//   // Function to render cards dynamically
//   function renderPlaces(filteredPlaces) {
//     placeList.innerHTML = ""; // Clear existing content
//     filteredPlaces.forEach((place) => {
//       const card = document.createElement("div");
//       card.className = "place-card";
//       card.style.margin = "20px";
//       card.style.padding = "10px";
//       card.style.border = "1px solid #ddd";
//       card.style.borderRadius = "10px";

//       card.innerHTML = `
//         <h2>${place.name}</h2>
//         <p>Price per night: $${place.price}</p>

//         <button class="details-btn" data-id="${place.id}">View Details</button>
//       `;

//       placeList.appendChild(card);
//     });

//     // Attach click event listeners to "View Details" buttons
//     const detailButtons = document.querySelectorAll(".details-btn");
//     detailButtons.forEach((button) => {
//       button.addEventListener("click", (e) => {
//         const placeId = e.target.getAttribute("data-id");
//         window.location.href = `place.html?id=${placeId}`; // Redirect with query parameter
//       });
//     });
//   }

//   // Initial render of all places
//   renderPlaces(places);

//   // Filter places by max price
//   maxPriceFilter.addEventListener("change", (e) => {
//     const maxPrice = e.target.value === "all" ? Infinity : parseInt(e.target.value, 10);
//     const filteredPlaces = places.filter((place) => place.price <= maxPrice);
//     renderPlaces(filteredPlaces);
//   });
// });



// document.addEventListener("DOMContentLoaded", () => {
//   // Récupère l'ID du lieu depuis l'URL
//   const urlParams = new URLSearchParams(window.location.search);
//   const placeId = urlParams.get("id");

//   // Exemple de données pour les lieux
//   const places = [
//     {
//       id: 1,
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
//       id: 2,
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
//       id: 3,
//       name: "Modern Apartment",
//       host: "Chris Lee",
//       price: 200,
//       description: "A sleek and stylish city apartment with modern amenities.",
//       amenities: "Smart TV, High-Speed WiFi, Gym Access",
//       reviews: [
//         { author: "Liam Martinez", comment: "Perfect for business travel.", rating: 4 },
//       ],
//     },
//   ];

  // Trouve le lieu correspondant à l'ID
//   const place = places.find((p) => p.id == placeId);

//   if (place) {
//     // Remplit les détails du lieu
//     document.getElementById("place-title").textContent = place.name;
//     document.getElementById("place-host").textContent = place.host;
//     document.getElementById("place-price").textContent = place.price;
//     document.getElementById("place-description").textContent = place.description;
//     document.getElementById("place-amenities").textContent = place.amenities;

//     // Remplit les avis
//     const reviewsSection = document.getElementById("reviews-section");
//     reviewsSection.innerHTML = ""; // Vide la section d'avis actuelle

//     place.reviews.forEach((review) => {
//       const reviewDiv = document.createElement("div");
//       reviewDiv.className = "review";
//       reviewDiv.innerHTML = `
//         <p><strong>${review.author}:</strong></p>
//         <p>${review.comment}</p>
//         <p>Rating: ${"★".repeat(review.rating)}${"☆".repeat(5 - review.rating)}</p>
//       `;
//       reviewsSection.appendChild(reviewDiv);
//     });
//   // } else {
//   //   // Si aucun lieu trouvé, affiche un message d'erreur
//   //   document.body.innerHTML = "<h1>Place not found</h1>";
//   // }
// });

// if (placeId) {
//   // Chargement des détails pour place.html
//   const place = places.find((p) => p.id == placeId);

//   if (place) {
//     document.getElementById("place-title").textContent = place.name;
//     document.getElementById("place-host").textContent = place.host;
//     document.getElementById("place-price").textContent = place.price;
//     document.getElementById("place-description").textContent = place.description;
//     document.getElementById("place-amenities").textContent = place.amenities;

//     const reviewsSection = document.getElementById("reviews-section");
//     reviewsSection.innerHTML = "";

//     place.reviews.forEach((review) => {
//       const reviewDiv = document.createElement("div");
//       reviewDiv.className = "review";
//       reviewDiv.innerHTML = `
//         <p><strong>${review.author}:</strong></p>
//         <p>${review.comment}</p>
//         <p>Rating: ${"★".repeat(review.rating)}${"☆".repeat(5 - review.rating)}</p>
//       `;
//       reviewsSection.appendChild(reviewDiv);
//     });
//   } else {
//     document.body.innerHTML = "<h1>Place not found</h1>";
//   }
// }
// });







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
    // Nouvel élément ajouté :
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

  // Vérifie si on est sur la page des détails ou de la liste
  const urlParams = new URLSearchParams(window.location.search);
  const placeId = urlParams.get("id");

  if (placeId) {
    renderPlaceDetails(places, placeId);
  } else {
    renderPlaceList(places);
  }
});

/**
 * Affiche les détails d'un lieu.
 */
function renderPlaceDetails(places, placeId) {
  const place = places.find((p) => p.id == placeId);

  if (!place) {
    document.body.innerHTML = "<h1>Place not found</h1>";
    return;
  }

  // Remplit les informations dynamiques
  document.getElementById("place-title").textContent = place.name;
  document.getElementById("place-host").textContent = place.host;
  document.getElementById("place-price").textContent = `${place.price}`;
  document.getElementById("place-description").textContent = place.description;
  document.getElementById("place-amenities").textContent = place.amenities;

  const reviewsSection = document.getElementById("reviews-section");
  reviewsSection.innerHTML = "";

  // Affiche les avis
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

/**
 * Affiche la liste des lieux.
 */
function renderPlaceList(places) {
  const placeList = document.querySelector(".place-list");
  const maxPriceFilter = document.getElementById("max-price");

  function displayPlaces(filteredPlaces) {
    placeList.innerHTML = ""; // Efface le contenu existant
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

    // Ajoute des événements aux boutons
    document.querySelectorAll(".details-btn").forEach((button) => {
      button.addEventListener("click", (e) => {
        const placeId = e.target.getAttribute("data-id");
        window.location.href = `place.html?id=${placeId}`;
      });
    });
  }

  // Affiche tous les lieux au chargement initial
  displayPlaces(places);

  // Filtre les lieux en fonction du prix
  maxPriceFilter.addEventListener("change", (e) => {
    const maxPrice = e.target.value === "all" ? Infinity : parseInt(e.target.value, 10);
    const filteredPlaces = places.filter((place) => place.price <= maxPrice);
    displayPlaces(filteredPlaces);
  });
}

/**
 * Gestion du formulaire de connexion.
 */
document.addEventListener("DOMContentLoaded", () => {
  const users = {
    "admin@hbnb.com": "admin1234",
  };

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
        window.location.href = "add_review.html";
      } else {
        const errorMessage = document.getElementById("error-message");
        errorMessage.style.display = "block";
        errorMessage.textContent = "Invalid email or password. Please try again.";
      }
    });
  }
});






// // Récupérer l'ID du lieu à partir de l'URL
// const urlParams = new URLSearchParams(window.location.search);
// const placeId = parseInt(urlParams.get("id"));

// // Trouver le lieu correspondant
// const place = places.find((p) => p.id === placeId);

// if (place) {
//   // Mettre à jour les informations dynamiques
//   document.getElementById("place-title").textContent = place.name;
//   document.getElementById("place-host").textContent = place.host;
//   document.getElementById("place-price").textContent = place.price;
//   document.getElementById("place-description").textContent = place.description;
//   document.getElementById("place-amenities").textContent = place.amenities;

//   // Afficher les avis existants
//   const reviewsSection = document.getElementById("reviews-section");
//   reviewsSection.innerHTML = ""; // Réinitialiser les avis existants
//   place.reviews.forEach((review) => {
//     const reviewDiv = document.createElement("div");
//     reviewDiv.className = "review";
//     reviewDiv.innerHTML = `
//       <p><strong>${review.author}:</strong></p>
//       <p>${review.comment}</p>
//       <p>Rating: ${"★".repeat(review.rating)}${"☆".repeat(5 - review.rating)}</p>
//     `;
//     reviewsSection.appendChild(reviewDiv);
//   });

//   // Gestion de la soumission du formulaire d'ajout d'avis
//   const reviewForm = document.getElementById("review-form");
//   reviewForm.addEventListener("submit", (e) => {
//     e.preventDefault();

//     const reviewText = document.getElementById("review").value;
//     const rating = parseInt(document.getElementById("rating").value);

//     // Ajouter le nouvel avis
//     const newReview = {
//       author: "Anonymous", // Vous pouvez personnaliser avec le nom de l'utilisateur connecté
//       comment: reviewText,
//       rating: rating,
//     };
//     place.reviews.push(newReview);

//     // Réafficher les avis
//     const reviewDiv = document.createElement("div");
//     reviewDiv.className = "review";
//     reviewDiv.innerHTML = `
//       <p><strong>${newReview.author}:</strong></p>
//       <p>${newReview.comment}</p>
//       <p>Rating: ${"★".repeat(newReview.rating)}${"☆".repeat(5 - newReview.rating)}</p>
//     `;
//     reviewsSection.appendChild(reviewDiv);

//     // Réinitialiser le formulaire
//     reviewForm.reset();
//     alert("Review submitted successfully!");
//   });
// // } else {
// //   document.body.innerHTML = "<h1>Place not found</h1>";
// // }
// });



// document.addEventListener("DOMContentLoaded", () => {
//   const places = [
//     {
//       id: 1,
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
//       id: 2,
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
//       id: 3,
//       name: "Modern Apartment",
//       host: "Chris Lee",
//       price: 200,
//       description: "A sleek and stylish city apartment with modern amenities.",
//       amenities: "Smart TV, High-Speed WiFi, Gym Access",
//       reviews: [
//         { author: "Liam Martinez", comment: "Perfect for business travel.", rating: 4 },
//       ],
//     },
//   ];

//   const urlParams = new URLSearchParams(window.location.search);
//   const placeId = urlParams.get("id");

//   if (placeId) {
//     renderPlaceDetails(places, placeId);
//   } else {
//     renderPlaceList(places);
//   }
// });

// // Fonction pour afficher les avis
// function displayReviews(reviews, container) {
//   container.innerHTML = ""; // Vide les avis existants
//   reviews.forEach((review) => {
//     const reviewDiv = document.createElement("div");
//     reviewDiv.className = "review";
//     reviewDiv.innerHTML = `
//       <p><strong>${review.author}:</strong></p>
//       <p>${review.comment}</p>
//       <p>Rating: ${"★".repeat(review.rating)}${"☆".repeat(5 - review.rating)}</p>
//     `;
//     container.appendChild(reviewDiv);
//   });
// }

// // Fonction pour afficher les détails d'un lieu
// function renderPlaceDetails(places, placeId) {
//   const place = places.find((p) => p.id == placeId);

//   if (!place) {
//     document.body.innerHTML = "<h1>Place not found</h1>";
//     return;
//   }

//   document.getElementById("place-title").textContent = place.name;
//   document.getElementById("place-host").textContent = place.host;
//   document.getElementById("place-price").textContent = `$${place.price}`;
//   document.getElementById("place-description").textContent = place.description;
//   document.getElementById("place-amenities").textContent = place.amenities;

//   const reviewsSection = document.getElementById("reviews-section");
//   displayReviews(place.reviews, reviewsSection);

//   // Gestion de l'ajout d'un avis
//   const reviewForm = document.getElementById("review-form");
//   reviewForm.addEventListener("submit", (e) => handleReviewSubmit(e, place, reviewsSection));
// }

// // Fonction pour gérer la soumission d'un avis
// function handleReviewSubmit(event, place, reviewsSection) {
//   event.preventDefault();

//   const reviewInput = document.getElementById("review");
//   const ratingInput = document.getElementById("rating");

//   const reviewText = reviewInput.value.trim();
//   const rating = parseInt(ratingInput.value);

//   if (!reviewText || isNaN(rating)) {
//     alert("Please fill in both the review and rating.");
//     return;
//   }

//   const newReview = {
//     author: "Anonymous",
//     comment: reviewText,
//     rating: rating,
//   };

//   place.reviews.push(newReview);
//   displayReviews(place.reviews, reviewsSection);

//   reviewInput.value = ""; // Réinitialise le formulaire
//   ratingInput.value = "1";
//   alert("Review submitted successfully!");
// }

// // Fonction pour afficher la liste des lieux
// function renderPlaceList(places) {
//   const placeList = document.querySelector(".place-list");
//   const maxPriceFilter = document.getElementById("max-price");

//   function displayPlaces(filteredPlaces) {
//     placeList.innerHTML = "";
//     filteredPlaces.forEach((place) => {
//       const card = document.createElement("div");
//       card.className = "place-card";
//       card.innerHTML = `
//         <h2>${place.name}</h2>
//         <p>Price per night: $${place.price}</p>
//         <button class="details-btn" data-id="${place.id}">View Details</button>
//       `;
//       placeList.appendChild(card);
//     });

//     document.querySelectorAll(".details-btn").forEach((button) => {
//       button.addEventListener("click", (e) => {
//         const placeId = e.target.getAttribute("data-id");
//         window.location.href = `place.html?id=${placeId}`;
//       });
//     });
//   }

//   displayPlaces(places);

//   maxPriceFilter.addEventListener("change", (e) => {
//     const maxPrice = e.target.value === "all" ? Infinity : parseInt(e.target.value, 10);
//     const filteredPlaces = places.filter((place) => place.price <= maxPrice);
//     displayPlaces(filteredPlaces);
//   });
// }

document.addEventListener("DOMContentLoaded", () => {
  const addReviewButton = document.getElementById("add-review-button");

  // Vérifie si l'utilisateur est connecté
  const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";
  const urlParams = new URLSearchParams(window.location.search);
  const placeId = urlParams.get("id"); // Récupère l'ID du lieu actuel

  if (addReviewButton) {
    addReviewButton.addEventListener("click", (e) => {
      e.preventDefault();

      if (isLoggedIn) {
        // Redirige vers la page add_review.html avec l'ID de la card correspondante
        window.location.href = `add_review.html?id=${placeId}`;
      } else {
        // Si l'utilisateur n'est pas connecté, redirige vers login.html
        alert("You must be logged in to add a review!");
        window.location.href = "login.html";
      }
    });
  }
});
