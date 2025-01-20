#!/usr/bin/env python3

import uuid
import json

# JSON data (replace with your JSON string)
json_data = {
  "places": [
    {
      "id": "da95ad35-4779-4e82-a04e-1994615afaee",
      "title": "Beautiful Beach House",
      "description": "A beautiful beach house with amazing views...",
      "price": 148,
      "latitude": 34.052235,
      "longitude": -118.243683,
      "owner_id": "314c6e2a-93f9-45a0-8710-c5e4e1b02582",
      "amenities": [
        "ec4c3164-bc5d-4e11-adaa-cb62a9692804"
      ]
    },
    {
      "id": "acdf2c05-85e6-45f8-8102-3548b2aae041",
      "title": "Cozy Cabin",
      "description": "A warm and inviting cabin in the woods.",
      "price": 100,
      "latitude": 37.774929,
      "longitude": -122.419416,
      "owner_id": "2a6fcbae-5bcf-48c8-b6b1-94d95dbf60b6",
      "amenities": [
        "2020ff8a-d5d0-4571-a30b-437a8a5fde81"
      ]
    },
    {
      "id": "9f63be1e-4b35-44db-8b16-d02651466efb",
      "title": "Modern Apartment",
      "description": "A sleek and stylish city apartment with modern amenities.",
      "price": 200,
      "latitude": 40.712776,
      "longitude": -74.005974,
      "owner_id": "8bf65c58-7af4-49a4-a438-f28b8949cb84",
      "amenities": []
    },
    {
      "id": "a81e4f58-28f0-406e-9ca0-54928694623a",
      "title": "Rustic Lakehouse",
      "description": "A charming lakehouse with a beautiful view of the sunset.",
      "price": 180,
      "latitude": 44.428,
      "longitude": -110.5885,
      "owner_id": "5dcb4dc8-b218-4f1e-822d-6f29b4e5a2cf",
      "amenities": [
        "de9e2f01-bfac-4a56-a94d-8e1a453cb3cb",
        "5a73e4cd-3026-4f71-a65c-f7f1de342921"
      ]
    },
    {
      "id": "f153c5be-d5b8-4693-beb8-204f397fc249",
      "title": "Penthouse Suite",
      "description": "A luxurious penthouse with panoramic city views.",
      "price": 350,
      "latitude": 48.856613,
      "longitude": 2.352222,
      "owner_id": "3b8bcdc2-4910-4b7f-a3b5-e9b1a5c6b9c4",
      "amenities": []
    },
    {
      "id": "911e597a-5d37-47f9-9d4c-58c5b6efc8a3",
      "title": "Super Cheap Room",
      "description": "An ultra-affordable room with shared facilities. Great for adventurers on a budget.",
      "price": 5,
      "latitude": 45.764043,
      "longitude": 4.835659,
      "owner_id": "1c1f38c1-33cc-4bdf-8d0f-b90e39eb80a1",
      "amenities": [
        "db3f39de-7666-4636-b839-e51bfb47a6de",
        "f85cc6b7-3c12-42e1-b3ff-8347b5a2be3a"
      ]
    },
    {
      "id": "84786c83-cbfa-460d-9e49-bfd1eda8425e",
      "title": "Cheaper Cabin",
      "description": "Still cozy but much cheaper than its cousin.",
      "price": 10,
      "latitude": 47.218371,
      "longitude": -1.553621,
      "owner_id": "2d2fcbae-2ccc-48c8-b6b1-94d95dbf50b2",
      "amenities": [
        "c8e7de58-d6a4-4e0f-a79b-58a9ef8124c9",
        "f74cc8b7-1b53-4d78-93ef-3a59b544be4e"
      ]
    },
    {
      "id": "cba26651-e709-4b99-abaf-6035c2a2347b",
      "title": "Nice Apartment",
      "description": "A moderately priced apartment with all essentials.",
      "price": 49,
      "latitude": 48.856613,
      "longitude": 2.352222,
      "owner_id": "e79dd06a-de35-4d7d-81b4-ea91671c7ea3",
      "amenities": [
        "db3f39de-7666-4636-b839-e51bfb47a6de",
        "e1b2f62e-447c-498c-8134-776d9db6c00c"
      ]
    },
    {
      "id": "6dd217a8-72e4-4bb0-8f01-0c1572474190",
      "title": "Family Lakehouse",
      "description": "A great lakehouse with space for the entire family.",
      "price": 50,
      "latitude": 50.62925,
      "longitude": 3.057256,
      "owner_id": "0ca2ab58-1181-4e37-b0b0-48317044021e",
      "amenities": []
    },
    {
      "id": "44e4eaf0-1863-4c96-b40f-4e58f4e47f0d",
      "title": "Modern Villa",
      "description": "A stunning villa perfect for a luxury retreat.",
      "price": 70,
      "latitude": 43.710173,
      "longitude": 7.261953,
      "owner_id": "3b8bcdc2-8910-4b7f-a3b5-e9b1a5c7b9c4",
      "amenities": []
    },
    {
      "id": "447a3ede-918f-4543-9e5e-86f74b8ed5e4",
      "title": "Elegant Mansion",
      "description": "An elegant mansion with stunning architecture.",
      "price": 350,
      "latitude": 41.902783,
      "longitude": 12.496366,
      "owner_id": "1c1f38c1-33cc-4bdf-8d0f-b90e39eb80a1",
      "amenities": []
    },
    {
      "id": "7de0a1b4-a506-4b05-a5a9-b27f14239ee5",
      "title": "test",
      "description": "test2",
      "price": 25,
      "latitude": 10,
      "longitude": 10,
      "owner_id": "ea4e1163-0657-43a3-9fd9-6ec1f8bebba1",
      "amenities": []
    },
    {
      "id": "8498cd8a-6bb5-40fa-950f-81c1706d5064",
      "title": "test",
      "description": "test",
      "price": 12,
      "latitude": 1,
      "longitude": 1,
      "owner_id": "ea4e1163-0657-43a3-9fd9-6ec1f8bebba1",
      "amenities": []
    }
  ]
}

def is_valid_uuid4(value):
    """Check if the value is a valid UUID4."""
    try:
        uuid_obj = uuid.UUID(value, version=4)
        return str(uuid_obj) == value  # Ensure format matches
    except ValueError:
        return False

def validate_places(data):
    """Validate the UUID fields in the places data."""
    for place in data["places"]:
        print(f"Validating Place: {place.get('title', 'Unknown')}")
        # Validate `id`
        id_status = "✅" if is_valid_uuid4(place["id"]) else "❌"
        print(f"  ID: {place['id']} {id_status}")

        # Validate `owner_id`
        owner_status = "✅" if is_valid_uuid4(place["owner_id"]) else "❌"
        print(f"  Owner ID: {place['owner_id']} {owner_status}")

        # Validate each `amenity` ID
        for idx, amenity in enumerate(place.get("amenities", [])):
            amenity_status = "✅" if is_valid_uuid4(amenity) else "❌"
            print(f"  Amenity {idx + 1}: {amenity} {amenity_status}")

# Run validation
validate_places(json_data)
