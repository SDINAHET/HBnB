
# HBnB Project

This project is a Flask-based RESTful API for managing users, places, reviews, and amenities.

## Project Structure

- **app/**: Contains the main application code.
  - **api/**: API endpoints organized by version.
  - **models/**: Business logic classes (User, Place, Review, Amenity).
  - **services/**: Facade for managing interaction between layers.
  - **persistence/**: In-memory storage (will be replaced with a database layer).
- **run.py**: Entry point for the application.
- **config.py**: Configuration for environment variables.
- **requirements.txt**: Required Python packages.
    