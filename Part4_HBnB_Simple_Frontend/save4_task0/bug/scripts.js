// Ensure the DOM is fully loaded
window.addEventListener('DOMContentLoaded', () => {
  const places = fetchPlaces(); // Fetch places data
  const isLoggedIn = checkUserLogin(); // Check if user is logged in

  if (window.location.pathname.includes('index.html')) {
    displayPlaces(places); // Display list of places
  } else if (window.location.pathname.includes('place.html')) {
    displayPlaceDetails(places, isLoggedIn); // Display place details
  }
});

// Function to fetch place data
function fetchPlaces() {
  return [
    {
      id: 1,
      name: "Beautiful Beach House",
      host: "John Doe",
      pricePerNight: 150,
      description: "A beautiful beach house with amazing views...",
      amenities: ["WiFi", "Pool", "Air Conditioning"],
      reviews: [
        { userName: "Jane Smith", comment: "Great place to stay!", rating: 4 },
        { userName: "Robert Brown", comment: "Amazing location and very comfortable.", rating: 5 },
      ],
    },
    {
      id: 2,
      name: "Cozy Cabin",
      host: "Alice Johnson",
      pricePerNight: 100,
      description: "A warm and inviting cabin in the woods.",
      amenities: ["Fireplace", "Hiking Trails", "Mountain View"],
      reviews: [
        { userName: "Emma Wilson", comment: "So cozy and quiet!", rating: 5 },
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
}

// Function to check if the user is logged in
function checkUserLogin() {
  return localStorage.getItem('userToken') !== null;
}

// Display places on index.html
function displayPlaces(places) {
  const placeContainer = document.querySelector('.place-card-container'); // Container for all place cards

  if (!places || places.length === 0) {
    const noPlacesMessage = document.createElement('p');
    noPlacesMessage.textContent = 'No places available.';
    placeContainer.appendChild(noPlacesMessage);
    return;
  }

  places.forEach((place) => {
    const placeCard = document.createElement('div');
    placeCard.classList.add('place-card');

    const name = document.createElement('h3');
    name.textContent = place.name;

    const price = document.createElement('p');
    price.textContent = `Price per night: $${place.pricePerNight}`;

    const button = document.createElement('button');
    button.classList.add('details-button');
    button.textContent = 'View Details';
    button.addEventListener('click', () => viewPlaceDetails(place.id));

    placeCard.appendChild(name);
    placeCard.appendChild(price);
    placeCard.appendChild(button);

    placeContainer.appendChild(placeCard);
  });
}

// Navigate to the place details page
function viewPlaceDetails(placeId) {
  window.location.href = `place.html?id=${placeId}`;
}

// Display place details on place.html
function displayPlaceDetails(places, isLoggedIn) {
  const placeId = parseInt(new URLSearchParams(window.location.search).get('id'));
  const place = places.find((p) => p.id === placeId);
  const detailsContainer = document.querySelector('#details-container');

  if (!place) {
    const errorMessage = document.createElement('p');
    errorMessage.textContent = 'Place not found.';
    detailsContainer.appendChild(errorMessage);
    return;
  }

  const detailsSection = document.createElement('div');
  detailsSection.classList.add('place-details');

  const name = document.createElement('h2');
  name.textContent = place.name;

  const host = document.createElement('p');
  host.textContent = `Host: ${place.host}`;

  const price = document.createElement('p');
  price.textContent = `Price per night: $${place.pricePerNight}`;

  const description = document.createElement('p');
  description.textContent = `Description: ${place.description}`;

  const amenitiesContainer = document.createElement('div');
  amenitiesContainer.classList.add('place-info');
  const amenitiesTitle = document.createElement('h3');
  amenitiesTitle.textContent = 'Amenities';

  const amenitiesList = document.createElement('ul');
  place.amenities.forEach((amenity) => {
    const listItem = document.createElement('li');
    listItem.textContent = amenity;
    amenitiesList.appendChild(listItem);
  });

  amenitiesContainer.appendChild(amenitiesTitle);
  amenitiesContainer.appendChild(amenitiesList);

  detailsSection.appendChild(name);
  detailsSection.appendChild(host);
  detailsSection.appendChild(price);
  detailsSection.appendChild(description);
  detailsSection.appendChild(amenitiesContainer);

  detailsContainer.appendChild(detailsSection);

  if (place.reviews && place.reviews.length > 0) {
    const reviewSection = document.createElement('div');
    reviewSection.classList.add('review-section');

    const reviewTitle = document.createElement('h3');
    reviewTitle.textContent = 'Reviews';
    reviewSection.appendChild(reviewTitle);

    place.reviews.forEach((review) => {
      const reviewCard = document.createElement('div');
      reviewCard.classList.add('review-card');

      const comment = document.createElement('p');
      comment.textContent = `${review.userName}: ${review.comment}`;

      const rating = document.createElement('p');
      rating.textContent = `Rating: ${review.rating}/5`;

      reviewCard.appendChild(comment);
      reviewCard.appendChild(rating);

      reviewSection.appendChild(reviewCard);
    });

    detailsContainer.appendChild(reviewSection);
  }

  if (isLoggedIn) {
    const addReviewSection = document.createElement('div');
    addReviewSection.classList.add('add-review');

    const formTitle = document.createElement('h3');
    formTitle.textContent = 'Add a Review';

    const form = document.createElement('form');
    form.classList.add('form');
    form.onsubmit = (event) => submitReview(event, place.id);

    const textarea = document.createElement('textarea');
    textarea.name = 'comment';
    textarea.placeholder = 'Write your comment here';
    textarea.required = true;

    const ratingInput = document.createElement('input');
    ratingInput.type = 'number';
    ratingInput.name = 'rating';
    ratingInput.min = '1';
    ratingInput.max = '5';
    ratingInput.placeholder = 'Rating (1-5)';
    ratingInput.required = true;

    const submitButton = document.createElement('button');
    submitButton.type = 'submit';
    submitButton.textContent = 'Submit';

    form.appendChild(textarea);
    form.appendChild(ratingInput);
    form.appendChild(submitButton);

    addReviewSection.appendChild(formTitle);
    addReviewSection.appendChild(form);

    detailsContainer.appendChild(addReviewSection);
  } else {
    const loginButton = document.createElement('button');
    loginButton.textContent = 'Login to Add a Review';
    loginButton.addEventListener('click', () => {
      window.location.href = 'login.html';
    });

    detailsContainer.appendChild(loginButton);
  }
}

// Handle review submission
function submitReview(event, placeId) {
  event.preventDefault();

  const form = event.target;
  const comment = form.comment.value.trim();
  const rating = parseInt(form.rating.value);

  if (comment && rating >= 1 && rating <= 5) {
    alert('Review submitted successfully!');
    form.reset();
  } else {
    alert('Please provide a valid comment and rating.');
  }
}
