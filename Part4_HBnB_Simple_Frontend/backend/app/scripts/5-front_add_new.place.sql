-- Users
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES
    ('1c1f38c1-33cc-4bdf-8d0f-b90e39eb80a1', 'Bob', 'Builder', 'bob.builder@hbnb.io', '$2a$12$E4jG5Vzq4DSO0jN0v7q/.SPyIYrX1d5Y3u2g/Emy4wOvlLglSKai6', FALSE),
    ('2d2fcbae-2ccc-48c8-b6b1-94d95dbf50b2', 'Mickey', 'Mouse', 'mickey.mouse@hbnb.io', '$2a$12$E4jG5Vzq4DSO0jN0v7q/.SPyIYrX1d5Y3u2g/Emy4wOvlLglSKai6', FALSE),
    ('8gf65c58-7ff4-49a4-a438-f28b8949cc84', 'Harry', 'Potter', 'harry.potter@hbnb.io', '$2a$12$E4jG5Vzq4DSO0jN0v7q/.SPyIYrX1d5Y3u2g/Emy4wOvlLglSKai6', FALSE),
    ('5scb4dc8-b218-4f1e-822d-6f29b4e5a3cf', 'Tony', 'Stark', 'tony.stark@hbnb.io', '$2a$12$E4jG5Vzq4DSO0jN0v7q/.SPyIYrX1d5Y3u2g/Emy4wOvlLglSKai6', FALSE),
    ('3b8bcdc2-8910-4b7f-a3b5-e9b1a5c7b9c4', 'Sherlock', 'Holmes', 'sherlock.holmes@hbnb.io', '$2a$12$E4jG5Vzq4DSO0jN0v7q/.SPyIYrX1d5Y3u2g/Emy4wOvlLglSKai6', FALSE);

-- Places
INSERT INTO places (id, title, description, price, latitude, longitude, owner_id)
VALUES
    ('5e5a38e6-c231-4315-8e9c-28ac88425634', 'Super Cheap Room', 'An ultra-affordable room with shared facilities. Great for adventurers on a budget.', 5, 45.764043, 4.835659, '1c1f38c1-33cc-4bdf-8d0f-b90e39eb80a1'),
    ('6c66b5f9-75b7-4767-8f5b-7d2b153b7057', 'Cheaper Cabin', 'Still cozy but much cheaper than its cousin.', 10, 47.218371, -1.553621, '2d2fcbae-2ccc-48c8-b6b1-94d95dbf50b2'),
    ('4f477fd8-fd69-47f1-8c22-12dc4db86199', 'Nice Apartment', 'A moderately priced apartment with all essentials.', 49, 48.856613, 2.352222, '8gf65c58-7ff4-49a4-a438-f28b8949cc84'),
    ('7e66193-4f0b-493d-bca2-94252343b5e3', 'Family Lakehouse', 'A great lakehouse with space for the entire family.', 50, 50.62925, 3.057256, '5scb4dc8-b218-4f1e-822d-6f29b4e5a3cf'),
    ('9c822b5-2601-43d9-866d-15db7932589f', 'Modern Villa', 'A stunning villa perfect for a luxury retreat.', 70, 43.710173, 7.261953, '3b8bcdc2-8910-4b7f-a3b5-e9b1a5c7b9c4'),
    ('3c88b0a2-b1a9-410e-a18c-4f5cd017ebae', 'Elegant Mansion', 'An elegant mansion with stunning architecture.', 350, 41.902783, 12.496366, '1c1f38c1-33cc-4bdf-8d0f-b90e39eb80a1');

-- Reviews
INSERT INTO reviews (id, text, rating, user_id, place_id)
VALUES
    ('21c9f95a-6e21-44c7-9dd8-819e27d6d6c1', 'I stayed here for 5€, and it was worth all 5 coins.', 4, '1c1f38c1-33cc-4bdf-8d0f-b90e39eb80a1', '5e5a38e6-c231-4315-8e9c-28ac88425634'),
    ('32d4f9da-67e3-4029-ae6c-c58a179b71b6', 'Amazing place, but bring your own tea.', 5, '2d2fcbae-2ccc-48c8-b6b1-94d95dbf50b2', '6c66b5f9-75b7-4767-8f5b-7d2b153b7057'),
    ('93c89d35-cc41-409b-87ef-f8d6e35d84f3', 'The host vanished, but the room was great.', 3, '8gf65c58-7ff4-49a4-a438-f28b8949cc84', '4f477fd8-fd69-47f1-8c22-12dc4db86199'),
    ('47e5d4fc-5d2e-4a7f-9c77-e2e97a8eaf43', 'Cozy house but haunted vibes.', 4, '5scb4dc8-b218-4f1e-822d-6f29b4e5a3cf', '7e66193-4f0b-493d-bca2-94252343b5e3'),
    ('81c822b5-2601-43d9-866d-15db7932579f', 'The villa was so modern, even my cat got Wi-Fi.', 5, '3b8bcdc2-8910-4b7f-a3b5-e9b1a5c7b9c4', '9c822b5-2601-43d9-866d-15db7932589f'),
    ('13c822b5-2601-43d9-866d-15db7932545f', 'This mansion is so elegant, I got inspired to write a novel.', 5, '1c1f38c1-33cc-4bdf-8d0f-b90e39eb80a1', '3c88b0a2-b1a9-410e-a18c-4f5cd017ebae');

-- INSERT INTO amenities (id, name)
-- VALUES
--     ('d1a8f46b-2e10-4b3b-bd63-8912ab3e72cf', 'WiFi'),
--     ('b3c7df68-4a77-4f0b-bd6a-74c5a8b83c25', 'Swimming Pool'),
--     ('e2c9ed7f-8d92-43b3-b816-5439eaa2c89b', 'Air Conditioning'),
--     ('a12ef460-8e90-4e7a-8f43-1918a006078d', 'Free Breakfast'),
--     ('acbc951d-ef60-4486-84b9-87afc47d1eb2', 'Gym'),
--     ('f85cc6b7-3c12-42e1-b3ff-8347b5a2be3a', 'Pet-Friendly'),
--     ('c8e7de58-d6a4-4e0f-a79b-58a9ef8124c9', 'Smart Home Automation'),
--     ('de9e2f01-bfac-4a56-a94d-8e1a453cb3cb', 'Fireplace'),
--     ('5a73e4cd-3026-4f71-a65c-f7f1de342921', 'Hiking Trails'),
--     ('db3f39de-7666-4636-b839-e51bfb47a6de', 'Smart TV'),
--     ('f74cc8b7-1b53-4d78-93ef-3a59b544be4e', 'High-Speed WiFi'),
--     ('e1b2f62e-447c-498c-8134-776d9db6c00c', 'Private Garden');

INSERT OR IGNORE INTO amenities (id, name)
VALUES
    ('d1a8f46b-2e10-4b3b-bd63-8912ab3e72cf', 'WiFi'),
    ('b3c7df68-4a77-4f0b-bd6a-74c5a8b83c25', 'Swimming Pool'),
    ('e2c9ed7f-8d92-43b3-b816-5439eaa2c89b', 'Air Conditioning'),
    ('a12ef460-8e90-4e7a-8f43-1918a006078d', 'Free Breakfast'),
    ('acbc951d-ef60-4486-84b9-87afc47d1eb2', 'Gym'),
    ('f85cc6b7-3c12-42e1-b3ff-8347b5a2be3a', 'Pet-Friendly'),
    ('c8e7de58-d6a4-4e0f-a79b-58a9ef8124c9', 'Smart Home Automation'),
    ('de9e2f01-bfac-4a56-a94d-8e1a453cb3cb', 'Fireplace'),
    ('5a73e4cd-3026-4f71-a65c-f7f1de342921', 'Hiking Trails'),
    ('db3f39de-7666-4636-b839-e51bfb47a6de', 'Smart TV'),
    ('f74cc8b7-1b53-4d78-93ef-3a59b544be4e', 'High-Speed WiFi'),
    ('e1b2f62e-447c-498c-8134-776d9db6c00c', 'Private Garden');


INSERT INTO place_amenity (place_id, amenity_id)
VALUES
    -- Super Cheap Room (5€)
    ('5e5a38e6-c231-4315-8e9c-28ac88425634', 'd1a8f46b-2e10-4b3b-bd63-8912ab3e72cf'), -- WiFi
    ('5e5a38e6-c231-4315-8e9c-28ac88425634', 'a12ef460-8e90-4e7a-8f43-1918a006078d'), -- Free Breakfast

    -- Cheaper Cabin (10€)
    ('6c66b5f9-75b7-4767-8f5b-7d2b153b7057', 'de9e2f01-bfac-4a56-a94d-8e1a453cb3cb'), -- Fireplace
    ('6c66b5f9-75b7-4767-8f5b-7d2b153b7057', '5a73e4cd-3026-4f71-a65c-f7f1de342921'), -- Hiking Trails

    -- Nice Apartment (49€)
    ('4f477fd8-fd69-47f1-8c22-12dc4db86199', 'b3c7df68-4a77-4f0b-bd6a-74c5a8b83c25'), -- Swimming Pool
    ('4f477fd8-fd69-47f1-8c22-12dc4db86199', 'e2c9ed7f-8d92-43b3-b816-5439eaa2c89b'), -- Air Conditioning

    -- Family Lakehouse (50€)
    ('7e66193-4f0b-493d-bca2-94252343b5e3', 'db3f39de-7666-4636-b839-e51bfb47a6de'), -- Smart TV
    ('7e66193-4f0b-493d-bca2-94252343b5e3', 'f85cc6b7-3c12-42e1-b3ff-8347b5a2be3a'), -- Pet-Friendly

    -- Modern Villa (70€)
    ('9c822b5-2601-43d9-866d-15db7932589f', 'c8e7de58-d6a4-4e0f-a79b-58a9ef8124c9'), -- Smart Home Automation
    ('9c822b5-2601-43d9-866d-15db7932589f', 'f74cc8b7-1b53-4d78-93ef-3a59b544be4e'), -- High-Speed WiFi

    -- Elegant Mansion (350€)
    ('3c88b0a2-b1a9-410e-a18c-4f5cd017ebae', 'db3f39de-7666-4636-b839-e51bfb47a6de'), -- Smart TV
    ('3c88b0a2-b1a9-410e-a18c-4f5cd017ebae', 'e1b2f62e-447c-498c-8134-776d9db6c00c'); -- Private Garden

