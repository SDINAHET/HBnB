-- Insert admin user
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
    'Admin',
    'HBnB',
    'admin@hbnb.io',
    'hashed_admin1234',  -- Replace with the hashed password
    TRUE
);

-- Insert initial amenities
INSERT INTO amenities (id, name) VALUES (UUID(), 'WiFi');
INSERT INTO amenities (id, name) VALUES (UUID(), 'Swimming Pool');
INSERT INTO amenities (id, name) VALUES (UUID(), 'Air Conditioning');
