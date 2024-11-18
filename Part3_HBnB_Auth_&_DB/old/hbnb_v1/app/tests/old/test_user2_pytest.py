#!/usr/bin/python3

import sys
import os
import requests
from datetime import datetime
import pytest
from app.models.user import User, ValidationError

BASE_URL = "http://localhost:5000/api/v1/users/"

# Append the project's root directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.fixture
def unique_email():
    """Generate a unique email address for testing."""
    unique_email.counter += 1
    return f"test_user_{unique_email.counter}@example.com"

unique_email.counter = 0

@pytest.fixture
def default_user(unique_email):
    """Create a default user for tests."""
    return User(first_name="John", last_name="Doe", email=unique_email)

def test_user_creation(default_user):
    """Test successful user creation."""
    assert default_user.first_name == "John"
    assert default_user.last_name == "Doe"
    assert default_user.email == default_user.email
    assert not default_user.is_admin  # Default value
    assert isinstance(default_user.created_at, datetime)
    assert isinstance(default_user.updated_at, datetime)

def test_user_invalid_email():
    """Test user creation with an invalid email."""
    with pytest.raises(ValidationError):
        User(first_name="Jane", last_name="Doe", email="invalidemail")

def test_user_missing_first_name(unique_email):
    """Test user creation with a missing first name."""
    with pytest.raises(ValidationError):
        User(first_name="", last_name="Doe", email=unique_email)

def test_user_missing_last_name(unique_email):
    """Test user creation with a missing last name."""
    with pytest.raises(ValidationError):
        User(first_name="Jane", last_name="", email=unique_email)

def test_user_unique_email(unique_email):
    """Test that email must be unique."""
    User(first_name="John", last_name="Doe", email=unique_email)
    with pytest.raises(ValidationError):
        User(first_name="Jane", last_name="Smith", email=unique_email)

def test_user_first_name_length(unique_email):
    """Test user creation with a first name exceeding maximum length."""
    with pytest.raises(ValidationError):
        User(first_name="A" * 51, last_name="Doe", email=unique_email)

def test_user_last_name_length(unique_email):
    """Test user creation with a last name exceeding maximum length."""
    with pytest.raises(ValidationError):
        User(first_name="John", last_name="D" * 51, email=unique_email)

def test_user_id_type(default_user):
    """Test that the user id is of the correct type."""
    assert isinstance(default_user.id, str)

def test_user_is_admin_default(default_user):
    """Test that the default value for is_admin is False."""
    assert not default_user.is_admin

def test_user_update(default_user):
    """Test updating user information and ensuring updated_at changes."""
    old_updated_at = default_user.updated_at
    default_user.first_name = "Jane"
    default_user.last_name = "Smith"
    default_user.email = unique_email()

    # Assuming your User model has a method to save the updated user
    default_user.save()

    # Check if the values have been updated
    assert default_user.first_name == "Jane"
    assert default_user.last_name == "Smith"
    assert default_user.email != default_user.email

    # Check if updated_at has changed
    assert default_user.updated_at > old_updated_at

# Uncomment and implement these tests as needed
# def test_create_user():
#     # Implement the test logic for creating a user via API
#
# def test_get_user_by_id():
#     # Implement the test logic for retrieving a user by ID via API
#
# def test_list_users():
#     # Implement the test logic for listing users via API
#
# def test_update_user():
#     # Implement the test logic for updating a user via API

if __name__ == "__main__":
    pytest.main()
