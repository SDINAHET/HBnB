document.addEventListener("DOMContentLoaded", async () => {
  const placeId = getPlaceIdFromURL();
  if (!placeId) {
    alert("Invalid Place ID!");
    window.location.href = "index.html";
    return;
  }

  const token = getCookie("token");
  checkAuthentication(token);

  try {
    const place = await fetchPlaceDetails(placeId, token);
    displayPlaceDetails(place);

    if (token) {
      setupAddReviewForm(placeId, token);
    } else {
      displayLoginForReview();
    }
  } catch (error) {
    console.error("Error loading place details:", error);
    document.querySelector(".place-details").innerHTML =
      "<p>Failed to load place details. Please try again later.</p>";
  }
});

function getPlaceIdFromURL() {
  const params = new URLSearchParams(window.location.search);
  return params.get("id");
}

function checkAuthentication(token) {
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

function getCookie(name) {
  const cookies = document.cookie.split("; ");
  for (let cookie of cookies) {
    const [key, value] = cookie.split("=");
    if (key === name) return value;
  }
  return null;
}

async function fetchPlaceDetails(placeId, token) {
  const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      ...(token && { Authorization: `Bearer ${token}` }),
    },
  });
  if (!response.ok) {
    throw new Error("Failed to fetch place details");
  }
  return await response.json();
}

function displayPlaceDetails(place) {
  document.getElementById("place-title").textContent = place.title;
  document.getElementById("place-host").textContent =
    place.owner?.first_name + " " + place.owner?.last_name || "Unknown";
  document.getElementById("place-price").textContent = `${place.price}€`;
  document.getElementById("place-description").textContent = place.description;
  document.getElementById("place-amenities").textContent =
    place.amenities?.map((amenity) => amenity.name).join(", ") || "None";

  const reviewsSection = document.getElementById("reviews-section");
  reviewsSection.innerHTML = "";
  if (!place.reviews?.length) {
    reviewsSection.innerHTML = "<p>No reviews yet.</p>";
  } else {
    place.reviews.forEach((review) => {
      const reviewDiv = document.createElement("div");
      reviewDiv.className = "review";
      reviewDiv.innerHTML = `
        <p><strong>${review.user_id}:</strong></p>
        <p>${review.text}</p>
        <p>Rating: ${"★".repeat(review.rating)}${"☆".repeat(
        5 - review.rating
      )}</p>
      `;
      reviewsSection.appendChild(reviewDiv);
    });
  }
}

function setupAddReviewForm(placeId, token) {
  const addReviewContainer = document.getElementById("add-review-container");
  const addReviewForm = document.createElement("form");
  addReviewForm.id = "add-review-form";
  addReviewForm.innerHTML = `
    <h2>Add a Review</h2>
    <textarea id="review-text" placeholder="Write your review..." required></textarea>
    <label for="review-rating">Rating:</label>
    <select id="review-rating" required>
      <option value="1">1</option>
      <option value="2">2</option>
      <option value="3">3</option>
      <option value="4">4</option>
      <option value="5">5</option>
    </select>
    <button type="submit">Submit Review</button>
  `;

  addReviewForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const text = document.getElementById("review-text").value.trim();
    const rating = parseInt(document.getElementById("review-rating").value, 10);

    try {
      const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}/reviews`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ text, rating }),
      });

      if (!response.ok) {
        throw new Error("Failed to submit review");
      }

      alert("Review submitted!");
      location.reload();
    } catch (error) {
      console.error("Error submitting review:", error);
    }
  });

  addReviewContainer.appendChild(addReviewForm);
}

function displayLoginForReview() {
  const addReviewContainer = document.getElementById("add-review-container");
  const loginButton = document.createElement("button");
  loginButton.textContent = "Login to Add Review";
  loginButton.addEventListener("click", () => {
    const redirectUrl = encodeURIComponent(window.location.href);
    window.location.href = `login.html?redirect=${redirectUrl}`;
  });
  addReviewContainer.appendChild(loginButton);
}
