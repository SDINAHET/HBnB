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


-- INSERT INTO amenities (id, name) VALUES ('amenity-uuid-1', 'WiFi');
-- INSERT INTO amenities (id, name) VALUES ('amenity-uuid-2', 'Swimming Pool');
-- INSERT INTO amenities (id, name) VALUES ('amenity-uuid-3', 'Air Conditioning');

-- Insert initial amenities
-- INSERT INTO amenities (id, name) VALUES (UUID(), 'WiFi');
-- INSERT INTO amenities (id, name) VALUES (UUID(), 'Swimming Pool');
-- INSERT INTO amenities (id, name) VALUES (UUID(), 'Air Conditioning');

-- from bcrypt import hashpw, gensalt
-- print(hashpw(b"admin1234", gensalt()).decode())
