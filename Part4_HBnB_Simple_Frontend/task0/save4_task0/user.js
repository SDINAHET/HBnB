export const users = [
  {
    email: "admin@hbnb.com",
    password: "admin1234", // Exemple uniquement, à ne pas utiliser en production
    name: "Admin User",
  },
  {
    email: "user1@hbnb.com",
    password: "password123",
    name: "John Doe",
  },
  {
    email: "user2@hbnb.com",
    password: "mypassword",
    name: "Alice Johnson",
  },
];

/**
 * Authentification d’un utilisateur
 * @param {string} email - Email de l'utilisateur.
 * @param {string} password - Mot de passe de l'utilisateur.
 * @returns {boolean} - Retourne true si l'utilisateur est authentifié, sinon false.
 */
export function authenticateUser(email, password) {
  const user = users.find((user) => user.email === email && user.password === password);
  return user ? true : false;
}

/**
 * Récupération des informations utilisateur par email.
 * @param {string} email - Email de l'utilisateur.
 * @returns {object|null} - Objet utilisateur ou null si non trouvé.
 */
export function getUserByEmail(email) {
  return users.find((user) => user.email === email) || null;
}
