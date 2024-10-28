```plaintext
██╗  ██╗██████╗ ███╗   ██╗██████╗
██║  ██║██╔══██╗████╗  ██║██╔══██╗
███████║███████║██╔██╗ ██║███████║
██╔══██║██║  ██║██║╚██╗██║██║  ██║
██║  ██║██████╔╝██║ ╚████║██████╔╝
╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝╚═════╝
 | HBnB Logo  # C24
'''

# Introduction to Part 2: Implementation of Business Logic and API Endpoints

In this phase of the HBnB project, you'll implement the core functionality of the application using Python and Flask. This will involve building the Presentation and Business logic layers, and defining essential classes, methods and API endpoints, based on the design developed in the previous part.

The goal is to bring the documented architecture to life by creating the project structure, develop the business logic, and implement key functionality such as managing users, places, reviews, and amenities.

## Project Vision and Scope

This part is focused on creating a functional and scalable foundation for the application. You will be working on:

- **Business Logic Layer:** Building the core models and logic that drive the application's functionality. This includes defining relationships, handling data validation, and managing interactions between different components.

- **Presentation Layer:** Defining the services and API endpoints using Flask and `flask-restx`. You will structure the endpoints logically, ensuring clear paths and parameters for each operation.

## Learning Objectives

This part of the project is designed to help you achieve the following learning outcomes:

1. **Set Up the Project Structure:**

    - Organize the project into a modular architecture, following best practices for Python and Flask applications.
    - Create the necessary packages for the Presentation and Business Logic layers.

2. **Implement the Business Logic Layer:**

    Understand how to translate documented designs into working code by:

    - Develop the core classes for the business logic, including User, Place, Review, and Amenity entities.
    - Implement relationships between entities and define how they interact within the application.
    - Implement the facade pattern to simplify communication between the Presentation and Business Logic layers.

3. **Build RESTful API Endpoints:**

    - Implement the necessary API endpoints to handle CRUD operations for Users, Places, Reviews, and Amenities.
    - Use `flask-restx` to define and document the API, ensuring a clear and consistent structure.
    - Implement data serialization to return extended attributes for related objects. For example, when retrieving a Place, the API should include details such as the owner's `first_name`, `last_name`, and relevant amenities.

4. **Test and Validate the API:**

    - Write tests to validate the behavior of the business logic classes.
    - Ensure that the API responses are consistent with the expected behavior.
    - Ensure that each endpoint works correctly and handles edge cases appropriately.

### Recommended Resources

- [Flask Official Documentation](https://flask.palletsprojects.com/)
- [flask-restx Documentation](https://flask-restx.readthedocs.io/)
- [Best Practices for Designing a Pragmatic RESTful API](https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api)
- [REST API Tutorial](https://restfulapi.net/)
- [Structuring Your Python Project](https://docs.python-guide.org/writing/structure/)
- [Modular Programming with Python](https://realpython.com/python-modules-packages/)
- [Facade Pattern in Python](https://refactoring.guru/design-patterns/facade/python/example)

###### _________________________
# Project Setup and Package Initialization

## Context

Before diving into the implementation of the business logic and API endpoints, it's essential to have **a well-organized project structure**. A **clear** and **modular** organization will help maintain the codebase, make it easier to integrate new features, and **ensure that your application is scalable**.

Additionally, to simplify the implementation, you are provided with the **complete in-memory repository code**.

## In this task, you will

1. Set up the structure for the Presentation, Business Logic, and Persistence layers, creating the necessary folders, packages, and files.
2. Prepare the project to use the Facade pattern for communication between layers.
3. Implement the in-memory repository to handle object storage and validation.
4. Plan for future integration of the Persistence layer, even though it won't be fully implemented in this part.

Although the Persistence layer will be fully implemented in Part 3, this task includes the implementation of the in-memory repository. This repository will later be replaced by a database-backed solution in Part 3.

## Instructions

1. **Create the Project Directory Structure**:

    Your project should be organized into the following structure:

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

    **Explanation:**

    - The `app/` directory contains the core application code.
    - The `api/` subdirectory houses the API endpoints, organized by version (`v1/`).
    - The `models/` subdirectory contains the business logic classes (e.g., `user.py`, `place.py`).
    - The `services/` subdirectory is where the Facade pattern is implemented, managing the interaction between layers.
    - The `persistence/` subdirectory is where the in-memory repository is implemented. This will later be replaced by a database-backed solution using SQL Alchemy.
    - `run.py` is the entry point for running the Flask application.
    - `config.py` will be used for configuring environment variables and application settings.
    - `requirements.txt` will list all the Python packages needed for the project.
    - `README.md` will contain a brief overview of the project.

2. **Initialize Python Packages**

    In each directory that is intended to be a Python package (e.g., `app/`, `api/`, `models/`, `services/`, `persistence/`, `v1/`), create an empty `__init__.py` file. This tells Python to treat these directories as importable packages.

3. **Set Up the Flask Application with Placeholders**

    Inside the `app/` directory, create the Flask application instance within the `__init__.py` file:

    ```python
    from flask import Flask
    from flask_restx import Api

    def create_app():
        app = Flask(__name__)
        api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1/')

        # Placeholder for API namespaces (endpoints will be added later)
        # Additional namespaces for places, reviews, and amenities will be added later

        return app
    ```

4. **Implement the In-Memory Repository**

    The in-memory repository will handle object storage and validation. It follows a consistent interface that will later be replaced by a database-backed repository.

    **Create the following structure under the `persistence/` directory:**

    ```text
    hbnb/
    ├── app/
    │   ├── persistence/
    │       ├── __init__.py
    │       ├── repository.py
    ```

    **Inside `repository.py`, the in-memory repository and interface will be fully implemented:**

    ```python
    from abc import ABC, abstractmethod

    class Repository(ABC):
        @abstractmethod
        def add(self, obj):
            pass

        @abstractmethod
        def get(self, obj_id):
            pass

        @abstractmethod
        def get_all(self):
            pass

        @abstractmethod
        def update(self, obj_id, data):
            pass

        @abstractmethod
        def delete(self, obj_id):
            pass

        @abstractmethod
        def get_by_attribute(self, attr_name, attr_value):
            pass


    class InMemoryRepository(Repository):
        def __init__(self):
            self._storage = {}

        def add(self, obj):
            self._storage[obj.id] = obj

        def get(self, obj_id):
            return self._storage.get(obj_id)

        def get_all(self):
            return list(self._storage.values())

        def update(self, obj_id, data):
            obj = self.get(obj_id)
            if obj:
                obj.update(data)

        def delete(self, obj_id):
            if obj_id in self._storage:
                del self._storage[obj_id]

        def get_by_attribute(self, attr_name, attr_value):
            return next((obj for obj in self._storage.values() if getattr(obj, attr_name) == attr_value), None)
    ```

5. **Plan for the Facade Pattern with Placeholders**

    In the `services/` subdirectory, create a `facade.py` file where you will define the `HBnBFacade` class. This class will handle communication between the Presentation, Business Logic, and Persistence layers. You will interact with the repositories (like the in-memory repository) through this Class:

    ```python
    from app.persistence.repository import InMemoryRepository

    class HBnBFacade:
        def __init__(self):
            self.user_repo = InMemoryRepository()
            self.place_repo = InMemoryRepository()
            self.review_repo = InMemoryRepository()
            self.amenity_repo = InMemoryRepository()

        # Placeholder method for creating a user
        def create_user(self, user_data):
            # Logic will be implemented in later tasks
            pass

        # Placeholder method for fetching a place by ID
        def get_place(self, place_id):
            # Logic will be implemented in later tasks
            pass
    ```

    The methods in the Facade use placeholders to avoid errors during initial testing. The actual logic will be added in future tasks.

    Let's create an instance of the `HBnBFacade` class in the `__init__.py` file of the `services/` directory:

    ```python
    from app.services.facade import HBnBFacade

    facade = HBnBFacade()
    ```

    This `facade` instance will be used as a [singleton](https://refactoring.guru/design-patterns/singleton) to make sure that only one instance of the `HBnBFacade` class is created and used throughout the application.

6. **Create the Entry Point**

    In the root directory, create the `run.py` file that will serve as the entry point for running the application:

    ```python
    from app import create_app

    app = create_app()

    if __name__ == '__main__':
        app.run(debug=True)
    ```

7. **Prepare the Configuration**

    In the root directory, create a `config.py` file where you can define environment-specific settings. For now, you can start with a basic configuration:

    ```python
    import os

    class Config:
        SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
        DEBUG = False

    class DevelopmentConfig(Config):
        DEBUG = True

    config = {
        'development': DevelopmentConfig,
        'default': DevelopmentConfig
    }
    ```

    You'll enhance this file as needed in later stages of the project.

8. **Document the Project Setup**

    In the `README.md` file, write a brief overview of the project setup:
    - Describe the purpose of each directory and file.
    - Include instructions on how to install dependencies and run the application.

9. **Install Required Packages**

    In the `requirements.txt` file, list the Python packages needed for the project:

    ```text
    flask
    flask-restx
    ```

    Install the dependencies using:

    ```bash
    pip install -r requirements.txt
    ```

10. **Test the Initial Setup**

    Run the application to ensure everything is set up correctly:

    ```bash
    python run.py
    ```

    You should see the Flask application running, although no routes are functional yet. This confirms that the project structure and basic setup are correct and ready for further development.

## Expected Outcome

By the end of this task, you'll have a well-organized, modular project structure with clear separation of concerns across the Presentation, Business Logic, and Persistence layers. The Flask application will be functional, with an in-memory repository and Facade pattern in place, ready for future integration of API endpoints and a database-backed persistence layer.

### Resources

- [**Flask Documentation**](https://flask.palletsprojects.com/)
- [**Flask-RESTx Documentation**](https://flask-restx.readthedocs.io/)
- [**Python Project Structure Best Practices**](https://docs.python-guide.org/writing/structure/)
- [**Facade Design Pattern in Python**](https://refactoring.guru/design-patterns/facade/python/example)
###### _________________________
# Implement Core Business Logic Classes

## Context

In Part 1, students designed the Business Logic layer, including defining entities and relationships. This task requires you to implement those designs while adhering to best practices for modular, maintainable code. You may have already created base classes with common attributes (e.g., `id`, `created_at`, and `updated_at`) to be inherited by concrete classes such as `User`, `Place`, `Review`, and `Amenity`.

## Why UUIDs Are Used as Identifiers

In the HBnB application, each object is identified by a universally unique identifier (UUID) instead of a sequential numeric ID. Here’s why:

1. **Global Uniqueness:** UUIDs are guaranteed to be unique across different systems and databases. This allows for distributed systems and ensures that IDs don’t clash when combining data from multiple sources.
2. **Security Considerations:** Sequential numeric IDs can reveal information about the system, such as the total number of users or entities. UUIDs are non-sequential and harder to predict, adding a layer of security by preventing malicious users from easily guessing valid IDs.
3. **Scalability and Flexibility:** UUIDs support systems that need to scale across multiple servers or regions. The decentralized generation of UUIDs ensures no conflict when data is merged or moved across systems.

For a deeper dive into why UUIDs are preferable in certain scenarios, you can refer to this article: [What are UUIDs, and are they better than regular IDs?](https://blog.boot.dev/clean-code/what-are-uuids-and-should-you-use-them/)

## Objective

In this task, you will:

1. **Implement the Classes**: Develop the core business logic classes for User, Place, Review, and Amenity based on your Part 1 design.

2. **Ensure Relationships**: Correctly implement the relationships between entities (e.g., User to Review, Place to Amenity, etc).

3. **Handle Attribute Validation and Updates**: Validate attributes and manage updates as per the defined requirements.

## Instructions

### Class guidelines before Implementation

Each class should include the following attributes, with appropriate types and value restrictions:

- **User Class:**

  - `id` (String): Unique identifier for each user.
  - `first_name` (String): The first name of the user. Required, maximum length of 50 characters.
  - `last_name` (String): The last name of the user. Required, maximum length of 50 characters.
  - `email` (String): The email address of the user. Required, must be unique, and should follow standard email format validation.
  - `is_admin` (Boolean): Indicates whether the user has administrative privileges. Defaults to `False`.
  - `created_at` (DateTime): Timestamp when the user is created.
  - `updated_at` (DateTime): Timestamp when the user is last updated.

- **Place Class:**

  - `id` (String): Unique identifier for each place.
  - `title` (String): The title of the place. Required, maximum length of 100 characters.
  - `description` (String): Detailed description of the place. Optional.
  - `price` (Float): The price per night for the place. Must be a positive value.
  - `latitude` (Float): Latitude coordinate for the place location. Must be within the range of -90.0 to 90.0.
  - `longitude` (Float): Longitude coordinate for the place location. Must be within the range of -180.0 to 180.0.
  - `owner` (User): `User` instance of who owns the place. This should be validated to ensure the owner exists.
  - `created_at` (DateTime): Timestamp when the place is created.
  - `updated_at` (DateTime): Timestamp when the place is last updated.

- **Review Class:**

  - `id` (String): Unique identifier for each review.
  - `text` (String): The content of the review. Required.
  - `rating` (Integer): Rating given to the place, must be between 1 and 5.
  - `place` (Place): `Place` instance being reviewed. Must be validated to ensure the place exists.
  - `user` (User): `User` instance of who wrote the review. Must be validated to ensure the user exists.
  - `created_at` (DateTime): Timestamp when the review is created.
  - `updated_at` (DateTime): Timestamp when the review is last updated.

- **Amenity Class:**

  - `id` (String): Unique identifier for each amenity.
  - `name` (String): The name of the amenity (e.g., "Wi-Fi", "Parking"). Required, maximum length of 50 characters.
  - `created_at` (DateTime): Timestamp when the amenity is created.
  - `updated_at` (DateTime): Timestamp when the amenity is last updated.

### Implementation Steps

1. **Implementing Classes, UUID, Created_at, and Updated_at Attributes**

    Each class should include:

    - A UUID identifier for each instance (`id = str(uuid.uuid4())`).
    - Timestamps for creation (`created_at`) and modification (`updated_at`).
    - The `created_at` timestamp should be set when an object is created, and the `updated_at` timestamp should be updated every time the object is modified.

    - Example base class for handling common attributes:

    ```python
    import uuid
    from datetime import datetime

    class BaseModel:
        def __init__(self):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        def save(self):
            """Update the updated_at timestamp whenever the object is modified"""
            self.updated_at = datetime.now()

        def update(self, data):
            """Update the attributes of the object based on the provided dictionary"""
            for key, value in data.items():
                if hasattr(self, key):
                    setattr(self, key, value)
            self.save()  # Update the updated_at timestamp
    ```

    - In this example we store the `UUID` generated as a `String` to avoid problems when retrieving from the Memory Repository.
    - Methods should be implemented to handle core operations, such as creating, updating, and retrieving instances. For instance, `save` methods to update timestamps and validate input data according to the constraints listed. The `update` method should allow updating object attributes based on a dictionary of new values.

    In the `models/` directory, implement the classes defined in your design:

    - `user.py`
    - `place.py`
    - `review.py`
    - `amenity.py`

    If you have created base classes in Part 1 (e.g., a base class for shared attributes like `id`, `created_at`, and `updated_at`), ensure that your entity classes inherit from them.

2. **Implement Relationships Between Entities**

    - Define relationships between the classes as follows:

    **User and Place:**

    - A `User` can own multiple `Place` instances (`one-to-many` relationship).
    - The `Place` class should include an attribute `owner`, referencing the `User` who owns it.

    **Place and Review:**

    - A `Place` can have multiple `Review` instances (`one-to-many` relationship).
    - The `Review` class should include attributes `place` and `user`, referencing the `Place` being reviewed and the `User` who wrote the review, respectively.

    **Place and Amenity:**

    - A `Place` can have multiple `Amenity` instances (`many-to-many` relationship).
    - This relationship can be represented using a list of amenities within the `Place` class. For simplicity, in-memory storage or a list of amenity IDs can be used.

    - Example of implementing relationships:

    ```python
    class Place(BaseModel):
        def __init__(self, title, description, price, latitude, longitude, owner):
            super().__init__()
            self.title = title
            self.description = description
            self.price = price
            self.latitude = latitude
            self.longitude = longitude
            self.owner = owner
            self.reviews = []  # List to store related reviews
            self.amenities = []  # List to store related amenities

        def add_review(self, review):
            """Add a review to the place."""
            self.reviews.append(review)

        def add_amenity(self, amenity):
            """Add an amenity to the place."""
            self.amenities.append(amenity)
    ```

    - Implement methods for managing these relationships, like adding a review to a place, or listing amenities associated with a place. Ensure that these operations validate the existence of related entities to maintain data integrity.

3. **Test the Core Classes Independently**

    Before moving on to the API implementation, write simple tests to validate that the classes are functioning as expected. Ensure that relationships between entities (e.g., adding a review to a place) work correctly.

   ### Example Tests

    Here’s a basic guide on how to test your implementation:

    **Testing the User Class**

    ```python
    from app.models.user import User

    def test_user_creation():
        user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
        assert user.first_name == "John"
        assert user.last_name == "Doe"
        assert user.email == "john.doe@example.com"
        assert user.is_admin is False  # Default value
        print("User creation test passed!")

    test_user_creation()
    ```

    **Testing the Place Class with Relationships**

    ```python
    from app.models.place import Place
    from app.models.user import User
    from app.models.review import Review

    def test_place_creation():
        owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com")
        place = Place(title="Cozy Apartment", description="A nice place to stay", price=100, latitude=37.7749, longitude=-122.4194, owner=owner)

        # Adding a review
        review = Review(text="Great stay!", rating=5, place=place, user=owner)
        place.add_review(review)

        assert place.title == "Cozy Apartment"
        assert place.price == 100
        assert len(place.reviews) == 1
        assert place.reviews[0].text == "Great stay!"
        print("Place creation and relationship test passed!")

    test_place_creation()
    ```

    **Testing the Amenity Class**

    ```python
    from app.models.amenity import Amenity

    def test_amenity_creation():
        amenity = Amenity(name="Wi-Fi")
        assert amenity.name == "Wi-Fi"
        print("Amenity creation test passed!")

    test_amenity_creation()
    ```

4. **Document the Implementation**
    - Update the `README.md` file to include information about the Business Logic layer, describing the entities and their responsibilities.
    - Include examples of how the classes and methods can be used.

## Expected Outcome

By the end of this task, you should have fully implemented core business logic classes (User, Place, Review, Amenity) with the appropriate attributes, methods, and relationships. With these components in place, you will be ready to proceed to implementing the API endpoints in the next task. The implemented classes should support the necessary validation, relationships, and data integrity checks required for the application’s core functionality. Additionally, the relationships between entities should be fully operational, allowing seamless interactions like linking reviews to places or associating amenities with places.

With this solid foundation in place, the business logic will be prepared for further integration with the Presentation and Persistence layers in subsequent tasks.

### Resources

- [**Python OOP Basics**](https://realpython.com/python3-object-oriented-programming/)
- [**Designing Classes and Relationships**](https://docs.python.org/3/tutorial/classes.html)
- [**Why You Should Use UUIDs**](https://datatracker.ietf.org/doc/html/rfc4122)
###### _________________________
# Implement the User Endpoints

## Context

This task involves setting up the endpoints to handle CRUD operations (Create, Read, Update) for users, while ensuring integration with the Business Logic layer via the Facade pattern. The `DELETE` operation will **not** be implemented for users in this part of the project.

The API interface, return format, and status codes must be clearly defined since it **must follow the standard RESTful API conventions**.

## Objective

In this task, the full implementation for user creation (POST) and retrieval (GET) by ID is provided as a guide. You will be responsible for implementing the retrieval of the list of users (GET /api/v1/users/) and updating user information (PUT /api/v1/users/<user_id>)

1. Set up the `POST`, `GET`, and `PUT` endpoints for managing users.
2. Implement the logic for handling user-related operations in the Business Logic layer.
3. Integrate the Presentation layer (API) and Business Logic layer through the Facade.

## Instructions: Detailed Guide to get you started

### Implement the Business Logic Layer

The Facade methods should be connected to the repository and models implemented in Task 2. Update `services/facade.py` with the following methods:

```python
class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
```

### Implement the User Endpoints in the Presentation Layer (API)

Create the `api/v1/users.py` file and include the following code:

```python
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user')
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload

        # Simulate email uniqueness check (to be replaced by real validation with persistence)
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        new_user = facade.create_user(user_data)
        return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email}, 201
```

- `POST /api/v1/users/`: Registers a new user and performs a check for email uniqueness.

**Explanation:**

- The `POST` endpoint registers a new user and performs a check for email uniqueness.
- If the email is already registered, the API returns a 400 status code with an error message.
- If input data is missing or invalid, a 400 status code is returned with a relevant error message **by the framework** thanks to the `validate=True` parameter.
- The Facade handles all interactions between layers.

### Implementation for User Retrieval by ID (GET /api/v1/users/<user_id>)

Continue in the `api/v1/users.py` file and include this additional code:

```python
@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200
```

- `GET /api/v1/users/<user_id>`: Retrieves user details by ID.

**Explanation:**

- The `GET` endpoint retrieves user details by ID.
- If the user does not exist, the API returns a 404 status code with an error message.

### Set Up the Namespace in `app/__init__.py`

Before implementing the endpoints, ensure that the users namespace is correctly registered in the application. Update the `app/__init__.py` file as follows:

```python
from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')

    # Register the users namespace
    api.add_namespace(users_ns, path='/api/v1/users')
    return app
```

This code registers the users namespace, allowing the routes defined in `api/v1/users.py` to be accessible through `/api/v1/users`.

Try running the application to ensure that the user registration and retrieval endpoints are working as expected.

## Input and Output Formats, Status Codes

Once the endpoints are implemented, use tools like Postman or cURL to test each operation.

For example, you can use the following cURL command to create a new user:

```bash
curl -X POST http://localhost:5000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -d '{"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"}'
```

or use the following cURL command to retrieve a user by ID:

```bash
curl -X GET http://localhost:5000/api/v1/users/<user_id>
```

For each endpoint, you must ensure that the input format, output format, and status codes are consistent and clearly defined:

### Test the Provided Endpoints

Ensure that the provided endpoints are working as expected:

#### Create a User (POST /api/v1/users/)

```http
POST /api/v1/users/
Content-Type: application/json

{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com"
}
```

Expected Response:

```jsonc
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com"
}

// 201 Created
```

Possible Status Codes:

- 201 Created: When the user is successfully created.
- 400 Bad Request: If the email is already registered or input data is invalid.

#### Retrieve a User by ID (GET /api/v1/users/<user_id>)

```http
GET /api/v1/users/<user_id>
Content-Type: application/json
```

Expected Response:

```jsonc
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@x.com"
}

// 200 OK
```

Possible Status Codes:

- `200 OK`: When the user is successfully retrieved.
- `404 Not Found`: If the user does not exist.

> Now you should have working services to create and retrieve users.

Complete the task by finishing the other endpoints for User management.

### Testing your endpoints

Ensure that your endpoints are working as expected. Here are some examples:

#### Retrieve a List of Users (GET /api/v1/users/)

```http
GET /api/v1/users/
Content-Type: application/json
```

Expected Response:

```jsonc
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com"
  },
  ...
]

// 200 OK
```

Possible Status Codes:

- `200 OK`: When the list of users is successfully retrieved.

#### Update a User (PUT /api/v1/users/<user_id>)

```http
PUT /api/v1/users/<user_id>
Content-Type: application/json

{
  "first_name": "Jane",
  "last_name": "Doe",
  "email": "jane.doe@example.com"
}
```

Expected Response:

```jsonc
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "first_name": "Jane",
  "last_name": "Doe",
  "email": "jane.doe@example.com"
}

// 200 OK
```

Possible Status Codes:

- 200 OK: When the user is successfully updated.
- 404 Not Found: If the user does not exist.
- 400 Bad Request: If input data is invalid.

## Sequence Diagram: Visualizing the Flow of User Registration

```mermaid
sequenceDiagram
    participant API
    participant Facade
    participant User

    API->>+Facade: create_user(user_data)
    Facade->>+User: create_instance(user_data)
    User-->>-Facade: user_instance
    Facade-->>-API: user_created_response
```

This diagram shows the interaction between the API, Facade, and Business Logic layer when registering a new user.

## Expected Outcome

By the end of this task, you should have fully implemented the core user management endpoints, including the ability to create, read, and update users. The provided implementation guide for the user registration endpoint should serve as a model for implementing the remaining user endpoints as well as endpoints for other entities (e.g., Place, Review, Amenity).

The functionality should be documented and tested, ensuring that all user-related operations are handled smoothly within the HBnB application.

## Resources

1. [**Flask-RESTx Documentation**](https://flask-restx.readthedocs.io/)
2. [**Testing REST APIs with cURL**](https://everything.curl.dev/)
3. [**Designing RESTful APIs**](https://restfulapi.net/)
###### _________________________
# Implement the Amenity Endpoints

## Context

This task involves setting up the endpoints to handle CRUD operations (Create, Read, Update) for amenities, while ensuring integration with the Business Logic layer via the Facade pattern. The `DELETE` operation will **not** be implemented for amenities in this part of the project.

## In this task, you will

1. Set up the `POST`, `GET`, and `PUT` endpoints for managing amenities.
2. Implement the necessary logic for handling amenity-related operations in the Business Logic layer.
3. Integrate the Presentation layer (API) and Business Logic layer through the Facade.

## Instructions: Detailed Guide to get you started

### Implement the Business Logic Layer

In the `models/amenity.py` file, the `Amenity` class should have already been implemented in Task 2.

Update the `HBnBFacade` class in the `services/facade.py` file, adding the following methods:

```python
def create_amenity(self, amenity_data):
    # Placeholder for logic to create an amenity
    pass

def get_amenity(self, amenity_id):
    # Placeholder for logic to retrieve an amenity by ID
    pass

def get_all_amenities(self):
    # Placeholder for logic to retrieve all amenities
    pass

def update_amenity(self, amenity_id, amenity_data):
    # Placeholder for logic to update an amenity
    pass
```

These methods manage the creation, retrieval, and updating of amenities within the Business Logic layer. You will need to fill in the logic that handles interactions with the repository and implements necessary validation.

### Implement the Amenity Endpoints in the Presentation Layer (API)

Create the `api/v1/amenities.py` file, then define the routes and create the skeleton methods for these endpoints. Use the placeholders provided below to get started.

```python
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        # Placeholder for the logic to register a new amenity
        pass

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        # Placeholder for logic to return a list of all amenities
        pass

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        # Placeholder for the logic to retrieve an amenity by ID
        pass

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        # Placeholder for the logic to update an amenity by ID
        pass
```

- `POST /api/v1/amenities/`: Register a new amenity.
- `GET /api/v1/amenities/`: Retrieve a list of all amenities.
- `GET /api/v1/amenities/<amenity_id>`: Get amenity details by ID.
- `PUT /api/v1/amenities/<amenity_id>`: Update an amenity's information.

**Explanation:**

- The `POST` endpoint handles the creation of a new amenity, while the `GET` endpoints manage retrieval, both for a single amenity and a list of all amenities. The `PUT` endpoint is responsible for updating an existing amenity’s details.
- The placeholders give you a foundation to build on, while you will need to implement the logic based on previous examples like the user registration task.

> [!IMPORTANT]
> **Remember to register the namespace and API documentation for the amenity endpoints in the `api/__init__.py` file.**

## Input and Output Formats, Status Codes

For each endpoint, ensure that the input format, output format, and status codes are consistent and clearly defined.

### Test the Provided Endpoints

Once the endpoints are implemented, use tools like Postman or cURL to test each operation.
Ensure that your endpoints are working as expected. Here are some examples:

#### Register a New Amenity (POST /api/v1/amenities/)

```http
POST /api/v1/amenities/
Content-Type: application/json

{
  "name": "Wi-Fi"
}
```

Expected Response:

```jsonc
{
  "id": "1fa85f64-5717-4562-b3fc-2c963f66afa6",
  "name": "Wi-Fi"
}

// 201 Created
```

Possible Status Codes:

- 201 Created: When the amenity is successfully created.
- 400 Bad Request: If input data is invalid.

#### Retrieve All Amenities (GET /api/v1/amenities/)

```http
GET /api/v1/amenities/
Content-Type: application/json
```

Expected Response:

```jsonc
[
  {
    "id": "1fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "Wi-Fi"
  },
  {
    "id": "2fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "Air Conditioning"
  }
]

// 200 OK
```

Possible Status Codes:

- 200 OK: List of amenities retrieved successfully.

#### Retrieve an Amenity’s Details (GET /api/v1/amenities/<amenity_id>)

```http
GET /api/v1/amenities/<amenity_id>
Content-Type: application/json
```

Expected Response:

```jsonc
{
  "id": "1fa85f64-5717-4562-b3fc-2c963f66afa6",
  "name": "Wi-Fi"
}

// 200 OK
```

Possible Status Codes:

- 200 OK: When the amenity is successfully retrieved.
- 404 Not Found: If the amenity does not exist.

#### Update an Amenity’s Information (PUT /api/v1/amenities/<amenity_id>)

```http
PUT /api/v1/amenities/<amenity_id>
Content-Type: application/json

{
  "name": "Air Conditioning"
}
```

Expected Response:

```jsonc
{
  "message": "Amenity updated successfully"
}

// 200 OK
```

Possible Status Codes:

- 200 OK: When the amenity is successfully updated.
- 404 Not Found: If the amenity does not exist.
- 400 Bad Request: If input data is invalid.

## Expected Outcome

By the end of this task, you should have fully implemented the core amenity management endpoints, including the ability to create, read, and update amenities. The functionality should be documented and tested, ensuring that all amenity-related operations are handled smoothly within the HBnB application.

## Resources

- [**Flask-RESTx Documentation**](https://flask-restx.readthedocs.io/)
- [**Testing REST APIs with cURL**](https://everything.curl.dev/)
- [**Designing RESTful APIs**](https://restfulapi.net/)
###### _________________________
Implement the Place Endpoints
Context
This task involves setting up the endpoints to handle CRUD operations (Create, Read, Update) for places, while ensuring integration with the Business Logic layer via the Facade pattern. The DELETE operation will not be implemented for places in this part of the project.

Given that the Place entity has relationships with other entities, such as User (owner) and Amenity, you’ll need to handle these relationships carefully while maintaining the integrity of the application logic.

The Review entity will be implemented in the next task, so it should not be included in this task.

In this task, you will
Set up the POST, GET, and PUT endpoints for managing places.
Implement the logic for handling place-related operations in the Business Logic layer.
Integrate the Presentation layer (API) and Business Logic layer through the Facade.
Implement validation for specific attributes like price, latitude, and longitude.
Ensure that related data such as owner details and amenities are properly handled and returned with the Place data.
Instructions
Implement the Place Management Logic in the Business Logic Layer
In the models/place.py file, the Place class should have already been implemented in Task 2, ensure that the class handles relationships with other entities and performs attribute validation.

Update the HBnBFacade class in the services/facade.py file, adding the following methods:

def create_place(self, place_data):
    # Placeholder for logic to create a place, including validation for price, latitude, and longitude
    pass

def get_place(self, place_id):
    # Placeholder for logic to retrieve a place by ID, including associated owner and amenities
    pass

def get_all_places(self):
    # Placeholder for logic to retrieve all places
    pass

def update_place(self, place_id, place_data):
    # Placeholder for logic to update a place
    pass
These methods handle place creation, retrieval, and updates. Consider using custom setter methods or raising exceptions to handle invalid data.

Validation of Place Attributes
When implementing validation for attributes like price, latitude, and longitude, consider the following:

price should be a non-negative float.
latitude should be between -90 and 90.
longitude should be between -180 and 180.
Implement these validations using property setters in the Place class, raising appropriate exceptions for invalid values.

Implement the Place Endpoints in the Presentation Layer (API)
Create the api/v1/places.py file, then define the routes and create the skeleton methods for these endpoints. Use the placeholders provided below to get started.

from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        # Placeholder for the logic to register a new place
        pass

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        # Placeholder for logic to return a list of all places
        pass

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        # Placeholder for the logic to retrieve a place by ID, including associated owner and amenities
        pass

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        # Placeholder for the logic to update a place by ID
        pass
POST /api/v1/places/: Register a new place.
GET /api/v1/places/: Return a list of all places.
GET /api/v1/places/<place_id>: Retrieve details of a specific place, including its associated owner and amenities.
PUT /api/v1/places/<place_id>: Update place information.
Explanation:

The POST endpoint registers a new place, while GET and PUT manage place retrieval and updates. The GET /api/v1/places/<place_id> endpoint includes associated owner and amenities for the place.
You are responsible for implementing the logic for handling relationships between places, owners, and amenities.
Important

Remember to register the namespace and API documentation for the amenity endpoints in the api/__init__.py file.

Input and Output Formats, Status Codes
For each endpoint, ensure that the input format, output format, and status codes are consistent and clearly defined.

Test the Provided Endpoints
Once the endpoints are implemented, use tools like Postman or cURL to test each operation. Ensure that your endpoints are working as expected. Here are some examples:

Register a New Place (POST /api/v1/places/)
POST /api/v1/places/
Content-Type: application/json

{
  "title": "Cozy Apartment",
  "description": "A nice place to stay",
  "price": 100.0,
  "latitude": 37.7749,
  "longitude": -122.4194,
  "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
Expected Response:

{
  "id": "1fa85f64-5717-4562-b3fc-2c963f66afa6",
  "title": "Cozy Apartment",
  "description": "A nice place to stay",
  "price": 100.0,
  "latitude": 37.7749,
  "longitude": -122.4194,
  "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}

// 201 Created
Possible Status Codes:

201 Created: When the place is successfully created.
400 Bad Request: If input data is invalid.
Retrieve All Places (GET /api/v1/places/)
GET /api/v1/places/
Content-Type: application/json
Expected Response:

[
  {
    "id": "1fa85f64-5717-4562-b3fc-2c963f66afa6",
    "title": "Cozy Apartment",
    "latitude": 37.7749,
    "longitude": -122.4194
  },
  ...
]

// 200 OK
Possible Status Codes:

200 OK: List of places retrieved successfully.
Retrieve Place Details (GET /api/v1/places/<place_id>)
GET /api/v1/places/<place_id>
Content-Type: application/json
Expected Response:

{
  "id": "1fa85f64-5717-4562-b3fc-2c963f66afa6",
  "title": "Cozy Apartment",
  "description": "A nice place to stay",
  "latitude": 37.7749,
  "longitude": -122.4194,
  "owner": {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com"
  },
  "amenities": [
    {
      "id": "4fa85f64-5717-4562-b3fc-2c963f66afa6",
      "name": "Wi-Fi"
    },
    {
      "id": "5fa85f64-5717-4562-b3fc-2c963f66afa6",
      "name": "Air Conditioning"
    }
  ]
}

// 200 OK
Possible Status Codes:

200 OK: When the place and its associated owner and amenities are successfully retrieved.
404 Not Found: If the place does not exist.
Update a Place’s Information (PUT /api/v1/places/<place_id>)
PUT /api/v1/places/<place_id>
Content-Type: application/json

{
  "title": "Luxury Condo",
  "description": "An upscale place to stay",
  "price": 200.0
}
Expected Response:

{
  "message": "Place updated successfully"
}

// 200 OK
Possible Status Codes:

200 OK: When the place is successfully updated.
404 Not Found: If the place does not exist.
400 Bad Request: If input data is invalid.
Expected Outcome
By the end of this task, you should have implemented the core place management endpoints, including the ability to create, read, and update places. You will have handled the relationships between places, owners, and amenities, including validating specific attributes like price, latitude, and longitude. The functionality should be documented and tested, ensuring smooth operation within the HBnB application.

Resources
Flask-RESTx Documentation
Testing REST APIs with cURL
Designing RESTful APIs
###### _________________________
# Implement the Review Endpoints

## Context

This task involves setting up the endpoints to handle CRUD operations (Create, Read, Update) for reviews, while ensuring integration with the Business Logic layer via the Facade pattern.

The `DELETE` operation **will be implemented** for reviews, making it the only entity for which deletion is supported in this part of the project.

## In this task, you will

1. Set up the `POST`, `GET`, `PUT`, and `DELETE` endpoints for managing reviews.
2. Implement the logic for handling review-related operations in the Business Logic layer.
3. Integrate the Presentation layer (API) and Business Logic layer through the Facade.
4. Implement validation for specific attributes like the text and rating of the review, and ensure that the review is associated with both a user and a place.
5. Update the Place model in `api/v1/places.py` to consider the collection of reviews for a place.

## Instructions

### Implement the Review Management Logic in the Business Logic Layer

In the `models/review.py` file, the `Review` class should already be implemented from Task 2. Ensure that the class can handle relationships with users and places.

Update the `HBnBFacade` class in the `services/facade.py` file, adding the following methods:

```python
def create_review(self, review_data):
    # Placeholder for logic to create a review, including validation for user_id, place_id, and rating
    pass

def get_review(self, review_id):
    # Placeholder for logic to retrieve a review by ID
    pass

def get_all_reviews(self):
    # Placeholder for logic to retrieve all reviews
    pass

def get_reviews_by_place(self, place_id):
    # Placeholder for logic to retrieve all reviews for a specific place
    pass

def update_review(self, review_id, review_data):
    # Placeholder for logic to update a review
    pass

def delete_review(self, review_id):
    # Placeholder for logic to delete a review
    pass
```

These methods manage review creation, retrieval, updates, and deletion. You need to implement validation to ensure that the `user_id`, `place_id`, and `rating` are valid and correspond to existing users and places.

### Implement the Review Endpoints in the Presentation Layer (API)

Create the `api/v1/reviews.py` file, then define the routes and create the skeleton methods for these endpoints. Use the placeholders provided below to get started.

```python
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        # Placeholder for the logic to register a new review
        pass

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        # Placeholder for logic to return a list of all reviews
        pass

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        # Placeholder for the logic to retrieve a review by ID
        pass

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """Update a review's information"""
        # Placeholder for the logic to update a review by ID
        pass

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        # Placeholder for the logic to delete a review
        pass

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        # Placeholder for logic to return a list of reviews for a place
        pass
```

- `POST /api/v1/reviews/`: Register a new review.
- `GET /api/v1/reviews/`: Return a list of all reviews.
- `GET /api/v1/reviews/<review_id>`: Retrieve details of a specific review.
- `GET /api/v1/places/<place_id>/reviews`: Retrieve all reviews for a specific place.
- `PUT /api/v1/reviews/<review_id>`: Update a review’s information.
- `DELETE /api/v1/reviews/<review_id>`: Delete a review.

**Explanation:**

- The `POST` endpoint handles the creation of a new review, while `GET`, `PUT`, and `DELETE` endpoints manage review retrieval, updates, and deletion.
- The `GET /api/v1/places/<place_id>/reviews` endpoint is specific to retrieving all reviews associated with a particular place.
- Placeholders are provided, but you need to implement the logic that handles relationships between reviews, users, and places.

> [!IMPORTANT]
> **Remember to register the namespace and API documentation for the amenity endpoints in the `api/__init__.py` file.**

### Update the Place Model to Include Reviews

In the `api/v1/places.py` file, update the `place_model` to include the collection of reviews for a place. This ensures that when retrieving place details, all associated reviews are included.

**Updated Place Model:**

```python
# Adding the review model
review_model = api.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the place (1-5)'),
    'user_id': fields.String(description='ID of the user')
})

place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'owner': fields.Nested(user_model, description='Owner of the place'),
    'amenities': fields.List(fields.Nested(amenity_model), description='List of amenities'),
    'reviews': fields.List(fields.Nested(review_model), description='List of reviews')
})
   ```

## Input and Output Formats, Status Codes

For each endpoint, ensure that the input format, output format, and status codes are consistent and clearly defined.

### Test the Provided Endpoints

Once the endpoints are implemented, use tools like Postman or cURL to test each operation.
Ensure that your endpoints are working as expected. Here are some examples:

#### Register a New Review (POST /api/v1/reviews/)

```http
POST /api/v1/reviews/
Content-Type: application/json

{
  "text": "Great place to stay!",
  "rating": 5,
  "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "place_id": "1fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

Expected Response:

```jsonc
{
  "id": "2fa85f64-5717-4562-b3fc-2c963f66afa6",
  "text": "Great place to stay!",
  "rating": 5,
  "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "place_id": "1fa85f64-5717-4562-b3fc-2c963f66afa6"
}

// 201 Created
```

Possible Status Codes:

- 201 Created: When the review is successfully created.
- 400 Bad Request: If input data is invalid.

#### Retrieve All Reviews (GET /api/v1/reviews/)

```http
GET /api/v1/reviews/
```

Expected Response:

```jsonc
[
  {
    "id": "2fa85f64-5717-4562-b3fc-2c963f66afa6",
    "text": "Great place to stay!",
    "rating": 5
  },
  ...
]

// 200 OK
```

Possible Status Codes:

- 200 OK: List of reviews retrieved successfully.

#### Retrieve a Review’s Details (GET /api/v1/reviews/<review_id>)

```http
GET /api/v1/reviews/<review_id>
```

Expected Response:

```jsonc
{
  "id": "2fa85f64-5717-4562-b3fc-2c963f66afa6",
  "text": "Great place to stay!",
  "rating": 5,
  "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "place_id": "1fa85f64-5717-4562-b3fc-2c963f66afa6"
}

// 200 OK
```

Possible Status Codes:

- 200 OK: When the review is successfully retrieved.
- 404 Not Found: If the review does not exist.

#### Update a Review’s Information (PUT /api/v1/reviews/<review_id>)

```http
PUT /api/v1/reviews/<review_id>
Content-Type: application/json

{
  "text": "Amazing stay!",
  "rating": 4
}
```

Expected Response:

```jsonc
{
  "message": "Review updated successfully"
}

// 200 OK
```

Possible Status Codes:

- 200 OK: When the review is successfully updated.
- 404 Not Found: If the review does not exist.
- 400 Bad Request: If input data is invalid.

#### Delete a Review (DELETE /api/v1/reviews/<review_id>)

```http
DELETE /api/v1/reviews/<review_id>
```

Expected Response:

```jsonc
{
  "message": "Review deleted successfully"
}

// 200 OK
```

Possible Status Codes:

- 200 OK: When the review is successfully deleted.
- 404 Not Found: If the review does not exist.

#### Retrieve All Reviews for a Specific Place (GET /api/v1/places/<place_id>/reviews)

```http
GET /api/v1/places/<place_id>/reviews
```

Expected Response:

```jsonc
[
  {
    "id": "2fa85f64-5717-4562-b3fc-2c963f66afa6",
    "text": "Great place to stay!",
    "rating": 5
  },
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "text": "Very comfortable and clean.",
    "rating": 4
  }
]

// 200 OK
```

Possible Status Codes:

- 200 OK: List of reviews for the place retrieved successfully.
- 404 Not Found: If the place does not exist.

## Expected Outcome

By the end of this task, you should have implemented the core review management endpoints, including the ability to create, read, update, and delete reviews. Additionally, you will have implemented the ability to retrieve all reviews associated with a specific place. The functionality should be documented and tested, ensuring that all review-related operations are handled smoothly within the HBnB application.

## Resources

- [**Flask-RESTx Documentation**](https://flask-restx.readthedocs.io/)
- [**Testing REST APIs with cURL**](https://everything.curl.dev/)
- [**Designing RESTful APIs**](https://restfulapi.net/)
###### _________________________
# Implement Testing and Validation of the Endpoints

## Objective

This task involves creating and running tests for the endpoints you have developed so far. You will implement validation logic, perform thorough testing using `cURL`, and document the results of those tests. The focus is on ensuring that each endpoint works as expected and adheres to the input/output formats, status codes, and validation rules you have defined in previous tasks.

## In this task, you will

1. Implement basic validation checks for each of the attributes in your endpoints.
2. Perform black-box testing using `cURL` and the Swagger documentation generated by Flask-RESTx.
3. Create a detailed testing report, highlighting both successful and failed cases.

## Instructions

### Implement Basic Validation in the Business Logic Layer

For this task, you should revisit each of the entity models (`User`, `Place`, `Review`, `Amenity`) and ensure that basic validation is performed at the model level. Here are a few key validations to implement:

- **User:**
  - Ensure that the `first_name`, `last_name`, and `email` attributes are not empty.
  - Ensure that the `email` is in a valid email format.

- **Place:**
  - Ensure that `title` is not empty.
  - Ensure that `price` is a positive number.
  - Ensure that `latitude` is between -90 and 90.
  - Ensure that `longitude` is between -180 and 180.

- **Review:**
  - Ensure that `text` is not empty.
  - Ensure that `user_id` and `place_id` reference valid entities.

### Testing the Endpoints Using cURL

Once you have implemented the necessary validation, you should perform tests using `cURL`. Below are some examples of how to test different scenarios:

#### Testing the Creation of a User

```bash
curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com"
}'
```

**Expected Response:**

```jsonc
{
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com"
}

// 200 OK
```

#### Testing Invalid Data for a User

```bash
curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{
    "first_name": "",
    "last_name": "",
    "email": "invalid-email"
}'
```

**Expected Response:**

```json
{
    "error": "Invalid input data"
}

// 400 Bad Request
```

You should repeat similar tests for other entities and endpoints, focusing on:

- **Boundary Testing** (e.g., out-of-range latitude/longitude).
- **Required Fields** (e.g., missing or empty values).
- **Error Handling** (e.g., retrieving a non-existent resource).

### **Generate Swagger Documentation**

Since Flask-RESTx automatically generates Swagger documentation based on your API models, you should review this documentation to ensure it accurately reflects your endpoints. To access the Swagger documentation, visit:

```text
http://127.0.0.1:5000/api/v1/
```

Use this documentation as a reference when performing manual tests or writing automated tests.

### **Write and Run Unit Tests**

In addition to manual tests, you should write automated unit tests using Python’s `unittest` or `pytest` frameworks. Here’s a basic example of how to structure your tests:

```python
import unittest
from app import create_app

class TestUserEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_user_invalid_data(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "",
            "email": "invalid-email"
        })
        self.assertEqual(response.status_code, 400)
```

These tests should cover both positive and negative scenarios for all endpoints.

### Document the Testing Process

As you perform your tests, keep a log of:

- The endpoints tested.
- The input data used.
- The expected output vs. the actual output.
- Any issues encountered.

This documentation will be essential when you present your results and demonstrate that your implementation meets all the requirements.

## Expected Outcome

By the end of this task, you should have:

- Implemented basic validation for all entity models.
- Performed thorough testing using cURL and other tools.
- Generated Swagger documentation to confirm that your API is correctly described.
- Created and executed unit tests using `unittest` or `pytest`.
- Documented the testing process, highlighting both successful cases and edge cases that were handled correctly.


###### _________________________
###### _________________________
###### _________________________


```plaintext
██╗  ██╗██████╗ ███╗   ██╗██████╗
██║  ██║██╔══██╗████╗  ██║██╔══██╗
███████║███████║██╔██╗ ██║███████║
██╔══██║██║  ██║██║╚██╗██║██║  ██║
██║  ██║██████╔╝██║ ╚████║██████╔╝
╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝╚═════╝
 | HBnB Logo  # C24
'''

```plaintext
<!-- #                     '-.,;;:;,
                      _;\;|\;:;,
                     ) __ ' \;::,
                 .--'  e   ':;;;:,           ;,
                (^           ;;::;          ;;;,
        _        --_.--.___,',:;::;     ,,,;:;;;,
       < \        `;     |  ;:;;:;        ':;:;;;,,
     <`-; \__     ,;    /    ';:;;:,       ';;;'
     <`_   __',   ; ,  /    ::;;;:         //
        `)|  \ \   ` .'      ';;:;,       //
         `    \ `\  /        ;;:;;.      //__
               \  `/`         ;:;  ~._,=~`   `~=,
                \_|      (        ^     ^  ^ _^  \
                  \    _,`      / ^ ^  ^   .' `.^ ;
         <`-.  #C24 '-;`       /`  ^   ^  /\    ) ^/
         <'- \__..-'` ___,,,-'._ ^  ^ _.'\^`'-' ^/
          `)_   ..-''`          `~~~~`    `~===~`
          <_.-`-._\ -->
'''
