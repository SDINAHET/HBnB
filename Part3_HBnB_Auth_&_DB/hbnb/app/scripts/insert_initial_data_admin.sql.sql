-- Insert admin user
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1', -- fix const
    'Admin',
    'HBnB',
    'admin@hbnb.io',
    ---'hashed_admin1234',  -- Replace with the hashed password
    '$2b$12$WZqhkmHErIMTl7YKJ/RdfXEbrNKg9XyFo7Csh5RgN5tQ8qGHyjfD2', -- bcrypt hash of 'admin1234'
    TRUE
);

-- Insert initial amenities
INSERT INTO amenities (id, name) VALUES (UUID(), 'WiFi');
INSERT INTO amenities (id, name) VALUES (UUID(), 'Swimming Pool');
INSERT INTO amenities (id, name) VALUES (UUID(), 'Air Conditioning');

-- from bcrypt import hashpw, gensalt
-- print(hashpw(b"admin1234", gensalt()).decode())
