-- Table Users
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES
    ('1b6ef38c-88cb-4bcf-9d0f-b70e39eb70a8', 'John', 'Doe', 'john.doe@hbnb.io', '$2a$12$E4jG5Vzq4DSO0jN0v7q/.SPyIYrX1d5Y3u2g/Emy4wOvlLglSKai6', FALSE),
    ('2a6fcbae-5bcf-48c8-b6b1-94d95dbf60b6', 'Alice', 'Johnson', 'alice.johnson@hbnb.io', '$2a$12$E4jG5Vzq4DSO0jN0v7q/.SPyIYrX1d5Y3u2g/Emy4wOvlLglSKai6', FALSE),
    ('8bf65c58-7af4-49a4-a438-f28b8949cb84', 'Chris', 'Lee', 'chris.lee@hbnb.io', '$2a$12$E4jG5Vzq4DSO0jN0v7q/.SPyIYrX1d5Y3u2g/Emy4wOvlLglSKai6', FALSE),
    ('5dcb4dc8-b218-4f1e-822d-6f29b4e5a2cf', 'Laura', 'White', 'laura.white@hbnb.io', '$2a$12$E4jG5Vzq4DSO0jN0v7q/.SPyIYrX1d5Y3u2g/Emy4wOvlLglSKai6', FALSE),
    ('3b8bcdc2-4910-4b7f-a3b5-e9b1a5c6b9c4', 'David', 'Beckham', 'david.beckham@hbnb.io', '$2a$12$E4jG5Vzq4DSO0jN0v7q/.SPyIYrX1d5Y3u2g/Emy4wOvlLglSKai6', FALSE);

-- Table Places
INSERT INTO places (id, title, description, price, latitude, longitude, owner_id)
VALUES
    ('765a38e6-c131-4315-8e9c-28ac88424634', 'Beautiful Beach House', 'A beautiful beach house with amazing views...', 150, 34.052235, -118.243683, '1b6ef38c-88cb-4bcf-9d0f-b70e39eb70a8'),
    ('5c66b5f9-74a7-4767-8f5b-7d2b153b6057', 'Cozy Cabin', 'A warm and inviting cabin in the woods.', 100, 37.774929, -122.419416, '2a6fcbae-5bcf-48c8-b6b1-94d95dbf60b6'),
    ('3f477fd8-fc69-47f1-8c22-12dc4db86099', 'Modern Apartment', 'A sleek and stylish city apartment with modern amenities.', 200, 40.712776, -74.005974, '8bf65c58-7af4-49a4-a438-f28b8949cb84'),
    ('13e66193-3e0b-493d-bca2-94252343a5e3', 'Rustic Lakehouse', 'A charming lakehouse with a beautiful view of the sunset.', 180, 44.4280, -110.5885, '5dcb4dc8-b218-4f1e-822d-6f29b4e5a2cf'),
    ('377822b5-1601-43d9-866d-15db7932579f', 'Penthouse Suite', 'A luxurious penthouse with panoramic city views.', 350, 48.856613, 2.352222, '3b8bcdc2-4910-4b7f-a3b5-e9b1a5c6b9c4');

-- Table Amenities
INSERT INTO amenities (id, name)
VALUES
    ('a12ef460-8e90-4e7a-8f43-1918a006078d', 'WiFi'),
    ('acbc951d-ef60-4486-84b9-87afc47d1eb2', 'Swimming Pool'),
    ('6fac204d-90b6-40cc-a87a-dbbc0814745e', 'Air Conditioning'),
    ('de9e2f01-bfac-4a56-a94d-8e1a453cb3cb', 'Fireplace'),
    ('5a73e4cd-3026-4f71-a65c-f7f1de342921', 'Hiking Trails'),
    ('c2e7de58-d6a4-4e0f-a79b-58a9ef8124c9', 'Mountain View'),
    ('db3f39de-7666-4636-b839-e51bfb47a6de', 'Smart TV'),
    ('f74cc8b7-1b53-4d78-93ef-3a59b544be4e', 'High-Speed WiFi'),
    ('e1b2f62e-447c-498c-8134-776d9db6c00c', 'Private Garden');

-- Table Place_Amenity
INSERT INTO place_amenity (place_id, amenity_id)
VALUES
    ('765a38e6-c131-4315-8e9c-28ac88424634', 'a12ef460-8e90-4e7a-8f43-1918a006078d'),
    ('765a38e6-c131-4315-8e9c-28ac88424634', 'acbc951d-ef60-4486-84b9-87afc47d1eb2'),
    ('765a38e6-c131-4315-8e9c-28ac88424634', '6fac204d-90b6-40cc-a87a-dbbc0814745e'),
    ('5c66b5f9-74a7-4767-8f5b-7d2b153b6057', 'de9e2f01-bfac-4a56-a94d-8e1a453cb3cb'),
    ('5c66b5f9-74a7-4767-8f5b-7d2b153b6057', '5a73e4cd-3026-4f71-a65c-f7f1de342921');

-- Table Reviews
INSERT INTO reviews (id, text, rating, user_id, place_id)
VALUES
    ('91c9f95a-6e21-44c7-9dd8-819e27d6c6c1', 'Great place to stay!', 4, '1b6ef38c-88cb-4bcf-9d0f-b70e39eb70a8', '765a38e6-c131-4315-8e9c-28ac88424634'),
    ('b2d4f9da-67e3-4029-ae6c-c58a179b61b6', 'Amazing location and very comfortable.', 5, '2a6fcbae-5bcf-48c8-b6b1-94d95dbf60b6', '765a38e6-c131-4315-8e9c-28ac88424634'),
    ('fc89d35d-cc41-409b-87ef-f8d6e35d84f3', 'So cozy and quiet!', 5, '2a6fcbae-5bcf-48c8-b6b1-94d95dbf60b6', '5c66b5f9-74a7-4767-8f5b-7d2b153b6057'),
    ('a7e5d4fc-5d2e-4a7f-9c77-e2e97a8eaf43', 'Perfect for business travel.', 4, '8bf65c58-7af4-49a4-a438-f28b8949cb84', '3f477fd8-fc69-47f1-8c22-12dc4db86099');
