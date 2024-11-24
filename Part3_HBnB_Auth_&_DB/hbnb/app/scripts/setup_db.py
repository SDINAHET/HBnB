import sqlite3
import bcrypt
from datetime import datetime

# Define the database path
DB_PATH = "app/development.db"

# SQL commands to create tables
CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    id CHAR(36) PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
"""

CREATE_PLACES_TABLE = """
CREATE TABLE IF NOT EXISTS places (
    id CHAR(36) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    owner_id CHAR(36),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE CASCADE
);
"""

CREATE_REVIEWS_TABLE = """
CREATE TABLE IF NOT EXISTS reviews (
    id CHAR(36) PRIMARY KEY,
    text TEXT NOT NULL,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    user_id CHAR(36),
    place_id CHAR(36),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (place_id) REFERENCES places(id) ON DELETE CASCADE,
    UNIQUE (user_id, place_id)
);
"""

CREATE_AMENITIES_TABLE = """
CREATE TABLE IF NOT EXISTS amenities (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
"""

CREATE_PLACE_AMENITY_TABLE = """
CREATE TABLE IF NOT EXISTS place_amenity (
    place_id CHAR(36),
    amenity_id CHAR(36),
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES places(id) ON DELETE CASCADE,
    FOREIGN KEY (amenity_id) REFERENCES amenities(id) ON DELETE CASCADE
);
"""

# Insert admin user
def insert_admin_user(connection):
    admin_id = "36c9050e-ddd3-4c3b-9731-9f487208bbc1"  # Fixed UUID for admin user
    first_name = "Admin"
    last_name = "HBnB"
    email = "admin@hbnb.io"
    plain_password = "admin1234"  # Admin password
    is_admin = True

    # Hash the password
    hashed_password = bcrypt.hashpw(plain_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    # Insert the admin user
    try:
        connection.execute(
            """
            INSERT INTO users (id, first_name, last_name, email, password, is_admin)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (admin_id, first_name, last_name, email, hashed_password, is_admin),
        )
        print("Admin user inserted successfully!")
    except sqlite3.IntegrityError:
        print("Admin user already exists!")

# Insert initial amenities
def insert_amenities(connection):
    amenities = [
        ("amenity-uuid-1", "Air Conditioning"),
        ("amenity-uuid-2", "WiFi"),
        ("amenity-uuid-3", "Swimming Pool"),
    ]

    try:
        connection.executemany(
            """
            INSERT INTO amenities (id, name) VALUES (?, ?)
            """,
            amenities,
        )
        print("Amenities inserted successfully!")
    except sqlite3.IntegrityError:
        print("Some amenities already exist!")

# Main script
def main():
    # Connect to SQLite database
    connection = sqlite3.connect(DB_PATH)
    connection.execute("PRAGMA foreign_keys = ON;")  # Enable foreign keys
    cursor = connection.cursor()

    # Create tables
    cursor.execute(CREATE_USERS_TABLE)
    cursor.execute(CREATE_PLACES_TABLE)
    cursor.execute(CREATE_REVIEWS_TABLE)
    cursor.execute(CREATE_AMENITIES_TABLE)
    cursor.execute(CREATE_PLACE_AMENITY_TABLE)

    # Insert data
    insert_admin_user(cursor)
    insert_amenities(cursor)

    # Commit changes and close the connection
    connection.commit()
    connection.close()

if __name__ == "__main__":
    main()
