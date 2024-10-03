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
