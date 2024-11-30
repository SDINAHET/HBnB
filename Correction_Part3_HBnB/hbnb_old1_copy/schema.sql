PRAGMA foreign_keys = ON;

-- Create User table
CREATE TABLE users (
    id CHAR(36) PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create Place table
CREATE TABLE places (
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

-- Create Review table
CREATE TABLE reviews (
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

-- Create Amenity table
CREATE TABLE amenities (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP

);

-- Create Place_Amenity association table
CREATE TABLE place_amenity (
    place_id CHAR(36),
    amenity_id CHAR(36),
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES places(id) ON DELETE CASCADE,
    FOREIGN KEY (amenity_id) REFERENCES amenities(id) ON DELETE CASCADE
);

-- Insert admin user
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1', -- fix const UUID prédéfini
    'Admin',
    'HBnB',
    'admin@hbnb.io',
    ---'hashed_admin1234',  -- Replace with the hashed password
    -- '$2b$12$WZqhkmHErIMTl7YKJ/RdfXEbrNKg9XyFo7Csh5RgN5tQ8qGHyjfD2', -- bcrypt hash of 'admin1234'
    '$2a$12$ivDzHW.L7rqFI4ymAdVBbOswoVX4zsrfE1B1a5mnW.Yxt6e7ZKYoW', -- bcrypt2 hash of 'admin1234'
    TRUE
);

INSERT INTO amenities (id, name) VALUES ('a12ef460-8e90-4e7a-8f43-1918a006078d', 'WiFi');
INSERT INTO amenities (id, name) VALUES ('acbc951d-ef60-4486-84b9-87afc47d1eb2', 'Swimming Pool');
INSERT INTO amenities (id, name) VALUES ('6fac204d-90b6-40cc-a87a-dbbc0814745e', 'Air Conditioning');
