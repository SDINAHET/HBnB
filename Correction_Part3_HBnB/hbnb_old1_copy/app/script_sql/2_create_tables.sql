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



-- -- Create User table
-- CREATE TABLE users (
--     id CHAR(36) PRIMARY KEY,
--     first_name VARCHAR(255),
--     last_name VARCHAR(255),
--     email VARCHAR(255) UNIQUE NOT NULL,
--     password VARCHAR(255) NOT NULL,
--     is_admin BOOLEAN DEFAULT FALSE
-- );

-- -- Create Place table
-- CREATE TABLE places (
--     id CHAR(36) PRIMARY KEY,
--     title VARCHAR(255) NOT NULL,
--     description TEXT,
--     price DECIMAL(10, 2) NOT NULL,
--     latitude FLOAT NOT NULL,
--     longitude FLOAT NOT NULL,
--     owner_id CHAR(36),
--     FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE CASCADE
-- );

-- -- Create Review table
-- CREATE TABLE reviews (
--     id CHAR(36) PRIMARY KEY,
--     text TEXT NOT NULL,
--     rating INT CHECK (rating BETWEEN 1 AND 5),
--     user_id CHAR(36),
--     place_id CHAR(36),
--     FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
--     FOREIGN KEY (place_id) REFERENCES places(id) ON DELETE CASCADE,
--     UNIQUE (user_id, place_id)
-- );

-- -- Create Amenity table
-- CREATE TABLE amenities (
--     id CHAR(36) PRIMARY KEY,
--     name VARCHAR(255) UNIQUE NOT NULL
-- );

-- -- Create Place_Amenity association table
-- CREATE TABLE place_amenity (
--     place_id CHAR(36),
--     amenity_id CHAR(36),
--     PRIMARY KEY (place_id, amenity_id),
--     FOREIGN KEY (place_id) REFERENCES places(id) ON DELETE CASCADE,
--     FOREIGN KEY (amenity_id) REFERENCES amenities(id) ON DELETE CASCADE
-- );
