# HBnB - Part 3: Authentication and Database

## Project Overview

This part of the HBnB project focuses on adding authentication to the web application, using JWT tokens, along with improving the data storage solution using repositories and implementing database management. The goal is to create a secure, scalable system that enables authenticated users to perform specific actions, such as creating, updating, and managing entities like users, places, amenities, and reviews.

### Key Features

- **JWT Authentication**: Secure endpoints using JWT tokens to ensure only authenticated users can access certain functionalities.
- **RESTful API**: Implemented using Flask and Flask-RESTx, providing a structured and easy-to-use interface for managing the HBnB application.
- **Repository Pattern**: Introduced to abstract and encapsulate data access, promoting loose coupling between the application and data storage.
- **Business Logic Layer**: Centralized in the `facade.py` file to ensure that all API requests are processed consistently, regardless of the route they come from.
- **CRUD Operations**: Enabled for users, places, amenities, and reviews.

## Project Structure

Below is the directory structure of the project:

```
HBnB/
    ├── app/
    │   ├── __init__.py
    │   ├── api/
    │   │   ├── __init__.py
    │   │   ├── v1/
    │   │       ├── __init__.py
    │   │       ├── auth.py
    │   │       ├── protected.py
    │   │       ├── places.py
    │   │       ├── reviews.py
    │   │       ├── users.py
    │   │       ├── amenities.py
    │   ├── models/
    │   │   ├── __init__.py
    │   │   ├── base_entity.py
    │   │   ├── amenity.py
    │   │   ├── place.py
    │   │   ├── review.py
    │   │   ├── user.py
    │   ├── services/
    │   │   ├── __init__.py
    │   │   ├── facade.py
    │   ├── persistence/
    │   │   ├── __init__.py
    │   │   ├── repository.py
    ├── config.py
    ├── requirements.txt
    ├── run.py
    ├── README.md
```

## Configuration

The `config.py` file defines the configuration classes for different environments, such as Development and Production. The configuration is used to manage settings like `SECRET_KEY` for JWT and database connection strings.

The Flask application is instantiated in the `create_app()` method inside `app/__init__.py`, which initializes the application using the selected configuration.

## Authentication

JWT (JSON Web Token) authentication is implemented using `flask-jwt-extended` to provide secure access to protected endpoints. Tokens are issued upon successful login, and users must provide their token as a `Bearer` token in the Authorization header to access protected routes.

### Key Authentication Endpoints

- **POST /api/v1/auth/login**: Login user and issue JWT.
- **GET /api/v1/protected**: Example protected endpoint requiring a valid JWT token.

## Endpoints

### User Endpoints
- **POST /api/v1/users**: Register a new user.
- **PUT /api/v1/users/<user_id>**: Update user details (self only).
- **GET /api/v1/users/<user_id>**: Retrieve user details.

### Place Endpoints
- **POST /api/v1/places**: Create a new place.
- **PUT /api/v1/places/<place_id>**: Update a place (owner only).
- **GET /api/v1/places**: Retrieve all places.
- **GET /api/v1/places/<place_id>**: Retrieve details of a specific place.

### Review Endpoints
- **POST /api/v1/reviews**: Create a new review (cannot review owned places).
- **PUT /api/v1/reviews/<review_id>**: Update a review (author only).
- **DELETE /api/v1/reviews/<review_id>**: Delete a review (author only).

### Amenity Endpoints
- **POST /api/v1/amenities**: Register a new amenity.
- **PUT /api/v1/amenities/<amenity_id>**: Update amenity details.
- **GET /api/v1/amenities**: Retrieve all amenities.

## Testing

### Unit Testing

Unit tests for the API are implemented using `unittest` and `pytest` frameworks. Tests cover success and failure scenarios for all CRUD operations and authentication workflows.

### GitHub Actions

GitHub Actions is configured to run the test suite automatically on each push. The workflow configuration ensures that the project stays functional during ongoing development.

### How to Run Tests

1. **Run Unit Tests**:
   ```
   pytest tests/
   ```
2. **Run All Tests with Coverage**:
   ```
   pytest --cov=app tests/
   ```
3. **Generate Allure Report**:
   - Install Allure:
     ```
     sudo apt install allure
     ```
   - Run tests with Allure:
     ```
     pytest --alluredir=allure-results
     ```
   - Serve the report:
     ```
     allure serve allure-results
     ```

## Running the Application

### Installation

1. **Clone the Repository**:
   ```
   git clone <repository-url>
   cd HBnB
   ```

2. **Set Up a Virtual Environment**:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

### Start the Server

1. **Run the Application**:
   ```
   python run.py
   ```

2. **Access the API Documentation**: Open `http://127.0.0.1:5000/` in your browser to view Swagger UI for the available endpoints.

### Environment Variables

- **JWT_SECRET_KEY**: Set this for JWT signing and verification.
- **FLASK_ENV**: Set to `development` or `production` to control configurations.

## Contribution

Feel free to fork the repository and submit a pull request. All contributions are welcomed. Make sure to run tests before submitting changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

