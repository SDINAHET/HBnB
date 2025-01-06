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
  if (placePrice) placePrice.textContent = `${place.price}`;
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

// /**
//  * Affiche les détails d'un lieu sur la page place.html.
//  */
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
//   reviewsSection.innerHTML = ""; // Clear existing reviews
//   place.reviews.forEach((review) => {
//     const reviewDiv = document.createElement("div");
//     reviewDiv.className = "review-card";
//     reviewDiv.innerHTML = `
//       <p><strong>${review.author}:</strong> ${review.comment}</p>
//       <p>Rating: ${"★".repeat(review.rating)}${"☆".repeat(5 - review.rating)}</p>
//     `;
//     reviewsSection.appendChild(reviewDiv);
//   });

  /*Add event listener to "Add Review" button*/
  // const addReviewButton = document.getElementById("add-review-button");
  // addReviewButton.addEventListener("click", () => {
  //   const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";

  //   if (isLoggedIn) {
  //     // Redirect to add_review.html
  //     window.location.href = `add_review.html?id=${placeId}`;
  //   } else {
  //     // Redirect to login.html with redirect back to add_review.html
  //     alert("You must be logged in to add a review!");
  //     const redirectUrl = encodeURIComponent(`add_review.html?id=${placeId}`);
  //     window.location.href = `login.html?redirect=${redirectUrl}`;
  //   }
  // });


/**
 * Affiche les détails d'un lieu sur la page place.html.
 */
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
//   reviewsSection.innerHTML = ""; // Clear existing reviews
//   place.reviews.forEach((review) => {
//     const reviewDiv = document.createElement("div");
//     reviewDiv.className = "review-card";
//     reviewDiv.innerHTML = `
//       <p><strong>${review.author}:</strong> ${review.comment}</p>
//       <p>Rating: ${"★".repeat(review.rating)}${"☆".repeat(5 - review.rating)}</p>
//     `;
//     reviewsSection.appendChild(reviewDiv);
//   });

//   // Add event listener to "Add Review" button
//   const addReviewButton = document.getElementById("add-review-button");
//   addReviewButton.addEventListener("click", () => {
//     const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";

//     if (isLoggedIn) {
//       // Redirect to add_review.html
//       window.location.href = `add_review.html?id=${placeId}`;
//     } else {
//       // Redirect to login.html with redirect back to add_review.html
//       alert("You must be logged in to add a review!");
//       const redirectUrl = encodeURIComponent(`add_review.html?id=${placeId}`);
//       window.location.href = `login.html?redirect=${redirectUrl}`;
//     }
//   });
// }

// /**
//  * Initialise le formulaire pour ajouter un avis sur la page add_review.html.
//  */
// // function setupAddReviewForm(places, placeId) {
// //   const place = places.find((p) => p.id == placeId);
// //   if (!place) {
// //     document.body.innerHTML = "<h1>Place not found</h1>";
// //     return;
// //   }

// //   const reviewForm = document.getElementById("add-review-form");
// //   reviewForm.addEventListener("submit", (e) => {
// //     e.preventDefault();

// //     const reviewText = document.getElementById("review").value;
// //     const reviewRating = parseInt(document.getElementById("rating").value);

// //     place.reviews.push({
// //       author: localStorage.getItem("userEmail"),
// //       comment: reviewText,
// //       rating: reviewRating,
// //     });

// //     alert("Review added successfully!");
// //     window.location.href = `place.html?id=${placeId}`;
// //   });
// // }

/**
 * Affiche la liste des lieux sur la page index.html.
 */
// function renderPlaceList(places) {
//   const placeList = document.querySelector(".place-list");
//   const maxPriceFilter = document.getElementById("max-price");

//   if (!placeList) return;

//   function displayPlaces(filteredPlaces) {
//     placeList.innerHTML = ""; // Clear existing list

//     filteredPlaces.forEach((place) => {
//       // Create place card
//       const card = document.createElement("div");
//       card.classList.add("place-card");

//       // Add name
//       const name = document.createElement("h2");
//       name.textContent = place.name;
//       card.appendChild(name);

//       // Add price
//       const price = document.createElement("p");
//       price.textContent = `Price per night: $${place.price}`;
//       card.appendChild(price);

//       // Add View Details button
//       const detailsButton = document.createElement("button");
//       detailsButton.classList.add("details-button");
//       detailsButton.textContent = "View Details";
//       detailsButton.setAttribute("data-id", place.id);
//       detailsButton.addEventListener("click", () => {
//         window.location.href = `place.html?id=${place.id}`;
//       });
//       card.appendChild(detailsButton);

//       placeList.appendChild(card);
//     });
//   }

//   // Initial rendering
//   displayPlaces(places);

//   // Filtering by price
//   if (maxPriceFilter) {
//     maxPriceFilter.addEventListener("change", (e) => {
//       const maxPrice = e.target.value === "all" ? Infinity : parseInt(e.target.value, 10);
//       const filteredPlaces = places.filter((place) => place.price <= maxPrice);
//       displayPlaces(filteredPlaces);
//     });
//   }
// }

/**
 * Initialise le formulaire de connexion sur la page login.html.
 */
function setupLoginForm() {
  const users = { "admin@hbnb.com": "admin1234" };
  const loginForm = document.getElementById("login-form");

  if (loginForm) {
    loginForm.addEventListener("submit", (e) => {
      e.preventDefault();

      const email = document.getElementById("email").value.trim();
      const password = document.getElementById("password").value.trim();

      if (users[email] && users[email] === password) {
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
}

// /**
//  * Affiche les détails d'un lieu et gère le bouton d'ajout d'avis.
//  */
// function renderPlaceDetails(places, placeId) {
//   const place = places.find((p) => p.id == placeId);

//   if (!place) {
//     const error = document.createElement("h1");
//     error.textContent = "Place not found";
//     document.body.appendChild(error);
//     return;
//   }

//   // Populate place details
//   document.getElementById("place-title").textContent = place.name;
//   document.getElementById("place-host").textContent = place.host;
//   document.getElementById("place-price").textContent = `${place.price}`;
//   document.getElementById("place-description").textContent = place.description;
//   document.getElementById("place-amenities").textContent = place.amenities;

//   // Display reviews
//   const reviewsSection = document.getElementById("reviews-section");
//   reviewsSection.innerHTML = ""; // Clear existing reviews

//   place.reviews.forEach((review) => {
//     const reviewDiv = document.createElement("div");
//     reviewDiv.classList.add("review-card");

//     const author = document.createElement("p");
//     author.textContent = `Author: ${review.author}`;
//     reviewDiv.appendChild(author);

//     const comment = document.createElement("p");
//     comment.textContent = `Comment: ${review.comment}`;
//     reviewDiv.appendChild(comment);

//     const rating = document.createElement("p");
//     rating.textContent = `Rating: ${"★".repeat(review.rating)}${"☆".repeat(5 - review.rating)}`;
//     reviewDiv.appendChild(rating);

//     reviewsSection.appendChild(reviewDiv);
//   });

//   // Add Review Button
//   const addReviewButton = document.getElementById("add-review-button");
//   addReviewButton.addEventListener("click", () => {
//     const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";

//     if (isLoggedIn) {
//       window.location.href = `add_review.html?id=${placeId}`;
//     } else {
//       alert("You must be logged in to add a review!");
//       const redirectUrl = encodeURIComponent(`add_review.html?id=${placeId}`);
//       window.location.href = `login.html?redirect=${redirectUrl}`;
//     }
//   });
// }

// /**
//  * Affiche les détails d'un lieu et gère le bouton d'ajout d'avis.
//  */
// function renderPlaceDetails(places, placeId) {
//   const place = places.find((p) => p.id == placeId);

//   if (!place) {
//     const error = document.createElement("h1");
//     error.textContent = "Place not found";
//     document.body.appendChild(error);
//     return;
//   }

//   // Populate place details
//   document.getElementById("place-title").textContent = place.name;
//   document.getElementById("place-host").textContent = place.host;
//   document.getElementById("place-price").textContent = `$${place.price}`;
//   document.getElementById("place-description").textContent = place.description;
//   document.getElementById("place-amenities").textContent = place.amenities;

//   // Display reviews
//   const reviewsSection = document.getElementById("reviews-section");
//   reviewsSection.innerHTML = ""; // Clear existing reviews

//   place.reviews.forEach((review) => {
//     const reviewDiv = document.createElement("div");
//     reviewDiv.classList.add("review-card");

//     const author = document.createElement("p");
//     author.textContent = `Author: ${review.author}`;
//     reviewDiv.appendChild(author);

//     const comment = document.createElement("p");
//     comment.textContent = `Comment: ${review.comment}`;
//     reviewDiv.appendChild(comment);

//     const rating = document.createElement("p");
//     rating.textContent = `Rating: ${"★".repeat(review.rating)}${"☆".repeat(5 - review.rating)}`;
//     reviewDiv.appendChild(rating);

//     reviewsSection.appendChild(reviewDiv);
//   });

/**
 * Handles the logout functionality.
 */
function setupLogoutButton() {
  const logoutButton = document.getElementById("logout-button");

  if (logoutButton) {
    logoutButton.addEventListener("click", () => {
      // Clear the user's session data
      localStorage.removeItem("isLoggedIn");
      localStorage.removeItem("userEmail");

      // Notify the user
      alert("You have been logged out!");

      // Redirect to the login page
      window.location.href = "login.html";
    });
  }
}

// Ensure the logout button is functional when the DOM is loaded
document.addEventListener("DOMContentLoaded", setupLogoutButton);

function setupLoginForm() {
  console.log("Login form setup initialized.");
  const loginForm = document.getElementById("login-form");
  if (!loginForm) {
    console.error("Login form not found!");
    return;
  }

  loginForm.addEventListener("submit", (e) => {
    e.preventDefault();
    console.log("Login form submitted.");

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();
    console.log(`Email: ${email}, Password: ${password}`);

    if (email === "admin@hbnb.com" && password === "admin1234") {
      console.log("Login successful.");
      localStorage.setItem("isLoggedIn", "true");
      localStorage.setItem("userEmail", email);

      alert("Login successful!");
      const redirectUrl = new URLSearchParams(window.location.search).get("redirect");
      window.location.href = redirectUrl ? decodeURIComponent(redirectUrl) : "index.html";
    } else {
      console.log("Invalid login credentials.");
      alert("Invalid email or password. Please try again.");
    }
  });
}

/**
 * Initialise le bouton "Add Review" sur la page place.html.
 */
// function setupAddReviewButton(placeId) {
//   const addReviewButton = document.getElementById("add-review-button");

//   if (!addReviewButton) {
//     console.error("Add Review button not found!");
//     return;
//   }

//   addReviewButton.addEventListener("click", () => {
//     // Vérifie si l'utilisateur est connecté
//     const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";
//     if (!isLoggedIn) {
//       // Redirection vers login.html avec une redirection prévue après connexion
//       const redirectUrl = encodeURIComponent(`add_review.html?id=${placeId}`);
//       alert("You must be logged in to add a review!");
//       window.location.href = `login.html?redirect=${redirectUrl}`;
//     } else {
//       // Redirection vers la page d'ajout de review
//       window.location.href = `add_review.html?id=${placeId}`;
//     }
//   });
// }

// function checkLoginForAddReview() {
//   const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";
//   if (!isLoggedIn) {
//     alert("You must be logged in to add a review!");
//     window.location.href = "login.html";
//   }
// }

/**
 * Configure le bouton "Add Review" sur la page place.html.
 * Si l'utilisateur est connecté, redirige vers add_review.html.
 * Sinon, redirige vers login.html.
 */
// function setupAddReviewButton(placeId) {
//   const addReviewButton = document.getElementById("add-review-button");

//   if (!addReviewButton) {
//     console.error("Add Review button not found!");
//     return;
//   }

//   addReviewButton.addEventListener("click", () => {
//     const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";
//     if (!isLoggedIn) {
//       // Redirige vers la page de connexion avec une redirection prévue après
//       const redirectUrl = encodeURIComponent(`add_review.html?id=${placeId}`);
//       alert("You must be logged in to add a review!");
//       window.location.href = `login.html?redirect=${redirectUrl}`;
//     } else {
//       // Redirige directement vers la page d'ajout d'avis
//       window.location.href = `add_review.html?id=${placeId}`;
//     }
//   });
// }

// document.addEventListener("DOMContentLoaded", () => {
//   const addReviewButton = document.getElementById("add-review-button");

//   if (addReviewButton) {
//     addReviewButton.addEventListener("click", () => {
//       const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";

//       if (isLoggedIn) {
//         // Redirection vers add_review.html avec placeId
//         const placeId = new URLSearchParams(window.location.search).get("id");
//         window.location.href = `add_review.html?id=${placeId}`;
//       } else {
//         // Redirection vers login.html avec redirection prévue
//         alert("You must be logged in to add a review!");
//         const redirectUrl = encodeURIComponent(`add_review.html?id=${placeId}`);
//         window.location.href = `login.html?redirect=${redirectUrl}`;
//       }
//     });
//   }
// });

// Mise à jour du gestionnaire "Add Review" pour correspondre à l'URL correcte
document.addEventListener("DOMContentLoaded", () => {
  const addReviewButton = document.getElementById("add-review-button");

  if (addReviewButton) {
      addReviewButton.addEventListener("click", () => {
          const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";

          if (isLoggedIn) {
              // Redirige vers add-review.html avec placeId
              const placeId = new URLSearchParams(window.location.search).get("id");
              window.location.href = `add-review.html?id=${placeId}`;
          } else {
              // Redirige vers login.html avec une redirection prévue
              alert("You must be logged in to add a review!");
              const redirectUrl = encodeURIComponent(`add-review.html?id=${placeId}`);
              window.location.href = `login.html?redirect=${redirectUrl}`;
          }
      });
  }
});


function renderPlaceList(places) {
  const placeList = document.querySelector(".place-list");

  if (!placeList) return;

  // Efface la liste existante
  placeList.innerHTML = "";

  // Ajoute les cartes de lieu
  places.forEach((place) => {
    const card = document.createElement("div");
    card.className = "place-card";
    card.innerHTML = `
      <h2>${place.name}</h2>
      <p>Price per night: $${place.price}</p>
      <button class="details-btn" data-id="${place.id}">View Details</button>
    `;
    placeList.appendChild(card);
  });

  // Ajoute les gestionnaires d'événements pour chaque bouton "View Details"
  document.querySelectorAll(".details-btn").forEach((button) => {
    button.addEventListener("click", (e) => {
      const placeId = e.target.getAttribute("data-id");
      window.location.href = `place.html?id=${placeId}`;
    });
  });
}
