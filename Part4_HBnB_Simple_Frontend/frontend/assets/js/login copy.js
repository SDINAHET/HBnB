      // Add an event listener for the form submission:
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
                successMessage.textContent = `Login successful! Token: ${data.access_token}, User ID: ${data.user_id}, 20seconde before next page`;

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

      // Fonction pour effectuer la requête d'authentification Make the AJAX request to the API:
      async function loginUser(email, password) {
        const response = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ email, password }),
        });

        // Check if the request was successful / Handle the API response and store the token in a cookie:
        if (response.ok) {
          const data = await response.json();
          return data; // Retourne les données (token et user_id) en cas de succès
        } else {
          const error = await response.json();
          throw new Error(error.message || 'Login failed'); // Lève une erreur pour la gérer dans le bloc try-catch
        }
      }
