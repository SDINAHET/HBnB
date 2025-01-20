document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');
  const errorMessage = document.getElementById('error-message');
  const successMessage = document.getElementById('success-message');

  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const email = document.getElementById('email').value.trim();
      const password = document.getElementById('password').value.trim();

      try {
        // Appel à la fonction loginUser pour effectuer la requête
        const data = await loginUser(email, password);

        if (data) {
          // Masquer le message d'erreur en cas de succès
          errorMessage.style.display = 'none';

          // Stocker le token et l'ID utilisateur dans les cookies
          document.cookie = `token=${data.access_token}; path=/;`;
          document.cookie = `user_id=${data.user_id}; path=/;`;

          // Afficher un message de succès avec le token et l'ID utilisateur
          successMessage.style.display = 'block';
          successMessage.textContent = `Login successful! Token: ${data.access_token}, User ID: ${data.user_id}, 20 seconds before next page`;

          // Exemple : Récupérer des données protégées après connexion
          const token = getCookie("token");
          try {
            const response = await fetch("http://127.0.0.1:5000/api/v1/protected/protected", {
              method: "GET",
              headers: {
                "Authorization": `Bearer ${token}`,
                "Accept": "application/json",
              },
            });

            if (response.ok) {
              const protectedData = await response.json();
              console.log("Protected data:", protectedData);
              successMessage.textContent += `\nProtected data fetched: ${JSON.stringify(protectedData)}`;
            } else {
              console.error("Failed to fetch protected data:", response.statusText);
            }
          } catch (error) {
            console.error("Error fetching protected data:", error);
          }

          // Rediriger après 20 secondes
          setTimeout(() => {
            window.location.href = 'index.html';
          }, 20000);
        }
      } catch (error) {
        // Afficher un message d'erreur en cas de problème
        console.error('Error during login:', error);
        errorMessage.style.display = 'block';
        errorMessage.textContent = 'An error occurred. Please try again later.';
      }
    });
  }
});

// Fonction pour effectuer la requête d'authentification
async function loginUser(email, password) {
  const response = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ email, password }),
  });

  if (response.ok) {
    const data = await response.json();
    return data; // Retourne les données (token et user_id) en cas de succès
  } else {
    const error = await response.json();
    throw new Error(error.message || 'Login failed'); // Lève une erreur pour la gérer dans le bloc try-catch
  }
}

// Fonction utilitaire pour récupérer un cookie
function getCookie(name) {
  const cookies = document.cookie.split("; ");
  for (let cookie of cookies) {
    const [key, value] = cookie.split("=");
    if (key === name) return value;
  }
  return null;
}
