import sqlite3
import bcrypt
import uuid

# Define the database path
DB_PATH = "app/development.db"

# Function to generate a UUID4
def generate_uuid():
    return str(uuid.uuid4())

# Insert the admin user
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
        (generate_uuid(), "WiFi"),
        (generate_uuid(), "Swimming Pool"),
        (generate_uuid(), "Air Conditioning"),
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

    # Insert data
    insert_admin_user(cursor)
    insert_amenities(cursor)

    # Commit changes and close the connection
    connection.commit()
    connection.close()

if __name__ == "__main__":
    main()
