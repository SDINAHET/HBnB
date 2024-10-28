# Task0: Package Diagram
```mermaid
classDiagram
	class PresentationLayer {
		<<Interface>>
		+ServiceAPI
		+WebService
	}

	class BusinessLogicLayer {
		+User
		+Place
		+Review
		+Amenity
	}

	class PersistenceLayer {
		+DatabaseManager
		+Database JSON
		+Queries
	}

	PresentationLayer --> BusinessLogicLayer : Facade Pattern
	BusinessLogicLayer --> PersistenceLayer : Database Operations
```


# Task1: Class Diagram
```mermaid
classDiagram
     %% Classe de Base pour les Entités
    class BaseEntity {
        - UUID4 ID: String
        - createdAt: DateTime
        - updatedAt: DateTime
        + getId() String
        + getCreatedAt() DateTime
        + getUpdatedAt() DateTime
    }

    %% Classe User héritant de BaseEntity
    class User {
        - firstName: String
        - lastName: String
        - email: String
        - password: String
        - isAdmin: Boolean
        + registerProfile() Void
        + updateProfile() Void
        + deleteProfile() Void
    }

    %% Classe Place héritant de BaseEntity
    class Place {
        - title: String
        - description: String
        - price: Float
        - latitude: Float
        - longitude: Float
        - amenities: List<Amenity>
        - owner: User
        + createPlace() Void
        + updatePlace() Void
        + deletePlace() Void
        + listPlaces() List<Place>
    }

    %% Classe Review héritant de BaseEntity
    class Review {
        - rating: Int
        - comment: String
        + createReview() Void
        + deleteReview() Void
        + listReviewsByPlace() List<Review>
    }

    %% Classe Amenity héritant de BaseEntity
    class Amenity {
        - name: String
        - description: String
        + createAmenity() Void
        + updateAmenity() Void
        + deleteAmenity() Void
        + listAmenities() List<Amenity>
    }

    %% Relations d'Héritage
    BaseEntity <|-- User
    BaseEntity <|-- Place
    BaseEntity <|-- Review
    BaseEntity <|-- Amenity

    %% Relations entre les Entités
    User "1" -- "0..*" Place : owns
    User "1" -- "0..*" Review : writes
    Place "1" o-- "0..*" Review : receives
    Place "1" o-- "0..*" Amenity : has
```


# Task2: Sequence Diagrams
## 1. User Registration Sequence Diagram
```mermaid
sequenceDiagram
	participant User
	participant API
	participant BusinessLogic
	participant Persistence

	User->>API: Create User
	API->>BusinessLogic: Validate User Data
	BusinessLogic->>Persistence: Save User
	Persistence-->>BusinessLogic: Return Success
	BusinessLogic-->>API: Return User Info
	API-->>User: User Created
```

## 2. Place Creation Sequence Diagram
```mermaid
sequenceDiagram
	participant User
	participant API
	participant BusinessLogic
	participant Persistence

	User->>API: Create Place
	API->>BusinessLogic: Validate Place Data
	BusinessLogic->>Persistence: Save Place
	Persistence-->>BusinessLogic: Return Success
	BusinessLogic-->>API: Return Place Info
	API-->>User: Place Created
```
## 3. Review Submission Sequence Diagram
```mermaid
sequenceDiagram
	participant User
	participant API
	participant BusinessLogic
	participant Persistence

	User->>API: Add Review
	API->>BusinessLogic: Validate Review Data
	BusinessLogic->>Persistence: Save Review
	Persistence-->>BusinessLogic: Return Success
	BusinessLogic-->>API: Return Review Info
	API-->>User: Review Added
```
## 4. Fetching a List of Places Sequence Diagram
```mermaid
sequenceDiagram
	participant User
	participant API
	participant BusinessLogic
	participant Persistence

	User->>API: Fetch Places
	API->>BusinessLogic: Validate Request
	BusinessLogic->>Persistence: Retrieve Places
	Persistence-->>BusinessLogic: Return List
	BusinessLogic-->>API: Return List
	API-->>User: List of Places
```
