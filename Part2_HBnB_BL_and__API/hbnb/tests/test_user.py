#!/usr/bin/python3

# hbnb/tests/test_user.py

from app.models.user import User, ValidationError

def test_user_creation():
    try:
        user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="secure123")
        assert user.first_name == "John"
        assert user.last_name == "Doe"
        assert user.email == "john.doe@example.com"
        assert user.is_admin is False  # Default value
        print("User creation test passed!")
    except ValidationError as ve:
        print(f"User creation test failed: {ve}")

def test_user_invalid_email():
    try:
        user = User(first_name="Jane", last_name="Doe", email="invalidemail", password="password123")
    except ValidationError as ve:
        print(f"User invalid email test passed: {ve}")

def test_user_short_password():
    try:
        user = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com", password="123")
    except ValidationError as ve:
        print(f"User short password test passed: {ve}")

if __name__ == "__main__":
    test_user_creation()
    test_user_invalid_email()
    test_user_short_password()
