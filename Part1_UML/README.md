#Package Diagram
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


#Class Diagram
```mermaid
classDiagram
	class User {
		 - String first_name
		- String last_name
		- String email
		- String password
		+ register()
		+ update_profile()
	}
	class Place {
		- String title
		- String description
		- float price
		- float latitude
		- float longitude
		+ create_place()
		+ update_place()
		+ delete_place()
	}
	class Review {
		 - int rating
		- String comment
		+ create_review()
		+ delete_review()
	}
	class Amenity {
		- String name
		- String description
	}
	User "1" -- "*" Place : owns
	Place "1" -- "*" Review : receives
	Place "1" -- "*" Amenity : has
```

#correction Class Diagram
```mermaid
classDiagram
    class User {
        - string UUID4 id
        - String first_name
        - String last_name
        - String email
        - String password
        - boolean is_admin
        - String DateTime created_at
        - String DateTime updated_at
        + getUUID4(): ID
        + getCreatedAt(): datetime
        + getUpdatedAt(): datetime
        + register_profile()
        + update_profile()
		+delete_profile()
    }

    class Place {
        - String UUID4 id
        - String title
        - String description
        - float price
        - float latitude
        - float longitude
        - String DateTime created_at
        - String DateTime updated_at
        + getUUID4(): ID
        + getCreatedAt(): datetime
        + getUpdatedAt(): datetime
        + create_place()
        + update_place()
        + delete_place()
    }

    class Review {
        - String UUID4 id
        - int rating
        - String comment
        - String DateTime created_at
        - String DateTime updated_at
        + getUUID4(): ID
        + getCreatedAt(): datetime
        + getUpdatedAt(): datetime
        + create_review()
        + delete_review()
    }

    class Amenity {
        - String UUID4 id
        - String name
        - String description
        - String DateTime created_at
        - String DateTime updated_at
        + getUUID4(): ID
        + getCreatedAt(): datetime
        + getUpdatedAt(): datetime
    }

    User "1" -- "*" Place : owns
    User "1" -- "*" review : update
    Place "1" -- "*" Review : receives
    Place "1" -- "*" Amenity : has
    Place->>Amenity: addAmenity(name, description)
    Note over Place: Place can have multiple Amenities
```


#Sequence Diagram
##1. User Registration Sequence Diagram
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

##2. Place Creation Sequence Diagram
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
##3. Review Submission Sequence Diagram
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
##4. Fetching a List of Places Sequence Diagram
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
