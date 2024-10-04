# HBnB Evolution Technical Documentation

Table of Contents
1) Introduction
2) High-Level Architecture
3) Business Logic Layer
4) API Interaction Flow
5) Conclusion

## 1) Introduction
### Overview of the Project
HBnB Evolution is a simplified version of an AirBnB-like application designed to facilitate user interactions around property listings, user reviews, and amenities. This document serves as a foundation for understanding the architecture, business logic, and API interactions within the application.

### Purpose of the Document
The purpose of this document is to provide a clear and detailed reference that outlines the application's structure, the relationships between various components, and the flow of information through the system. This will serve as a guide for the implementation phases of the HBnB Evolution application.

## 2) High-Level Architecture
### High-Level Package Diagram
The following diagram illustrates the three-layer architecture of the HBnB Evolution application. It demonstrates the interaction between the Presentation Layer, Business Logic Layer, and Persistence Layer using the facade pattern.
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

Explanatory Notes:
Presentation Layer: This layer encompasses all services and API endpoints that interact with users, facilitating user registration, property management, and review submissions.
Business Logic Layer: It includes the core models representing the entities (User, Place, Review, Amenity) and their respective business logic.
Persistence Layer: Responsible for data storage and retrieval, this layer interacts directly with the database to perform CRUD operations.
Facade Pattern: The facade pattern simplifies communication between the layers by providing a unified interface through which the Presentation Layer interacts with the Business Logic Layer.

#### Purpose:
To illustrate the high-level structure of the application by showing how different layers interact and the relationships between them.

#### Key Components:
Presentation Layer: Contains the interface for interacting with users, including ServiceAPI and WebService.
Business Logic Layer: Manages the core functionality of the application, including classes like User, Place, Review, and Amenity.
Persistence Layer: Handles data storage and retrieval with DatabaseManager, Database JSON, and various queries.

#### Design Decisions:
The use of the Facade Pattern between the Presentation Layer and the Business Logic Layer simplifies the interface and hides complexity.
The direct interaction between the Business Logic Layer and the Persistence Layer is essential for clean separation of concerns, allowing business rules to operate independently of data storage.

#### Fit into Overall Architecture:
This diagram encapsulates the three-layer architecture of the application, defining clear boundaries and responsibilities for each layer. It sets the foundation for understanding how the application processes user requests and manages data.

## 3) Business Logic Layer
### Detailed Class Diagram
The following diagram outlines the classes within the Business Logic layer, detailing the attributes, methods, and relationships between the User, Place, Review, and Amenity entities.

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

#### Explanatory Notes:
User: Represents the application user with attributes for identification and methods for registration, updating profiles, and deletion.
Place: Represents a property listing, including methods for creation, updating, and listing of properties.
Review: Allows users to submit reviews for places they have visited, associated with both a user and a place.
Amenity: Represents amenities that can be associated with places, including methods for managing amenities.
Relationships:
A user can own multiple places (1 to many).
A place can have multiple reviews and amenities (1 to many).

#### Purpose:
To define the structure of key classes in the application, including their attributes and methods, and to illustrate the relationships between them.

#### Key Components:
    User: Manages user-related data and functionality.
    Place: Represents locations that can be listed, reviewed, and interacted with.
    Review: Handles the reviews made by users on places.
    Amenity: Describes additional features associated with a place.

#### Design Decisions:
Each class encapsulates its data and provides methods for interacting with that data, promoting encapsulation and abstraction.
The use of associations (e.g., User owns Place, Place receives Review) establishes clear relationships, helping to model real-world interactions.

#### Fit into Overall Architecture:
This diagram forms the core of the Business Logic Layer, showing how entities interact and are structured. It serves as a blueprint for implementation and guides the development of the application’s functionalities.

## 4) API Interaction Flow
### Sequence Diagrams for API Calls
The following sequence diagrams depict the flow of interactions for four different API calls, illustrating how information moves between the layers.

#### 1. User Registration
```mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: Register User (first_name, last_name, email, password)
API->>BusinessLogic: Validate and Process Registration
BusinessLogic->>Database: Save User Data
Database-->>BusinessLogic: Confirm User Registration
BusinessLogic-->>API: Return Success/Failure
API-->>User: Response
```
##### Purpose:
To outline the process of user registration, illustrating the flow of information and actions between the user and the system.

##### Key Components:
User: The actor initiating the registration.
API: The interface that processes user requests.
BusinessLogic: Validates and processes business rules for registration.
Persistence: Handles data storage.

##### Design Decisions:
The validation step ensures that only correctly formatted and complete data is saved, enhancing data integrity.
Returning user info after successful creation allows for immediate feedback to the user.

##### Fit into Overall Architecture:
his diagram shows how the Presentation Layer interacts with the Business Logic Layer and the Persistence Layer to fulfill user requests, emphasizing the application’s responsiveness and data handling.

#### 2. Place Creation
```mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: Create Place (title, description, price, latitude, longitude)
API->>BusinessLogic: Validate Place Data
BusinessLogic->>Database: Save Place Data
Database-->>BusinessLogic: Confirm Place Creation
BusinessLogic-->>API: Return Success/Failure
API-->>User: Response
```
##### Purpose:
To illustrate the steps involved in creating a new place, detailing the interactions among system components.

##### Key Components:
Same as above.

##### Design Decisions:
Similar to the user registration process, this sequence emphasizes validation and persistence of place data to maintain accuracy and reliability.

##### Fit into Overall Architecture:
It highlights the role of the Business Logic Layer in managing place creation and how it interfaces with the API and data storage.


#### 3. Review Submission
```mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: Submit Review (place_id, rating, comment)
API->>BusinessLogic: Validate Review Data
BusinessLogic->>Database: Save Review Data
Database-->>BusinessLogic: Confirm Review Submission
BusinessLogic-->>API: Return Success/Failure
API-->>User: Response
```

##### Purpose:
To demonstrate how users submit reviews and how these are processed within the application.

##### Key Components:
Same as above.

##### Design Decisions:
The sequence emphasizes data validation and storage for reviews, ensuring that only valid entries are accepted.

##### Fit into Overall Architecture:
This diagram is essential for understanding user interactions with reviews and illustrates the flow from the user through the system to data storage.

#### 4. Fetching a List of Places
```mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: Request List of Places
API->>BusinessLogic: Fetch Places
BusinessLogic->>Database: Retrieve Places Data
Database-->>BusinessLogic: Return Places Data
BusinessLogic-->>API: Send Places Data
API-->>User: Return List of Places
```
##### Purpose:
To show the process of fetching a list of places, highlighting the interactions necessary to retrieve data.

##### Key Components:
Same as above.

##### Design Decisions:
The validation step ensures that the request is legitimate, while retrieval from the persistence layer showcases the separation of concerns.

##### Fit into Overall Architecture:
This diagram illustrates the retrieval operations of the Business Logic Layer and its communication with the Presentation Layer, emphasizing the application’s ability to respond to user queries effectively.


#### Explanatory Notes:
Each sequence diagram illustrates the step-by-step interactions for specific API calls.
The flow shows how data is validated, processed, and stored, as well as how responses are generated and sent back to the user.

## 5) Conclusion
This technical documentation provides a foundational understanding of the HBnB Evolution application's architecture, business logic, and API interactions. The diagrams and explanations included serve as a comprehensive reference for the implementation phases, ensuring that all stakeholders have a clear vision of the system's design and functionality.
