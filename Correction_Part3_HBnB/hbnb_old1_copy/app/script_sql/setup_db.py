import sqlite3
import os

# Chemin vers la base de données (dans le dossier instance)
DB_PATH = os.path.join("instance", "development.db")

# Script SQL à exécuter
SQL_SCRIPT = """
# <Insérez le script SQL ici>
-- Activer les clés étrangères
PRAGMA foreign_keys = ON;

-- Créer la table `users`
CREATE TABLE IF NOT EXISTS users (
    id CHAR(36) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Créer la table `places`
CREATE TABLE IF NOT EXISTS places (
    id CHAR(36) PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    latitude FLOAT NOT NULL CHECK (latitude BETWEEN -90.0 AND 90.0),
    longitude FLOAT NOT NULL CHECK (longitude BETWEEN -180.0 AND 180.0),
    owner_id CHAR(36) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Créer la table `reviews`
CREATE TABLE IF NOT EXISTS reviews (
    id CHAR(36) PRIMARY KEY,
    text TEXT NOT NULL,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    user_id CHAR(36) NOT NULL,
    place_id CHAR(36) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (place_id) REFERENCES places(id) ON DELETE CASCADE,
    UNIQUE (user_id, place_id)
);

-- Créer la table `amenities`
CREATE TABLE IF NOT EXISTS amenities (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Créer la table `place_amenity` (association many-to-many)
CREATE TABLE IF NOT EXISTS place_amenity (
    place_id CHAR(36) NOT NULL,
    amenity_id CHAR(36) NOT NULL,
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES places(id) ON DELETE CASCADE,
    FOREIGN KEY (amenity_id) REFERENCES amenities(id) ON DELETE CASCADE
);

-- Insérer l'utilisateur administrateur
INSERT OR IGNORE INTO users (id, first_name, last_name, email, password, is_admin)
VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1',  -- UUID prédéfini
    'Admin',
    'HBnB',
    'admin@hbnb.io',
    '$2a$12$ivDzHW.L7rqFI4ymAdVBbOswoVX4zsrfE1B1a5mnW.Yxt6e7ZKYoW',  -- bcrypt hash de 'admin1234'
    TRUE
);

-- Insérer des données initiales dans la table `amenities`
INSERT OR IGNORE INTO amenities (id, name) VALUES
('a12ef460-8e90-4e7a-8f43-1918a006078d', 'WiFi'),
('acbc951d-ef60-4486-84b9-87afc47d1eb2', 'Swimming Pool'),
('6fac204d-90b6-40cc-a87a-dbbc0814745e', 'Air Conditioning');

"""

def initialize_database():
    # Créer une connexion SQLite
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        # Exécuter le script SQL
        cursor.executescript(SQL_SCRIPT)
        conn.commit()
        print("Base de données initialisée avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'initialisation de la base : {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    initialize_database()
