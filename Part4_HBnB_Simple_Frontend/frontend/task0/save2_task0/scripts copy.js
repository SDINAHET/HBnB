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
  // Données des lieux
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
  ];

  // Vérifie si on est sur la page des cartes ou des détails
  const urlParams = new URLSearchParams(window.location.search);
  const placeId = urlParams.get("id");

  if (placeId) {
    // Page des détails
    const place = places.find((p) => p.id == placeId);

    if (place) {
      // Remplir les informations dynamiques
      document.getElementById("place-title").textContent = place.name;
      document.getElementById("place-host").textContent = place.host;
      document.getElementById("place-price").textContent = `${place.price}`;
      document.getElementById("place-description").textContent = place.description;
      document.getElementById("place-amenities").textContent = place.amenities;

      const reviewsSection = document.getElementById("reviews-section");
      reviewsSection.innerHTML = "";

      // Générer les avis dynamiquement
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
    } else {
      document.body.innerHTML = "<h1>Place not found</h1>";
    }
  } else {
    // Page principale avec les cartes
    const placeList = document.querySelector(".place-list");
    const maxPriceFilter = document.getElementById("max-price");

    // Fonction pour afficher les lieux
    function renderPlaces(filteredPlaces) {
      placeList.innerHTML = ""; // Effacer le contenu existant
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

      // Ajoute des événements pour les boutons "View Details"
      document.querySelectorAll(".details-btn").forEach((button) => {
        button.addEventListener("click", (e) => {
          const placeId = e.target.getAttribute("data-id");
          window.location.href = `place.html?id=${placeId}`;
        });
      });
    }

    // Afficher tous les lieux au chargement initial
    renderPlaces(places);

    // Filtrer les lieux par prix
    maxPriceFilter.addEventListener("change", (e) => {
      const maxPrice = e.target.value === "all" ? Infinity : parseInt(e.target.value, 10);
      const filteredPlaces = places.filter((place) => place.price <= maxPrice);
      renderPlaces(filteredPlaces);
    });
  }
});


document.addEventListener("DOMContentLoaded", () => {
  // Dictionnaire des utilisateurs autorisés
  const users = {
    "admin@hbnb.com": "admin1234",
  };

  // Gestion du formulaire de connexion
  const loginForm = document.getElementById("login-form");

  loginForm.addEventListener("submit", (e) => {
    e.preventDefault();

    // Récupération des données du formulaire
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    // Vérification des identifiants
    if (users[email] && users[email] === password) {
      localStorage.setItem("isLoggedIn", "true"); // Enregistre la session
      localStorage.setItem("userEmail", email);  // Optionnel : Enregistre l'email
      alert("Login successful!");               // Affiche le message de succès
      window.location.href = "add_review.html"; // Redirige vers add_review.html
    } else {
      // Affiche un message d'erreur si les identifiants sont invalides
      const errorMessage = document.getElementById("error-message");
      errorMessage.style.display = "block";
      errorMessage.textContent = "Invalid email or password. Please try again.";
    }
  });
});


  // // Vérification de l'accès à "add_review.html"
  // if (window.location.pathname.endsWith("add_review.html")) {
  //   const isLoggedIn = localStorage.getItem("isLoggedIn");

  //   // Si l'utilisateur n'est pas connecté, redirige vers la page de connexion
  //   if (isLoggedIn !== "true") {
  //     // alert("You must be logged in to access this page!");
  //     window.location.href = "login.html";
  //   }
  // }
// });

// document.addEventListener("DOMContentLoaded", () => {
//   const logoutButton = document.getElementById("logout-button");

//   if (logoutButton) {
//     logoutButton.addEventListener("click", () => {
//       localStorage.removeItem("isLoggedIn");
//       localStorage.removeItem("userEmail");
//       alert("You have been logged out!");
//       window.location.href = "login.html";
//     });
//   }
// });


document.addEventListener("DOMContentLoaded", () => {
  // Gestion du formulaire de connexion
  const loginForm = document.getElementById("login-form");
  if (loginForm) {
    loginForm.addEventListener("submit", handleLogin);
  }

  // Vérification d'accès à add_review.html
  if (window.location.pathname.endsWith("add_review.html")) {
    checkAccess();
  }

  // Gestion de la déconnexion
  const logoutButton = document.getElementById("logout-button");
  if (logoutButton) {
    logoutButton.addEventListener("click", handleLogout);
  }
});

// document.addEventListener("DOMContentLoaded", () => {
//   // Vérifier si l'utilisateur est connecté
//   const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";

//   if (!isLoggedIn) {
//     alert("You must be logged in to add a review!");
//     window.location.href = "login.html";
//     return;
//   }

//   // Données d'exemple pour les lieux
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
//   ];

//   // Charger les détails du lieu
//   const urlParams = new URLSearchParams(window.location.search);
//   const placeId = parseInt(urlParams.get("id"), 10);
//   const place = places.find((p) => p.id === placeId);

//   if (place) {
//     // Remplir les détails dynamiquement
//     document.getElementById("place-title").textContent = place.name;
//     document.getElementById("place-host").textContent = place.host;
//     document.getElementById("place-price").textContent = place.price;
//     document.getElementById("place-description").textContent = place.description;
//     document.getElementById("place-amenities").textContent = place.amenities;

//     // Afficher les avis existants
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

//     // Gestion du formulaire d'ajout d'avis
//     const reviewForm = document.getElementById("review-form");
//     reviewForm.addEventListener("submit", (e) => {
//       e.preventDefault();

//       // Récupérer les données du formulaire
//       const reviewText = document.getElementById("review").value;
//       const rating = parseInt(document.getElementById("rating").value, 10);

//       // Ajouter le nouvel avis
//       const newReview = {
//         author: localStorage.getItem("userEmail") || "Anonymous",
//         comment: reviewText,
//         rating: rating,
//       };
//       place.reviews.push(newReview);

//       // Afficher le nouvel avis
//       const newReviewDiv = document.createElement("div");
//       newReviewDiv.className = "review";
//       newReviewDiv.innerHTML = `
//         <p><strong>${newReview.author}:</strong></p>
//         <p>${newReview.comment}</p>
//         <p>Rating: ${"★".repeat(newReview.rating)}${"☆".repeat(5 - newReview.rating)}</p>
//       `;
//       reviewsSection.appendChild(newReviewDiv);

//       // Réinitialiser le formulaire
//       reviewForm.reset();
//       alert("Your review has been submitted successfully!");
//     });
//   } else {
//     document.body.innerHTML = "<h1>Place not found</h1>";
//   }
// });
