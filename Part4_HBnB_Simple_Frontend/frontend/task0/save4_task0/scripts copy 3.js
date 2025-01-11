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




// document.addEventListener("DOMContentLoaded", () => {
//   const addReviewButton = document.getElementById("add-review-button");

//   // Vérifie si l'utilisateur est connecté
//   const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";
//   const urlParams = new URLSearchParams(window.location.search);
//   const placeId = urlParams.get("id"); // Récupère l'ID du lieu actuel

//   if (addReviewButton) {
//     addReviewButton.addEventListener("click", (e) => {
//       e.preventDefault();

//       if (isLoggedIn) {
//         // Redirige vers la page add_review.html avec l'ID de la card correspondante
//         window.location.href = `add_review.html?id=${placeId}`;
//       } else {
//         // Si l'utilisateur n'est pas connecté, redirige vers login.html
//         alert("You must be logged in to add a review!");
//         window.location.href = "login.html";
//       }
//     });
//   }
// });



// document.addEventListener("DOMContentLoaded", () => {
//   const addReviewButton = document.getElementById("add-review-button");
//   const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";
//   const urlParams = new URLSearchParams(window.location.search);
//   const placeId = urlParams.get("id");

//   if (isLoggedIn) {
//     // Replace the button with a form
//     const reviewForm = document.createElement("form");
//     reviewForm.className = "add-review-form";
//     reviewForm.innerHTML = `
//       <label for="review">Write your review:</label>
//       <textarea id="review" name="review" required></textarea>
//       <label for="rating">Rating:</label>
//       <select id="rating" name="rating" required>
//         <option value="1">1 Star</option>
//         <option value="2">2 Stars</option>
//         <option value="3">3 Stars</option>
//         <option value="4">4 Stars</option>
//         <option value="5" selected>5 Stars</option>
//       </select>
//       <button type="submit" class="submit-review">Submit Review</button>
//     `;

//     addReviewButton.replaceWith(reviewForm);

//     // Handle form submission
//     reviewForm.addEventListener("submit", (e) => {
//       e.preventDefault();
//       const reviewText = document.getElementById("review").value;
//       const rating = parseInt(document.getElementById("rating").value);

//       // Add review logic here
//       alert(`Review submitted successfully: ${reviewText}, ${rating} stars`);
//       reviewForm.reset();
//     });
//   } else {
//     // Handle button click for unauthenticated users
//     addReviewButton.addEventListener("click", () => {
//       alert("You must be logged in to add a review!");
//       window.location.href = "login.html";
//     });
//   }
// });

// document.addEventListener("DOMContentLoaded", () => {
//   const addReviewButton = document.getElementById("add-review-button");
//   const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";
//   const urlParams = new URLSearchParams(window.location.search);
//   const placeId = urlParams.get("id"); // Get the place ID from the URL

//   // Check if the user is logged in
//   if (isLoggedIn) {
//     // Redirect to add-review.html
//     if (addReviewButton) {
//       addReviewButton.addEventListener("click", () => {
//         window.location.href = `add-review.html?id=${placeId}`;
//       });
//     }
//   } else {
//     // Redirect to login.html with a return URL to add-review.html
//     if (addReviewButton) {
//       addReviewButton.addEventListener("click", () => {
//         alert("You must be logged in to add a review!");
//         const currentUrl = encodeURIComponent(`add-review.html?id=${placeId}`);
//         window.location.href = `login.html?redirect=${currentUrl}`;
//       });
//     }

//     // Handle redirect after login
//     const redirectUrl = urlParams.get("redirect");
//     if (redirectUrl) {
//       localStorage.setItem("redirectAfterLogin", redirectUrl); // Save the redirect URL for post-login navigation
//     }
//   }
// });

// Handle post-login redirection
// document.addEventListener("DOMContentLoaded", () => {
//   const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";

//   if (isLoggedIn) {
//     const redirectAfterLogin = localStorage.getItem("redirectAfterLogin");
//     if (redirectAfterLogin) {
//       localStorage.removeItem("redirectAfterLogin"); // Clear the saved redirect URL
//       window.location.href = redirectAfterLogin; // Redirect to the saved URL
//     }
//   }
// });

// ************************

// document.addEventListener("DOMContentLoaded", () => {
//   const addReviewButton = document.getElementById("add-review-button");

//   // Check if the user is on the add_review.html page
//   const urlParams = new URLSearchParams(window.location.search);
//   const currentPage = window.location.pathname; // Get current page path
//   const placeId = urlParams.get("id"); // Get the ID of the current place

//   const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";

//   if (currentPage.includes("add_review.html")) {
//     // User is on the add_review.html page
//     if (!isLoggedIn) {
//       // Redirect to login.html if not logged in
//       const currentUrl = encodeURIComponent(window.location.href); // Save current URL
//       alert("You must be logged in to add a review!");
//       window.location.href = `login.html?redirect=${currentUrl}`;
//     } else {
//       // User is logged in, proceed with rendering the Add Review page
//       console.log("User is logged in. Rendering Add Review page...");
//     }
//   }

//   if (addReviewButton) {
//     // Add event listener for the "Add Review" button
//     addReviewButton.addEventListener("click", (e) => {
//       e.preventDefault();

//       if (isLoggedIn) {
//         // Redirect to add_review.html with the place ID
//         window.location.href = `add_review.html?id=${placeId}`;
//       } else {
//         // Redirect to login.html if not logged in
//         alert("You must be logged in to add a review!");
//         const redirectUrl = encodeURIComponent(`add_review.html?id=${placeId}`);
//         window.location.href = `login.html?redirect=${redirectUrl}`;
//       }
//     });
//   }
// });

// ***********

// document.addEventListener("DOMContentLoaded", () => {
//   const reviewForm = document.getElementById("review-form");
//   const urlParams = new URLSearchParams(window.location.search);
//   const placeId = urlParams.get("id");

//   // Set the placeId in the hidden input field
//   if (placeId) {
//     document.getElementById("place-id").value = placeId;
//   }

//   // Handle review submission
//   reviewForm.addEventListener("submit", (e) => {
//     e.preventDefault();

//     const reviewText = document.getElementById("review").value.trim();
//     const rating = parseInt(document.getElementById("rating").value);
//     const placeId = document.getElementById("place-id").value;

//     if (!reviewText || isNaN(rating) || !placeId) {
//       alert("Please fill out all fields.");
//       return;
//     }

//     // Create a review object
//     const review = {
//       placeId: placeId,
//       review: reviewText,
//       rating: rating,
//       author: localStorage.getItem("userEmail") || "Anonymous",
//     };

//     // Save to localStorage or send to API
//     saveReview(review);

//     // Reset form
//     reviewForm.reset();
//     alert("Review submitted successfully!");
//   });
// });

// // Function to save review data
// function saveReview(review) {
//   let reviews = JSON.parse(localStorage.getItem("reviews")) || [];
//   reviews.push(review);
//   localStorage.setItem("reviews", JSON.stringify(reviews));
// }


// document.addEventListener("DOMContentLoaded", () => {
//   const urlParams = new URLSearchParams(window.location.search);
//   const placeId = urlParams.get("id");

//   if (placeId) {
//     renderReviews(placeId);
//   }
// });

// // Function to fetch and render reviews for a specific place
// function renderReviews(placeId) {
//   const reviews = JSON.parse(localStorage.getItem("reviews")) || [];
//   const placeReviews = reviews.filter((review) => review.placeId === placeId);

//   const reviewsSection = document.getElementById("reviews-section");
//   reviewsSection.innerHTML = ""; // Clear existing reviews

//   if (placeReviews.length === 0) {
//     reviewsSection.innerHTML = "<p>No reviews yet. Be the first to add one!</p>";
//     return;
//   }

//   placeReviews.forEach((review) => {
//     const reviewCard = document.createElement("div");
//     reviewCard.className = "review-card";
//     reviewCard.innerHTML = `
//       <p><strong>${review.author}:</strong></p>
//       <p>${review.review}</p>
//       <p>Rating: ${"★".repeat(review.rating)}${"☆".repeat(5 - review.rating)}</p>
//     `;
//     reviewsSection.appendChild(reviewCard);
//   });
// }

// document.addEventListener("DOMContentLoaded", () => {
//   const addReviewButton = document.getElementById("add-review-button");
//   const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";
//   const urlParams = new URLSearchParams(window.location.search);
//   const placeId = urlParams.get("id");
//   const redirectAfterLogin = urlParams.get("redirect");

//   // Handle redirection after login
//   if (redirectAfterLogin && isLoggedIn) {
//     window.location.href = redirectAfterLogin;
//     return;
//   }

//   // Add Review Button Logic
//   if (addReviewButton) {
//     addReviewButton.addEventListener("click", (e) => {
//       e.preventDefault();

//       if (!placeId) {
//         alert("Invalid place. Please try again.");
//         return;
//       }

//       if (isLoggedIn) {
//         // Redirect to add_review.html with the place ID
//         window.location.href = `add_review.html?id=${placeId}`;
//       } else {
//         // Redirect to login.html with a return URL for add_review.html
//         const redirectUrl = encodeURIComponent(`add_review.html?id=${placeId}`);
//         alert("You must be logged in to add a review!");
//         window.location.href = `login.html?redirect=${redirectUrl}`;
//       }
//     });
//   }

//   // Check if the user is on the add_review.html page
//   const currentPage = window.location.pathname;
//   if (currentPage.includes("add_review.html")) {
//     if (!isLoggedIn) {
//       // Redirect to login.html if not logged in
//       const currentUrl = encodeURIComponent(window.location.href); // Save current URL
//       alert("You must be logged in to add a review!");
//       window.location.href = `login.html?redirect=${currentUrl}`;
//     } else {
//       // User is logged in, proceed with rendering the Add Review page
//       console.log("User is logged in. Rendering Add Review page...");
//     }
//   }
// });

// document.addEventListener("DOMContentLoaded", () => {
//   const logoutButton = document.getElementById("logout-button");

//   if (logoutButton) {
//     logoutButton.addEventListener("click", (e) => {
//       e.preventDefault();

//       // Supprime les données de session
//       localStorage.removeItem("isLoggedIn");
//       localStorage.removeItem("userEmail");

//       // Redirige l'utilisateur vers la page de connexion
//       alert("You have been logged out successfully!");
//       window.location.href = "login.html";
//     });
//   }
// });

// document.addEventListener("DOMContentLoaded", () => {
//   const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";

//   if (!isLoggedIn) {
//     alert("You must be logged in to access this page!");
//     window.location.href = "login.html";
//   }
// });

// logoutButton.addEventListener("click", (e) => {
//   e.preventDefault();

//   if (confirm("Are you sure you want to log out?")) {
//     localStorage.removeItem("isLoggedIn");
//     localStorage.removeItem("userEmail");
//     alert("You have been logged out successfully!");
//     window.location.href = "login.html";
//   }
// });

// document.addEventListener("DOMContentLoaded", () => {
//   const signupForm = document.getElementById("signup-form");

//   signupForm.addEventListener("submit", (e) => {
//     e.preventDefault();

//     const email = document.getElementById("signup-email").value;
//     const password = document.getElementById("signup-password").value;

//     // Récupérer les utilisateurs existants depuis localStorage
//     let users = JSON.parse(localStorage.getItem("users")) || {};

//     // Vérifier si l'utilisateur existe déjà
//     if (users[email]) {
//       alert("This email is already registered. Please log in.");
//       return;
//     }

//     // Enregistrer le nouvel utilisateur
//     users[email] = password;
//     localStorage.setItem("users", JSON.stringify(users));

//     alert("Account created successfully! You can now log in.");
//     signupForm.reset();
//   });
// });




// document.addEventListener("DOMContentLoaded", () => {
//   const users = { "admin@hbnb.com": "admin1234" };
//   const loginForm = document.getElementById("login-form");

//   if (loginForm) {
//     loginForm.addEventListener("submit", (e) => {
//       e.preventDefault();

//       const email = document.getElementById("email").value.trim();
//       const password = document.getElementById("password").value.trim();

//       if (users[email] && users[email] === password) {
//         localStorage.setItem("isLoggedIn", "true");
//         localStorage.setItem("userEmail", email);

//         alert("Login successful!");
//         const redirectUrl = new URLSearchParams(window.location.search).get("redirect");
//         window.location.href = redirectUrl ? decodeURIComponent(redirectUrl) : "index.html";
//       } else {
//         alert("Invalid credentials. Please try again.");
//       }
//     });
//   }
// });


// document.addEventListener("DOMContentLoaded", () => {
//   const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";
//   const urlParams = new URLSearchParams(window.location.search);
//   const placeId = urlParams.get("id");

//   if (!isLoggedIn) {
//     const currentUrl = encodeURIComponent(window.location.href);
//     alert("You must be logged in to add a review!");
//     window.location.href = `login.html?redirect=${currentUrl}`;
//   }

//   // Si connecté, affiche le formulaire pour ajouter un avis
//   // (géré par handleAddReviewButton)
// });

document.addEventListener("DOMContentLoaded", () => {
  const addReviewButton = document.getElementById("add-review-button");

  // Check if the user is on the add_review.html page
  const urlParams = new URLSearchParams(window.location.search);
  const currentPage = window.location.pathname; // Get current page path
  const placeId = urlParams.get("id"); // Get the ID of the current place

  const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";
  const userEmail = localStorage.getItem("userEmail");

  // Admin credentials
  const adminEmail = "admin@hbnb.com";
  const adminPassword = "admin1234";

  if (currentPage.includes("add_review.html")) {
    // User is on the add_review.html page
    if (!isLoggedIn || userEmail !== adminEmail) {
      // Redirect to login.html if not logged in as admin
      const currentUrl = encodeURIComponent(window.location.href); // Save current URL
      alert("You must be logged in as admin to add a review!");
      window.location.href = `login.html?redirect=${currentUrl}`;
    } else {
      // Admin is logged in, proceed with rendering the Add Review page
      console.log("Admin is logged in. Rendering Add Review page...");
    }
  }

  if (addReviewButton) {
    // Add event listener for the "Add Review" button
    addReviewButton.addEventListener("click", (e) => {
      e.preventDefault();

      if (isLoggedIn && userEmail === adminEmail) {
        // Redirect to add_review.html with the place ID
        window.location.href = `add_review.html?id=${placeId}`;
      } else {
        // Redirect to login.html if not logged in as admin
        alert("You must be logged in as admin to add a review!");
        const redirectUrl = encodeURIComponent(`add_review.html?id=${placeId}`);
        window.location.href = `login.html?redirect=${redirectUrl}`;
      }
    });
  }
});

// Login logic to ensure only admin can log in
document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("login-form");

  if (loginForm) {
    loginForm.addEventListener("submit", (e) => {
      e.preventDefault();

      const email = document.getElementById("email").value.trim();
      const password = document.getElementById("password").value.trim();

      // Admin credentials
      const adminEmail = "admin@hbnb.com";
      const adminPassword = "admin1234";

      if (email === adminEmail && password === adminPassword) {
        localStorage.setItem("isLoggedIn", "true");
        localStorage.setItem("userEmail", email);

        alert("Login successful!");
        const redirectUrl = new URLSearchParams(window.location.search).get("redirect");
        window.location.href = redirectUrl ? decodeURIComponent(redirectUrl) : "index.html";
      } else {
        alert("Invalid credentials. Only admin is allowed to log in.");
      }
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const currentPage = window.location.pathname;
  const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";
  const userEmail = localStorage.getItem("userEmail");
  if (currentPage.includes("add_review.html")) {
    if (!isLoggedIn || userEmail !== "admin@hbnb.com") {
      alert("Only admin can access this page.");
      window.location.href = "login.html";
    }
  }
});
