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
      reviews: [{ author: "Emma Wilson", comment: "So cozy and quiet!", rating: 5 }],
    },
    {
      id: 3,
      name: "Modern Apartment",
      host: "Chris Lee",
      price: 200,
      description: "A sleek and stylish city apartment with modern amenities.",
      amenities: "Smart TV, High-Speed WiFi, Gym Access",
      reviews: [{ author: "Liam Martinez", comment: "Perfect for business travel.", rating: 4 }],
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

  /**
   * Affiche la liste des lieux dans le DOM.
   * @param {Array} data - Liste des lieux à afficher.
   */
  function renderPlaceList(data) {
    const placeListEl = document.querySelector(".place-list");
    if (!placeListEl) return;

    // Vider les anciens éléments
    placeListEl.innerHTML = "";

    // Créer une carte pour chaque lieu
    data.forEach((place) => {
      const card = document.createElement("div");
      card.className = "place-card";
      card.innerHTML = `
        <h2>${place.name}</h2>
        <p>Price per night: $${place.price}</p>
        <button class="details-btn" data-id="${place.id}">View Details</button>
      `;
      placeListEl.appendChild(card);
    });

    // Ajouter des événements aux boutons "View Details"
    document.querySelectorAll(".details-btn").forEach((btn) => {
      btn.addEventListener("click", (e) => {
        const pid = e.target.getAttribute("data-id");
        window.location.href = `place.html?id=${pid}`;
      });
    });
  }

  /**
   * Configure le filtre "Max Price".
   */
  function setupMaxPriceFilter() {
    const maxPriceSelect = document.getElementById("maxPrice");
    if (!maxPriceSelect) return;

    // Filtrer les lieux lorsqu'une option est sélectionnée
    maxPriceSelect.addEventListener("change", () => {
      const value = maxPriceSelect.value; // Ex: "100" ou "all"
      const maxPrice = value === "all" ? Infinity : parseInt(value, 10);

      // Filtrer les lieux en fonction du prix
      const filteredPlaces = places.filter((place) => place.price <= maxPrice);

      // Réafficher les lieux filtrés
      renderPlaceList(filteredPlaces);
    });
  }

  // Initialisation
  renderPlaceList(places); // Affiche tous les lieux au départ
  setupMaxPriceFilter();   // Active le filtrage par prix
});
