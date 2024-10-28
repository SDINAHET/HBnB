```plaintext
██╗  ██╗██████╗ ███╗   ██╗██████╗
██║  ██║██╔══██╗████╗  ██║██╔══██╗
███████║███████║██╔██╗ ██║███████║
██╔══██║██║  ██║██║╚██╗██║██║  ██║
██║  ██║██████╔╝██║ ╚████║██████╔╝
╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝╚═════╝
 | HBnB Part2 Logo  # C24
'''

# HBnB Application - Part 2: Implementation of Business Logic and API Endpoints

## Overview

In Part 2 of the HBnB Project, the focus shifts to the **Implementation Phase**. This phase involves building the **Presentation** and **Business Logic** layers of the application using Python and Flask. The core functionality is brought to life by defining the necessary classes, methods, and API endpoints that form the foundation of the HBnB application.

**Note:** At this stage, user authentication and role-based access control are not implemented. These features will be addressed in the subsequent part of the project.

## Table of Contents

- [Objectives](#objectives)
- [Project Vision and Scope](#project-vision-and-scope)
- [Learning Objectives](#learning-objectives)
- [Project Setup and Package Initialization](#project-setup-and-package-initialization)
- [Implement Core Business Logic Classes](#implement-core-business-logic-classes)
- [Implement API Endpoints](#implement-api-endpoints)
  - [User Endpoints](#user-endpoints)
  - [Amenity Endpoints](#amenity-endpoints)
  - [Place Endpoints](#place-endpoints)
  - [Review Endpoints](#review-endpoints)
- [Testing and Validation](#testing-and-validation)
- [Resources](#resources)
- [Repository Information](#repository-information)
- [Contributors](#contributors)

## Objectives

This is objectives of this project:

1. **Set Up the Project Structure:**
   - Organize the project into a modular architecture following best practices for Python and Flask applications.
   - Create necessary packages for the Presentation and Business Logic layers.

2. **Implement the Business Logic Layer:**
   - Develop core classes for business logic, including `User`, `Place`, `Review`, and `Amenity` entities.
   - Implement relationships between entities and define their interactions.
   - Utilize the Facade pattern to simplify communication between the Presentation and Business Logic layers.

3. **Build RESTful API Endpoints:**
   - Implement CRUD operations for Users, Places, Reviews, and Amenities.
   - Use `flask-restx` to define and document the API, ensuring a clear and consistent structure.
   - Implement data serialization to return extended attributes for related objects (e.g., owner details and amenities when retrieving a Place).

4. **Test and Validate the API:**
   - Ensure that each endpoint works correctly and handles edge cases appropriately.
   - Use tools like Postman or cURL to test API endpoints.
   - Create a detailed testing report highlighting both successful and failed cases.

## Project Vision and Scope

The implementation phase focuses on creating a functional and scalable foundation for the HBnB application by developing:

- **Presentation Layer:** Defining services and API endpoints using Flask and `flask-restx`. Endpoints are structured logically, ensuring clear paths and parameters for each operation.

- **Business Logic Layer:** Building core models and logic that drive the application’s functionality, including defining relationships, handling data validation, and managing interactions between different components.

**Note:** User authentication and access control will be integrated in Part 3.

## Learning Objectives

This part of the project is designed to help you achieve the following learning outcomes:

- **Modular Design and Architecture:** Learn how to structure a Python application using best practices for modularity and separation of concerns.

- **API Development with Flask and flask-restx:** Gain hands-on experience in building RESTful APIs using Flask, focusing on creating well-documented and scalable endpoints.

- **Business Logic Implementation:** Understand how to translate documented designs into working code, implementing core business logic in a structured and maintainable manner.

- **Data Serialization and Composition Handling:** Practice returning extended attributes in API responses, handling nested and related data efficiently.

- **Testing and Debugging:** Develop skills in testing and validating APIs to ensure that endpoints handle requests correctly and return appropriate responses.

## Project Setup and Package Initialization

### 1. Project Directory Structure

Organize the project into a modular architecture with clear separation of concerns:

```text
    hbnb/
    ├── app/
    │   ├── __init__.py
    │   ├── api/
    │   │   ├── __init__.py
    │   │   ├── v1/
    │   │       ├── __init__.py
    │   │       ├── users.py
    │   │       ├── places.py
    │   │       ├── reviews.py
    │   │       ├── amenities.py
    │   ├── models/
    │   │   ├── __init__.py
    │   │   ├── base_entity.py
    │   │   ├── user.py
    │   │   ├── place.py
    │   │   ├── review.py
    │   │   ├── amenity.py
    │   ├── services/
    │   │   ├── __init__.py
    │   │   ├── facade.py
    │   ├── persistence/
    │       ├── __init__.py
    │       ├── repository.py
    ├── run.py
    ├── config.py
    ├── requirements.txt
    ├── README.md
```

### 2. Initializing Python Packages

Ensure each directory intended to be a Python package contains an `__init__.py` file. This allows Python to recognize these directories as importable packages.

For example, `hbnb/app/__init__.py`:

```python
# hbnb/app/__init__.py
```

Similarly, other __init__.py files can remain empty or include initialization code as needed.

### 3. Setting Up the Flask Application with Placeholders

Initialize the Flask application within app/__init__.py:

```python
# hbnb/app/__init__.py

from flask import Flask
from flask_restx import Api

def create_app(config_name=None):
    app = Flask(__name__)

    # Load configuration
    if config_name:
        from ..config import config
        app.config.from_object(config[config_name])
    else:
        from ..config import config
        app.config.from_object(config['default'])

    api = Api(
        app,
        version='1.0',
        title='HBnB API',
        description='HBnB Application API'
    )

    # Import and add API namespaces (placeholders)
    from .api.v1 import users, places, reviews, amenities
    api.add_namespace(users.api, path='/api/v1/users')
    api.add_namespace(places.api, path='/api/v1/places')
    api.add_namespace(reviews.api, path='/api/v1/reviews')
    api.add_namespace(amenities.api, path='/api/v1/amenities')

    return app
```

### 4. Implementing the In-Memory Repository

The in-memory repository handles object storage and provides an interface that can later be replaced with a database-backed solution.

app/persistence/repository.py

```python
# hbnb/app/persistence/repository.py

from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        """Add an object to the repository."""
        pass

    @abstractmethod
    def get(self, obj_id):
        """Retrieve an object by its ID."""
        pass

    @abstractmethod
    def get_all(self):
        """Retrieve all objects."""
        pass

    @abstractmethod
    def update(self, obj_id, data):
        """Update an object with the provided data."""
        pass

    @abstractmethod
    def delete(self, obj_id):
        """Delete an object by its ID."""
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        """Retrieve an object by a specific attribute."""
        pass


class InMemoryRepository(Repository):
    def __init__(self):
        self._storage = {}

    def add(self, obj):
        """Add an object to the repository."""
        self._storage[obj.id] = obj

    def get(self, obj_id):
        """Retrieve an object by its ID."""
        return self._storage.get(obj_id)

    def get_all(self):
        """Retrieve all objects."""
        return list(self._storage.values())

    def update(self, obj_id, data):
        """Update an object with the provided data."""
        obj = self.get(obj_id)
        if obj:
            obj.update(data)

    def delete(self, obj_id):
        """Delete an object by its ID."""
        if obj_id in self._storage:
            del self._storage[obj_id]

    def get_by_attribute(self, attr_name, attr_value):
        """Retrieve an object by a specific attribute."""
        return next((obj for obj in self._storage.values() if getattr(obj, attr_name, None) == attr_value), None)
```

### 5. Planning for the Facade Pattern

Implement the Facade pattern to simplify communication between the Presentation and Business Logic layers.
app/services/facade.py

```python
# hbnb/app/services/facade.py

from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # User Methods
    def create_user(self, first_name: str, last_name: str, email: str, password: str, is_admin: bool = False) -> User:
        user = User(first_name=first_name, last_name=last_name, email=email, password=password, is_admin=is_admin)
        self.user_repo.add(user)
        user.register_profile()
        return user

    def get_user(self, user_id: str) -> User:
        return self.user_repo.get(user_id)

    def get_all_users(self) -> list:
        return self.user_repo.get_all()

    def update_user(self, user_id: str, data: dict):
        self.user_repo.update(user_id, data)

    def delete_user(self, user_id: str):
        user = self.get_user(user_id)
        if user:
            # Optionally handle cascading deletes
            self.user_repo.delete(user_id)
            user.delete_profile()

    # Amenity Methods
    def create_amenity(self, name: str, description: str = "") -> Amenity:
        amenity = Amenity(name=name, description=description)
        self.amenity_repo.add(amenity)
        amenity.create_amenity()
        return amenity

    def get_amenity(self, amenity_id: str) -> Amenity:
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self) -> list:
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id: str, data: dict):
        self.amenity_repo.update(amenity_id, data)

    def delete_amenity(self, amenity_id: str):
        amenity = self.get_amenity(amenity_id)
        if amenity:
            self.amenity_repo.delete(amenity_id)
            amenity.delete_amenity()

    # Place Methods
    def create_place(self, title: str, description: str, price: float, latitude: float, longitude: float, owner_id: str) -> Place:
        owner = self.get_user(owner_id)
        if not owner:
            raise ValueError("Owner not found.")
        place = Place(title=title, description=description, price=price, latitude=latitude, longitude=longitude, owner=owner)
        self.place_repo.add(place)
        place.create_place()
        return place

    def get_place(self, place_id: str) -> Place:
        return self.place_repo.get(place_id)

    def get_all_places(self) -> list:
        return self.place_repo.get_all()

    def update_place(self, place_id: str, data: dict):
        self.place_repo.update(place_id, data)

    def delete_place(self, place_id: str):
        place = self.get_place(place_id)
        if place:
            self.place_repo.delete(place_id)
            place.delete_place()

    # Review Methods
    def create_review(self, text: str, rating: int, place_id: str, user_id: str) -> Review:
        place = self.get_place(place_id)
        user = self.get_user(user_id)
        if not place:
            raise ValueError("Place not found.")
        if not user:
            raise ValueError("User not found.")
        review = Review(text=text, rating=rating, place=place, user=user)
        self.review_repo.add(review)
        review.create_review()
        return review

    def get_review(self, review_id: str) -> Review:
        return self.review_repo.get(review_id)

    def get_all_reviews(self) -> list:
        return self.review_repo.get_all()

    def update_review(self, review_id: str, data: dict):
        self.review_repo.update(review_id, data)

    def delete_review(self, review_id: str):
        review = self.get_review(review_id)
        if review:
            self.review_repo.delete(review_id)
            review.delete_review()
```

```python
```


```python
```


























# HBnB API Testing and Validation

## Validation
Each endpoint includes validation checks for attributes to ensure data integrity and prevent invalid data from being processed. Examples:

- **User Creation**: Validates that the first name and last name are provided and do not exceed 50 characters, the email follows a standard format, and the password is at least 6 characters long.
- **Place Creation**: Validates that the title is provided and does not exceed 100 characters, the price is a positive value, and the latitude and longitude are within valid ranges.

## Testing Tools
- **cURL**: Used for black-box testing to verify each endpoint’s response format and status codes.
- **Postman**: An alternative tool for testing API endpoints with a user-friendly interface.
- **Flask-RESTx Swagger Documentation**: Automatically generated documentation available at [http://localhost:5000/api/v1/](http://localhost:5000/api/v1/) to visually confirm the API structure.

## Example cURL Commands
### Create a User
```bash
curl -X POST http://localhost:5000/api/v1/users/ \
     -H "Content-Type: application/json" \
     -d '{"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "password": "secure123"}'
```
### Get All Users
```bash
curl http://localhost:5000/api/v1/users/
```

### Get a Specific User
```bash
curl http://localhost:5000/api/v1/users/<user_id>
```

### Update a User
```bash
curl -X PUT http://localhost:5000/api/v1/users/<user_id> \
     -H "Content-Type: application/json" \
     -d '{"first_name": "Jane", "email": "jane.doe@example.com"}'
```

### Create an Amenity
```bash
curl -X POST http://localhost:5000/api/v1/amenities/ \
     -H "Content-Type: application/json" \
     -d '{"name": "Wi-Fi", "description": "High-speed wireless internet"}'
```

### Create a Place
```bash
curl -X POST http://localhost:5000/api/v1/places/ \
     -H "Content-Type: application/json" \
     -d '{
           "title": "Cozy Apartment",
           "description": "A nice place to stay",
           "price": 100.0,
           "latitude": 37.7749,
           "longitude": -122.4194,
           "owner_id": "<user_id>",
           "amenities": ["<amenity_id1>", "<amenity_id2>"]
         }'
```

### Create a Review
```bash
curl -X POST http://localhost:5000/api/v1/reviews/ \
     -H "Content-Type: application/json" \
     -d '{
           "text": "Great place!",
           "rating": 5,
           "place_id": "<place_id>",
           "user_id": "<user_id>"
         }'
```

### Automated Testing
Implement unit tests using unittest or pytest to automate testing of business logic and API endpoints.

Example: Testing User Creation
```bash
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
```

# Resources

## Flask and Flask-RESTx Documentation
- [Flask Official Documentation](https://flask.palletsprojects.com/)
- [Flask-RESTx Documentation](https://flask-restx.readthedocs.io/)

## RESTful API Design Best Practices
- [Best Practices for Designing a Pragmatic RESTful API](https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api)
- [REST API Tutorial](https://restfulapi.net/)

## Python Project Structure and Modular Design
- [Structuring Your Python Project](https://docs.python-guide.org/writing/structure/)
- [Modular Programming with Python](https://realpython.com/python-modules-packages/)

## Facade Design Pattern
- [Facade Pattern in Python](https://refactoring.guru/design-patterns/facade)

## Testing REST APIs
- [Testing REST APIs with cURL](https://everything.curl.dev/)
- [Postman Documentation](https://learning.postman.com/docs/)

## Repository Information
- **GitHub Repository**: [holbertonschool-hbnb](https://github.com/holbertonschool-hbnb)
- **Directory**: `part2`

## Contributors
- Louis Beaumois
- Stéphane Dinahet
- Henri Milles


###
```bash

```

###
```bash

```

###
```bash

```

###
```bash

```

###
```bash

```

###
```bash

```

###
```bash

```
