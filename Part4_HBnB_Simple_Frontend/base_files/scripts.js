/*
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener("DOMContentLoaded", () => {
  /* DO SOMETHING */
// });
  // Redirection des boutons "View Details"
  const detailButtons = document.querySelectorAll(".details-btn");
  detailButtons.forEach((button) => {
    button.addEventListener("click", () => {
      window.location.href = "place.html"; // Rediriger vers place.html
    });
  });

  // Filtrage des places par prix
  const maxPriceFilter = document.getElementById("max-price");
  const placeCards = document.querySelectorAll(".place-card");

  maxPriceFilter.addEventListener("change", (e) => {
    const maxPrice = e.target.value === "all" ? Infinity : parseInt(e.target.value);

    placeCards.forEach((card) => {
      const priceText = card.querySelector("p").textContent;
      const price = parseInt(priceText.match(/\$([0-9]+)/)[1]);

      card.style.display = price <= maxPrice ? "block" : "none";
    });
  });
});

document.getElementById("login-form").addEventListener("submit", (e) => {
  e.preventDefault();
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  console.log("Email:", email);
  console.log("Password:", password);

  // Remplacez par une requête à votre API pour authentifier l'utilisateur
  alert("Login successful (logic to be implemented)");
});
