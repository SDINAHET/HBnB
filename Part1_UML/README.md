# Package Diagram
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


# Class Diagram
```mermaid
classDiagram
    class User {
        - UUID4 ID: String
        - First_name: String
        - Last_name: String
        - Email: String
        - Password: String
        - Is_admin: Boolean
        - DateTime created_at: String
        - DateTime updated_at: String
        + getUUID4() ID
        + getCreatedAt() datetime
        + getUpdatedAt() datetime
        + register_profile()
        + update_profile()
        + delete_profile()
    }

    class Place {
        - UUID4 ID: String
        - Title: String
        - Description: String
        - Price: Float
        - Latitude: Float
        - Longitude: Float
        - DateTime created_at: String
        - DateTime updated_at: String
        + getUUID4() ID
        + getCreatedAt() datetime
        + getUpdatedAt() datetime
        + created_place()
        + updated_place()
        + deleted_place()
		+ list_place()
    }

    class Review {
        - UUID4 ID: String
        - Rating: Int
        - Comment: String
        - DateTime created_at: String
        - DateTime updated_at: String
        + getUUID4() ID
        + getCreatedAt() datetime
        + getUpdatedAt() datetime
        + created_review()
        + deleted_review()
        + listed_by_place_review()
    }

    class Amenity {
        - UUID4 ID: String
        - Name: String
        - Description: String
        - DateTime created_at: String
        - DateTime updated_at: String
        + getUUID4() ID
        + getCreatedAt() datetime
        + getUpdatedAt() datetime
        + created_amenity()
        + updated_amenity()
        + deleted_amenity()
        + listed_amenity()
    }

    User "1" -- "*" Place : owns
    User "1" -- "*" Review : update
    Place "1" -- "*" Review : receives
    Place "1" o-- "*" Amenity : has
```


# Sequence Diagrams
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
