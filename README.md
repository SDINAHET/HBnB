# Project HBNB

## PART1

<h4>Context and Objective</h4>

<p>In this initial phase, you will focus on creating comprehensive technical documentation that will serve as the foundation for the development of the HBnB Evolution application. This documentation will help in understanding the overall architecture, the detailed design of the business logic, and the interactions within the system.</p>

<h4>Problem Description</h4>

<p>You are tasked with documenting the architecture and design of a simplified version of an AirBnB-like application, named HBnB Evolution. The application will allow users to perform the following primary operations:</p>

<ol>
<li><strong>User Management</strong>: Users can register, update their profiles, and be identified as either regular users or administrators.</li>
<li><strong>Place Management</strong>: Users can list properties (places) they own, specifying details such as name, description, price, and location (latitude and longitude). Each place can also have a list of amenities.</li>
<li><strong>Review Management</strong>: Users can leave reviews for places they have visited, including a rating and a comment.</li>
<li><strong>Amenity Management</strong>: The application will manage amenities that can be associated with places.</li>
</ol>

<h4>Business Rules and Requirements</h4>

<ol>
<li><p><strong>User Entity</strong></p>

<ul>
<li>Each user has a <code>first name</code>, <code>last name</code>, <code>email</code>, and <code>password</code>.</li>
<li>Users can be identified as administrators through a <code>boolean</code> attribute.</li>
<li>Users should be able to register, update their profile information, and be deleted.</li>
</ul></li>
<li><p><strong>Place Entity</strong></p>

<ul>
<li>Each place has a <code>title</code>, <code>description</code>, <code>price</code>, <code>latitude</code>, and <code>longitude</code>.</li>
<li>Places are associated with the user who created them (<code>owner</code>).</li>
<li>Places can have a <strong>list of amenities</strong>.</li>
<li>Places can be created, updated, deleted, and listed.</li>
</ul></li>
<li><p><strong>Review Entity</strong></p>

<ul>
<li>Each review is associated with a specific <code>place</code> and <code>user</code>, and includes a <code>rating</code> and <code>comment</code>.</li>
<li>Reviews can be created, updated, deleted, and listed by place.</li>
</ul></li>
<li><p><strong>Amenity Entity</strong></p>

<ul>
<li>Each amenity has a <code>name</code>, and <code>description</code>.</li>
<li>Amenities can be created, updated, deleted, and listed.</li>
</ul></li>
</ol>

<blockquote>
<ul>
<li>Each object should be uniquely identified by a ID.</li>
<li>For audit reasons, the creation and update datetime should be registered for all entities.</li>
</ul>
</blockquote>

<h4><strong>Architecture and Layers</strong></h4>

<ul>
<li>The application follows a layered architecture divided into:

<ul>
<li><strong>Presentation Layer</strong>: This includes the services and API through which users interact with the system.</li>
<li><strong>Business Logic Layer</strong>: This contains the models and the core logic of the application.</li>
<li><strong>Persistence Layer</strong>: This is responsible for storing and retrieving data from the database.</li>
</ul></li>
</ul>

<h4><strong>Persistence</strong></h4>

<ul>
<li>All data will be persisted in a database, which will be specified and implemented in Part 3 of the project.</li>
</ul>

<h4>Tasks</h4>

<ol>
<li><p><strong>High-Level Package Diagram</strong></p>

<ul>
<li>Create a high-level package diagram that illustrates the three-layer architecture of the application and the communication between these layers via the facade pattern.</li>
</ul></li>
<li><p><strong>Detailed Class Diagram for Business Logic Layer</strong></p>

<ul>
<li>Design a detailed class diagram for the Business Logic layer, focusing on the User, Place, Review, and Amenity entities, including their attributes, methods, and relationships. Ensure to include the relationships between Places and Amenities.</li>
</ul></li>
<li><p><strong>Sequence Diagrams for API Calls</strong></p>

<ul>
<li>Develop sequence diagrams for at least four different API calls to show the interaction between the layers and the flow of information. Suggested API calls include user registration, place creation, review submission, and fetching a list of places.</li>
</ul></li>
<li><p><strong>Documentation Compilation</strong></p>

<ul>
<li>Compile all diagrams and explanatory notes into a comprehensive technical document.</li>
</ul></li>
</ol>

<h4>Conditions and Constraints</h4>

<ul>
<li>The documentation must clearly represent the interactions and flow of data between the different layers of the application.</li>
<li>Use UML notation for all diagrams to ensure consistency and clarity.</li>
<li>The business rules and requirements outlined above must be reflected accurately in the diagrams.</li>
<li>Ensure that the diagrams are detailed enough to guide the implementation phase in the next parts of the project.</li>
</ul>

<h4>Resources:</h4>

<ul>
<li><p>UML Basics</p>

<ul>
<li><a href="https://intranet.hbtn.io/concepts/1166" title="[Concept Page] OOP - Introduction to UML" target="_blank">[Concept Page] OOP - Introduction to UML</a></li>
</ul></li>
<li><p>Package Diagrams</p>

<ul>
<li><a href="/rltoken/TwbMUc103_TTSmUJ2PJ75g" title="UML Package Diagram Overview" target="_blank">UML Package Diagram Overview</a></li>
<li><a href="/rltoken/cmtzgEn1nV70oHy5yVyXtQ" title="UML Package Diagrams Guide" target="_blank">UML Package Diagrams Guide</a></li>
</ul></li>
<li><p>Class Diagrams</p>

<ul>
<li><a href="/rltoken/QeY8b_kDd8LvXn0UrUQf1w" title="UML Class Diagram Tutorial" target="_blank">UML Class Diagram Tutorial</a></li>
<li><a href="/rltoken/V9C_7aQidACV2TZv6W3aoQ" title="How to Draw UML Class Diagrams" target="_blank">How to Draw UML Class Diagrams</a></li>
</ul></li>
<li><p>Sequence Diagrams</p>

<ul>
<li><a href="/rltoken/JLXWY9rghHDqvehB0bmw8g" title="UML Sequence Diagram Tutorial" target="_blank">UML Sequence Diagram Tutorial</a></li>
<li><a href="/rltoken/fGZTiA0jmClwNuP9RIYDcA" title="Understanding Sequence Diagrams" target="_blank">Understanding Sequence Diagrams</a></li>
</ul></li>
<li><p>General Diagram Tools</p>

<ul>
<li><a href="/rltoken/ntmP_DqeGZ6nnCIc1hjCvA" title="Mermaid.js Documentation" target="_blank">Mermaid.js Documentation</a></li>
<li><a href="/rltoken/6ZbmaR6TyvcasnjkewTGQQ" title="draw.io" target="_blank">draw.io</a></li>
</ul></li>
</ul>

<h4>Expected Outcome</h4>

<p>By the end of this part, you should have a complete set of technical documentation that provides a clear and detailed blueprint for the HBnB Evolution application. This documentation will not only guide you through the implementation phases but also ensure that you have a solid understanding of the application&rsquo;s design and architecture.</p>

<p>Good luck, and remember to leverage the provided resources and your own research to overcome any challenges you encounter!</p>

  </div>
</div>
        </div>
      </div>
    </div>

### Task part1:
        <h2 id="task-container" class="gap">Tasks</h2>

  <div class="col-sm-12 col-md-12 col-lg-8 xol-xl-9">
      <div data-role="task31645" data-position="1" id="task-num-0">
        <div class="panel panel-default task-card " id="task-31645">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. High-Level Package Diagram
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="9546"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <h4>Objective</h4>

<p>Create a high-level package diagram that illustrates the three-layer architecture of the HBnB application and the communication between these layers via the facade pattern. This diagram will provide a conceptual overview of how the different components of the application are organized and how they interact with each other.</p>

<h4>Description</h4>

<p>In this task, you will develop a package diagram that visually represents the structure of the application, focusing on its three main layers:</p>

<ol>
<li><p><strong>Presentation Layer (Services, API):</strong> This layer handles the interaction between the user and the application. It includes all the services and APIs that are exposed to the users.</p></li>
<li><p><strong>Business Logic Layer (Models):</strong> This layer contains the core business logic and the models that represent the entities in the system (e.g., User, Place, Review, Amenity).</p></li>
<li><p><strong>Persistence Layer:</strong> This layer is responsible for data storage and retrieval, interacting directly with the database.</p></li>
</ol>

<p>Your diagram should clearly show the three layers, the components within each layer, and the communication pathways between them. The facade pattern should be represented as the interface through which the layers interact.</p>

<h4>Steps to Complete the Task</h4>

<ol>
<li><p><strong>Understand the Layered Architecture</strong></p>

<ul>
<li>Review the concept of layered architecture and how it is used to organize an application.</li>
<li>Understand the responsibilities of each layer in the context of the HBnB application.</li>
</ul></li>
<li><p><strong>Research the Facade Pattern</strong></p>

<ul>
<li>Familiarize yourself with the facade design pattern and how it simplifies interactions between layers by providing a unified interface.</li>
</ul></li>
<li><p><strong>Identify Key Components</strong></p>

<ul>
<li>Identify the key components that belong to each layer:

<ul>
<li><strong>Presentation Layer:</strong> Services, API endpoints.</li>
<li><strong>Business Logic Layer:</strong> Core models (User, Place, Review, Amenity).</li>
<li><strong>Persistence Layer:</strong> Database access objects or repositories.</li>
</ul></li>
</ul></li>
<li><p><strong>Draft the Package Diagram</strong></p>

<ul>
<li>Create a draft of your package diagram, showing the three layers and their components.</li>
<li>Indicate the communication pathways between layers via the facade pattern.</li>
<li>Ensure that the diagram is clear, logical, and easy to understand.</li>
</ul></li>
<li><p><strong>Review and Refine</strong></p>

<ul>
<li>Review your diagram to ensure that it accurately represents the application&rsquo;s architecture.</li>
<li>Make any necessary adjustments to improve clarity and completeness.</li>
</ul></li>
</ol>

<h4>Example of a generic package diagram using Mermaid.js:</h4>

<pre><code class="mermaid">classDiagram
class PresentationLayer {
    &lt;&lt;Interface&gt;&gt;
    +ServiceAPI
}
class BusinessLogicLayer {
    +ModelClasses
}
class PersistenceLayer {
    +DatabaseAccess
}
PresentationLayer --&gt; BusinessLogicLayer : Facade Pattern
BusinessLogicLayer --&gt; PersistenceLayer : Database Operations
</code></pre>

<h3><strong>Learning Resources</strong></h3>

<ul>
<li><a href="https://intranet.hbtn.io/concepts/1158" title="[Concept Page] Software Architecture Patterns - Layered Architecture in Python" target="_blank">[Concept Page] Software Architecture Patterns - Layered Architecture in Python</a></li>
<li><a href="/rltoken/Cbvx3wsffPH9GpvWf3N2SA" title="Facade Pattern Overview" target="_blank">Facade Pattern Overview</a></li>
<li><a href="/rltoken/cmtzgEn1nV70oHy5yVyXtQ" title="UML Package Diagram Guide" target="_blank">UML Package Diagram Guide</a></li>
<li><a href="/rltoken/TwbMUc103_TTSmUJ2PJ75g" title="UML Package Diagram Overview" target="_blank">UML Package Diagram Overview</a></li>
</ul>

<h4>Deliverables</h4>

<ul>
<li><p><strong>High-Level Package Diagram:</strong></p>

<ul>
<li>A clear, well-organized package diagram showing the three layers (Presentation, Business Logic, Persistence).</li>
<li>Communication pathways between layers via the facade pattern.</li>
</ul></li>
<li><p><strong>Explanatory Notes:</strong></p>

<ul>
<li>A brief description of each layer and its responsibilities.</li>
<li>Explanation of how the facade pattern facilitates communication between the layers.</li>
</ul></li>
</ul>

<h4>Recommendations</h4>

<ul>
<li><strong>Start Simple:</strong> Begin with a basic structure, then refine it as you understand the relationships and components better.</li>
<li><strong>Use Mermaid.js:</strong> If you are comfortable with coding, Mermaid.js is a great option for creating diagrams as part of your project documentation. It’s especially useful for version control and iterative development.</li>
<li><strong>Seek Feedback:</strong> Once your diagram is drafted, get feedback from peers or tutors to ensure clarity and accuracy.</li>
<li><strong>Document As You Go:</strong> Keep notes on your design decisions, as these will be useful when you compile your final documentation.</li>
</ul>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="31645" data-batch-id="843" data-toggle="modal" data-target="#task-31645-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-31645-users-done-modal" data-task-id="31645" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "0. High-Level Package Diagram"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


</div>


        <div class="fs-4 text-right">
            <strong class="text-primary">
              <span id="task-31645-score-info-score">0</span>/10
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

      </div>
      <div data-role="task31646" data-position="2" id="task-num-1">
        <div class="panel panel-default task-card " id="task-31646">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Detailed Class Diagram for Business Logic Layer
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="9546"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <h4>Objective</h4>

<p>Design a detailed class diagram for the Business Logic layer of the HBnB application. This diagram will depict the entities within this layer, their attributes, methods, and the relationships between them. The primary goal is to provide a clear and detailed visual representation of the core business logic, focusing on the key entities: User, Place, Review, and Amenity.</p>

<h4>Description</h4>

<p>In this task, you will create a class diagram that represents the internal structure of the Business Logic layer. This diagram will include entities, their attributes, methods, and relationships such as associations, inheritance, and dependencies.</p>

<h4>Steps to Complete the Task</h4>

<ol>
<li><p><strong>Review the Business Logic Requirements</strong></p>

<ul>
<li>Understand the business rules and requirements for each entity in the Business Logic layer.</li>
<li>Review how these entities interact with each other and the significance of their relationships.</li>
</ul></li>
<li><p><strong>Identify Key Attributes and Methods</strong></p>

<ul>
<li>For each entity, identify the key attributes and methods that define its behavior and state.</li>
<li>Ensure that each entity includes a unique identifier (UUID4) and attributes for creation and update dates.</li>
</ul></li>
<li><p><strong>Design the Class Diagram</strong></p>

<ul>
<li>Begin by outlining the entities as classes, specifying their attributes and methods.</li>
<li>Represent relationships between entities using appropriate UML notation (e.g., associations, generalizations, compositions).</li>
<li>Include multiplicity where relevant.</li>
</ul></li>
<li><p><strong>Refine and Review</strong></p>

<ul>
<li>Review the diagram to ensure that it accurately represents the business logic and adheres to the project’s requirements.</li>
<li>Refine the diagram as needed to improve clarity and completeness.</li>
</ul></li>
</ol>

<h4>Example of a generic class diagram using Mermaid.js:</h4>

<pre><code class="mermaid">classDiagram
class ClassName {
    +AttributeType attributeName
    +MethodType methodName()
}
ClassName1 --|&gt; ClassName2 : Inheritance
ClassName3 o-- ClassName : Composition
ClassName4 --&gt; ClassName : Association
</code></pre>

<h3><strong>Learning Resources</strong></h3>

<ul>
<li><a href="/rltoken/QeY8b_kDd8LvXn0UrUQf1w" title="UML Class Diagram Tutorial" target="_blank">UML Class Diagram Tutorial</a></li>
<li><a href="/rltoken/V9C_7aQidACV2TZv6W3aoQ" title="How to Draw UML Class Diagrams" target="_blank">How to Draw UML Class Diagrams</a></li>
<li><a href="https://intranet.hbtn.io/concepts/1216" title="[Concept Page] OOP - SOLID Pronciples" target="_blank">[Concept Page] OOP - SOLID Pronciples</a></li>
<li><a href="/rltoken/iosNtHCMbjQLGQyu59HD0A" title="SOLID Principles of Object-Oriented Design" target="_blank">SOLID Principles of Object-Oriented Design</a></li>
</ul>

<h4>Deliverables</h4>

<ul>
<li><p><strong>Detailed Class Diagram:</strong></p>

<ul>
<li>A comprehensive class diagram showing the key entities, including their attributes, methods, and relationships.</li>
<li>Proper use of UML notation to depict associations, generalizations, and compositions.</li>
</ul></li>
<li><p><strong>Explanatory Notes:</strong></p>

<ul>
<li>A brief description of each entity, including its role in the system and key attributes and methods.</li>
<li>Explanation of relationships between entities and how they contribute to the overall business logic.</li>
</ul></li>
</ul>

<h4>Recommendations</h4>

<ul>
<li><strong>Start with a Basic Outline:</strong> Begin by defining the classes and their basic attributes. Once you have the core structure, add methods and refine the relationships between entities.</li>
<li><strong>Leverage Mermaid.js:</strong> If you are comfortable with coding, consider using Mermaid.js for creating and maintaining your class diagram as part of your project documentation.</li>
<li><strong>Consider Relationships Carefully:</strong> Pay close attention to how entities are related, especially when defining associations and compositions. Ensure that these relationships are accurately represented in your diagram.</li>
<li><strong>Iterate and Improve:</strong> Don’t hesitate to revise your diagram as you refine your understanding of the system. Continuous improvement will lead to a more accurate and comprehensive representation.</li>
</ul>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="31646" data-batch-id="843" data-toggle="modal" data-target="#task-31646-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-31646-users-done-modal" data-task-id="31646" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "1. Detailed Class Diagram for Business Logic Layer"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


</div>


        <div class="fs-4 text-right">
            <strong class="text-primary">
              <span id="task-31646-score-info-score">0</span>/10
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

      </div>
      <div data-role="task31647" data-position="3" id="task-num-2">
        <div class="panel panel-default task-card " id="task-31647">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Sequence Diagrams for API Calls
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="9546"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <h4>Objective</h4>

<p>Develop sequence diagrams for at least four different API calls to illustrate the interaction between the layers (Presentation, Business Logic, Persistence) and the flow of information within the HBnB application. The sequence diagrams will help visualize how different components of the system interact to fulfill specific use cases, showing the step-by-step process of handling API requests.</p>

<h4>Description</h4>

<p>In this task, you will create sequence diagrams that represent the flow of interactions across the different layers of the application for specific API calls. These diagrams will show how the Presentation Layer (Services, API), Business Logic Layer (Models), and Persistence Layer (Database) communicate with each other to handle user requests.</p>

<p>You will create sequence diagrams for the following API calls:</p>

<ol>
<li><strong>User Registration:</strong> A user signs up for a new account.</li>
<li><strong>Place Creation:</strong> A user creates a new place listing.</li>
<li><strong>Review Submission:</strong> A user submits a review for a place.</li>
<li><strong>Fetching a List of Places:</strong> A user requests a list of places based on certain criteria.</li>
</ol>

<h4>Steps to Complete the Task</h4>

<ol>
<li><p><strong>Understand the Use Cases</strong></p>

<ul>
<li>Review the requirements and business logic for each of the selected API calls.</li>
<li>Understand the sequence of operations needed to fulfill each API call, from the moment a request is received by the API to the point where a response is returned to the client.</li>
</ul></li>
<li><p><strong>Identify Key Components Involved</strong></p>

<ul>
<li>Determine which components of the system (within each layer) are involved in handling each API call.</li>
<li>Identify the order of operations, including method calls and data exchanges between components.</li>
</ul></li>
<li><p><strong>Design the Sequence Diagrams</strong></p>

<ul>
<li>Begin by drafting the sequence of interactions for each API call.</li>
<li>For each diagram, start with the API call from the Presentation Layer, followed by interactions with the Business Logic Layer, and ending with operations in the Persistence Layer.</li>
<li>Clearly show the flow of messages, including method invocations, data retrieval, and processing steps.</li>
</ul></li>
<li><p><strong>Refine and Review</strong></p>

<ul>
<li>Review your diagrams to ensure they accurately reflect the flow of information and operations required to fulfill each API call.</li>
<li>Refine the diagrams for clarity and completeness, ensuring all relevant interactions are captured.</li>
</ul></li>
</ol>

<h4>Example of a generic sequence diagram using Mermaid.js:</h4>

<pre><code class="mermaid">sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User-&gt;&gt;API: API Call (e.g., Register User)
API-&gt;&gt;BusinessLogic: Validate and Process Request
BusinessLogic-&gt;&gt;Database: Save Data
Database--&gt;&gt;BusinessLogic: Confirm Save
BusinessLogic--&gt;&gt;API: Return Response
API--&gt;&gt;User: Return Success/Failure
</code></pre>

<h3><strong>Learning Resources</strong></h3>

<ul>
<li><a href="/rltoken/JLXWY9rghHDqvehB0bmw8g" title="UML Sequence Diagram Tutorial" target="_blank">UML Sequence Diagram Tutorial</a></li>
<li><a href="/rltoken/fGZTiA0jmClwNuP9RIYDcA" title="Understanding Sequence Diagrams" target="_blank">Understanding Sequence Diagrams</a></li>
<li><a href="/rltoken/wTzEdyHuxhh74FPpDhH-Vw" title="RESTful API Design Guide" target="_blank">RESTful API Design Guide</a></li>
</ul>

<h4>Deliverables</h4>

<ul>
<li><p><strong>Sequence Diagrams:</strong></p>

<ul>
<li>Four sequence diagrams, each depicting the interaction flow for a specific API call (User Registration, Place Creation, Review Submission, Fetching a List of Places).</li>
<li>Diagrams should clearly illustrate the communication between layers and the sequence of operations required to process each request.</li>
</ul></li>
<li><p><strong>Explanatory Notes:</strong></p>

<ul>
<li>A brief description of each API call, outlining the key steps involved and the purpose of the sequence diagram.</li>
<li>Explanation of the flow of interactions, highlighting how each layer contributes to fulfilling the API request.</li>
</ul></li>
</ul>

<h4>Recommendations</h4>

<ul>
<li><strong>Focus on Clarity:</strong> Ensure that your diagrams are easy to read and understand. Use consistent naming conventions for components and clearly indicate the flow of messages.</li>
<li><strong>Use Mermaid.js for Code-Based Diagrams:</strong> If you prefer working with code, Mermaid.js offers a straightforward way to create and maintain sequence diagrams as part of your documentation.</li>
<li><strong>Double-Check the Flow:</strong> Make sure the sequence of operations in your diagrams accurately reflects the intended behavior of the system. Each step should logically follow the previous one.</li>
<li><strong>Iterate as Needed:</strong> Don&rsquo;t hesitate to revise your diagrams as you refine your understanding of the system&rsquo;s interactions. The goal is to create accurate and informative representations of the API calls.</li>
</ul>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="31647" data-batch-id="843" data-toggle="modal" data-target="#task-31647-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-31647-users-done-modal" data-task-id="31647" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "2. Sequence Diagrams for API Calls"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


</div>


        <div class="fs-4 text-right">
            <strong class="text-primary">
              <span id="task-31647-score-info-score">0</span>/10
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

      </div>
      <div data-role="task31648" data-position="4" id="task-num-3">
        <div class="panel panel-default task-card " id="task-31648">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Documentation Compilation
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="9546"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <h4>Objective</h4>

<p>Compile all the diagrams and explanatory notes created in the previous tasks into a comprehensive technical document. This document will serve as a detailed blueprint for the HBnB project, guiding the implementation phases and providing a clear reference for the system’s architecture and design.</p>

<h4>Description</h4>

<p>In this task, you will bring together the high-level package diagram, detailed class diagram for the Business Logic layer, and sequence diagrams for API calls into a single, well-organized document. The goal is to create a cohesive and comprehensive technical document that not only includes the diagrams but also provides explanatory notes that clarify design decisions, describe interactions, and outline the overall architecture of the application.</p>

<p>The final document should be clear, professional, and structured in a way that makes it easy to follow and understand. It will be used as a reference throughout the project, so accuracy and completeness are critical.</p>

<h4>Steps to Complete the Task</h4>

<ol>
<li><p><strong>Organize Your Work</strong></p>

<ul>
<li>Gather all diagrams created in the previous tasks: </li>
<li>High-Level Package Diagram (Task 1)</li>
<li>Detailed Class Diagram for the Business Logic Layer (Task 2)</li>
<li>Sequence Diagrams for API Calls (Task 3)</li>
<li>Ensure that each diagram is finalized and reviewed for accuracy and clarity.</li>
</ul></li>
<li><p><strong>Create an Introduction</strong></p>

<ul>
<li>Write a brief introduction for the document that explains its purpose and scope. </li>
<li>Provide an overview of the HBnB project and the role of this technical document in guiding the implementation process.</li>
</ul></li>
<li><p><strong>Structure the Document</strong></p>

<ul>
<li><strong>Introduction:</strong> Briefly describe the project, the purpose of the document, and what it contains.</li>
<li><strong>High-Level Architecture:</strong> Include the high-level package diagram and explain the layered architecture and facade pattern used.</li>
<li><strong>Business Logic Layer:</strong> Present the detailed class diagram, explaining the entities, their relationships, and how they fit into the business logic of the application.</li>
<li><strong>API Interaction Flow:</strong> Include the sequence diagrams for the selected API calls, providing explanations of the interactions and data flow between components.</li>
</ul></li>
<li><p><strong>Add Explanatory Notes</strong></p>

<ul>
<li>For each diagram, include explanatory notes that describe:</li>
<li>The purpose of the diagram.</li>
<li>Key components or classes involved.</li>
<li>Design decisions and their rationale.</li>
<li>How the diagram fits into the overall architecture and design of the application.</li>
</ul></li>
<li><p><strong>Review and Edit</strong></p>

<ul>
<li>Review the entire document to ensure it is clear, logical, and free of errors.</li>
<li>Edit the document for clarity, conciseness, and professionalism. Ensure consistent formatting and style throughout.</li>
<li>Make sure that all diagrams are accurately represented and that their accompanying explanations are clear and informative.</li>
</ul></li>
<li><p><strong>Finalize the Document</strong></p>

<ul>
<li>Save the document in a standard format (e.g., PDF or Word document) for easy sharing and reference.</li>
<li>Double-check that all components of the technical documentation are included and correctly formatted.</li>
</ul></li>
</ol>

<h4><strong>Learning Resources</strong></h4>

<ul>
<li><a href="/rltoken/9sAyWkM3-MQGta2kyH-k5Q" title="Microsoft Writing Style Guide" target="_blank">Microsoft Writing Style Guide</a></li>
<li><a href="/rltoken/LjS7MOmyU-K0WRA3O5eJdA" title="Google Developer Documentation Style Guide" target="_blank">Google Developer Documentation Style Guide</a></li>
<li><a href="/rltoken/BaowT5SYwYTkZv_towzp2A" title="Tips for Formatting a Professional Document" target="_blank">Tips for Formatting a Professional Document</a></li>
</ul>

<h4>Deliverables</h4>

<p><strong>Comprehensive Technical Document:</strong>
- A well-organized document that includes:
  - <strong>Introduction:</strong> Overview of the project and the purpose of the document.
  - <strong>High-Level Architecture:</strong> High-Level Package Diagram with explanations.
  - <strong>Business Logic Layer:</strong> Detailed Class Diagram with explanations.
  - <strong>API Interaction Flow:</strong> Sequence Diagrams for API calls with explanations.
- The document should be clear, professional, and easy to follow, serving as a reference for the implementation phases.</p>

<h4>Recommendations</h4>

<ul>
<li><strong>Focus on Clarity:</strong> Ensure that both the diagrams and the accompanying text are easy to understand. Avoid overly technical jargon unless necessary, and explain all key terms and concepts.</li>
<li><strong>Consistency is Key:</strong> Maintain consistent formatting, terminology, and style throughout the document. This includes consistent naming conventions for classes, methods, and components.</li>
<li><strong>Seek Feedback:</strong> If possible, have peers or tutors review your document before finalizing it. Fresh eyes can help catch any errors or unclear sections you might have missed.</li>
<li><strong>Proofread Carefully:</strong> Errors in a technical document can lead to misunderstandings during implementation, so take the time to thoroughly proofread your work.</li>
</ul>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

## PART2
### TASK Part2:
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

# Implement the Place Endpoints

## Context

This task involves setting up the endpoints to handle CRUD operations (Create, Read, Update) for places, while ensuring integration with the Business Logic layer via the Facade pattern. The `DELETE` operation will **not** be implemented for places in this part of the project.

Given that the `Place` entity has relationships with other entities, such as `User` (owner) and `Amenity`, you’ll need to handle these relationships carefully while maintaining the integrity of the application logic.

The `Review` entity will be implemented in the next task, so it should **not be included in this task**.

## In this task, you will

1. Set up the `POST`, `GET`, and `PUT` endpoints for managing places.
2. Implement the logic for handling place-related operations in the Business Logic layer.
3. Integrate the Presentation layer (API) and Business Logic layer through the Facade.
4. Implement validation for specific attributes like `price`, `latitude`, and `longitude`.
5. Ensure that related data such as `owner` details and `amenities` are properly handled and returned with the Place data.

## Instructions

### Implement the Place Management Logic in the Business Logic Layer

In the `models/place.py` file, the `Place` class should have already been implemented in Task 2, ensure that the class handles relationships with other entities and performs attribute validation.

Update the `HBnBFacade` class in the `services/facade.py` file, adding the following methods:

```python
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
```

These methods handle place creation, retrieval, and updates. Consider using custom setter methods or raising exceptions to handle invalid data.

#### Validation of Place Attributes

When implementing validation for attributes like `price`, `latitude`, and `longitude`, consider the following:

- `price` should be a non-negative float.
- `latitude` should be between -90 and 90.
- `longitude` should be between -180 and 180.

Implement these validations using property setters in the `Place` class, raising appropriate exceptions for invalid values.

### Implement the Place Endpoints in the Presentation Layer (API)

Create the `api/v1/places.py` file, then define the routes and create the skeleton methods for these endpoints. Use the placeholders provided below to get started.

```python
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
```

- `POST /api/v1/places/`: Register a new place.
- `GET /api/v1/places/`: Return a list of all places.
- `GET /api/v1/places/<place_id>`: Retrieve details of a specific place, including its associated owner and amenities.
- `PUT /api/v1/places/<place_id>`: Update place information.

**Explanation:**

- The `POST` endpoint registers a new place, while `GET` and `PUT` manage place retrieval and updates. The `GET /api/v1/places/<place_id>` endpoint includes associated owner and amenities for the place.
- You are responsible for implementing the logic for handling relationships between places, owners, and amenities.

> [!IMPORTANT]
> **Remember to register the namespace and API documentation for the amenity endpoints in the `api/__init__.py` file.**

## Input and Output Formats, Status Codes

For each endpoint, ensure that the input format, output format, and status codes are consistent and clearly defined.

### Test the Provided Endpoints

Once the endpoints are implemented, use tools like Postman or cURL to test each operation.
Ensure that your endpoints are working as expected. Here are some examples:

#### Register a New Place (POST /api/v1/places/)

```http
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
```

Expected Response:

```jsonc
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
```

Possible Status Codes:

- 201 Created: When the place is successfully created.
- 400 Bad Request: If input data is invalid.

#### Retrieve All Places (GET /api/v1/places/)

```http
GET /api/v1/places/
Content-Type: application/json
```

Expected Response:

```jsonc
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
```

Possible Status Codes:

- 200 OK: List of places retrieved successfully.

#### Retrieve Place Details (GET /api/v1/places/<place_id>)

```http
GET /api/v1/places/<place_id>
Content-Type: application/json
```

Expected Response:

```jsonc
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
```

Possible Status Codes:

- 200 OK: When the place and its associated owner and amenities are successfully retrieved.
- 404 Not Found: If the place does not exist.

#### Update a Place’s Information (PUT /api/v1/places/<place_id>)

```http
PUT /api/v1/places/<place_id>
Content-Type: application/json

{
  "title": "Luxury Condo",
  "description": "An upscale place to stay",
  "price": 200.0
}
```

Expected Response:

```jsonc
{
  "message": "Place updated successfully"
}

// 200 OK
```

Possible Status Codes:

- 200 OK: When the place is successfully updated.
- 404 Not Found: If the place does not exist.
- 400 Bad Request: If input data is invalid.

## Expected Outcome

By the end of this task, you should have implemented the core place management endpoints, including the ability to create, read, and update places. You will have handled the relationships between places, owners, and amenities, including validating specific attributes like price, latitude, and longitude. The functionality should be documented and tested, ensuring smooth operation within the HBnB application.

## Resources

- [**Flask-RESTx Documentation**](https://flask-restx.readthedocs.io/)
- [**Testing REST APIs with cURL**](https://everything.curl.dev/)
- [**Designing RESTful APIs**](https://restfulapi.net/)

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

## PART3
### TASK Part3:

### Introduction to Part 3: Enhanced Backend with Authentication and Database Integration

Welcome to Part 3 of the **HBnB Project**, where you will extend the backend of the application by introducing **user authentication**, **authorization**, and **database integration** using **SQLAlchemy** and **SQLite** for development. Later, you'll configure **MySQL** for production environments. In this part, you will secure the backend, introduce persistent storage, and prepare the application for a scalable, real-world deployment.

#### Objectives of the Project
1. **Authentication and Authorization**: Implement JWT-based user authentication using **Flask-JWT-Extended** and role-based access control with the `is_admin` attribute for specific endpoints.
2. **Database Integration**: Replace in-memory storage with **SQLite** for development using **SQLAlchemy** as the ORM and prepare for **MySQL** for production.
3. **CRUD Operations with Database Persistence**: Refactor all CRUD operations to interact with a persistent database.
4. **Database Design and Visualization**: Design the database schema using **mermaid.js** and ensure all relationships between entities are correctly mapped.
5. **Data Consistency and Validation**: Ensure that data validation and constraints are properly enforced in the models.

#### Learning Objectives
By the end of this part, you will:
- Implement **JWT authentication** to secure your API and manage user sessions.
- Enforce **role-based access control** to restrict access based on user roles (regular users vs. administrators).
- Replace in-memory repositories with a **SQLite-based persistence layer** using **SQLAlchemy** for development and configure **MySQL** for production.
- Design and visualize a **relational database schema** using **mermaid.js** to handle relationships between users, places, reviews, and amenities.
- Ensure the backend is secure, scalable, and provides reliable data storage for production environments.

#### Project Context
In the previous parts of the project, you worked with in-memory storage, which is ideal for prototyping but insufficient for production environments. In Part 3, you'll transition to **SQLite**, a lightweight relational database, for development, while preparing the system for **MySQL** in production. This will give you hands-on experience with real-world database systems, allowing your application to scale effectively.

Additionally, you'll introduce **JWT-based authentication** to secure the API, ensuring that only authenticated users can interact with certain endpoints. You will also implement role-based access control to enforce restrictions based on the user's privileges (regular users vs. administrators).

#### Project Resources
Here are some resources that will guide you through this part of the project:
- **JWT Authentication**: [Flask-JWT-Extended Documentation](https://flask-jwt-extended.readthedocs.io/en/stable/)
- **SQLAlchemy ORM**: [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/20/)
- **SQLite**: [SQLite Documentation](https://sqlite.org/docs.html)
- **MySQL**: [MySQL Documentation](https://dev.mysql.com/doc/)
- **Flask Documentation**: [Flask Official Documentation](https://flask.palletsprojects.com/en/2.0.x/)
- **Mermaid.js for ER Diagrams**: [Mermaid.js Documentation](https://mermaid-js.github.io/mermaid/#/)

#### Structure of the Project
In this part of the project, the tasks are organized in a way that builds progressively towards a complete, secure, and database-backed backend system:

1. **Modify the User Model to Include Password**: You will start by modifying the `User` model to store passwords securely using bcrypt2 and update the user registration logic.
2. **Implement JWT Authentication**: Secure the API using JWT tokens, ensuring only authenticated users can access protected endpoints.
3. **Implement Authorization for Specific Endpoints**: You will implement role-based access control to restrict certain actions (e.g., admin-only actions).
4. **SQLite Database Integration**: Transition from in-memory data storage to **SQLite** as the persistent database during development.
5. **Map Entities Using SQLAlchemy**: Map existing entities (`User`, `Place`, `Review`, `Amenity`) to the database using SQLAlchemy and ensure relationships are well-defined.
6. **Prepare for MySQL in Production**: Towards the end of this phase, you’ll configure the application to use **MySQL** in production and **SQLite** for development.
7. **Database Design and Visualization**: Use **mermaid.js** to create entity-relationship diagrams for your database schema.

Each task is carefully designed to build on previous work and ensure the system transitions smoothly from development to production readiness.

---

By the end of Part 3, you will have a backend that not only stores data in a persistent and secure database but also ensures that only authorized users can access and modify specific data. You will have implemented industry-standard authentication and database management practices that are crucial for real-world web applications.

### Transitioning from In-Memory to Database Persistence: A Step-by-Step Guide

In the earlier stages of the HBnB project, you implemented an in-memory persistence mechanism using a custom repository pattern. This allowed for rapid development and testing, as data was stored temporarily in memory during runtime. However, as your application evolves, a more permanent and robust data storage solution is required. This guide will walk you through transitioning from in-memory persistence to a database-backed persistence using SQLAlchemy while maintaining consistency with the code and patterns you've already implemented.

#### Recap: In-Memory Repository Implementation

In Part 2, you implemented a repository interface and an in-memory repository that adheres to this interface. Here's a recap of the code provided:

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

This repository pattern provided a simple yet effective way to manage CRUD operations on your entities, with the flexibility to switch out the storage mechanism later on.

#### Transitioning to Database Persistence with SQLAlchemy

Now, it's time to transition from the in-memory storage to a database-backed storage using SQLAlchemy. The key advantage here is that the existing repository interface allows us to easily swap out the in-memory implementation for a SQLAlchemy-based one without affecting the rest of your codebase.

**Step 1: Implement the SQLAlchemy Repository**

You will create a new repository class that implements the `Repository` interface but uses SQLAlchemy to interact with the database. This repository will adhere to the same interface as your in-memory repository, ensuring consistency.

```python
from app import db  # Assuming you have set up SQLAlchemy in your Flask app
from app.models import User, Place, Review, Amenity  # Import your models

class SQLAlchemyRepository(Repository):
    def __init__(self, model):
        self.model = model

    def add(self, obj):
        db.session.add(obj)
        db.session.commit()

    def get(self, obj_id):
        return self.model.query.get(obj_id)

    def get_all(self):
        return self.model.query.all()

    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            db.session.commit()

    def delete(self, obj_id):
        obj = self.get(obj_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()

    def get_by_attribute(self, attr_name, attr_value):
        return self.model.query.filter(getattr(self.model, attr_name) == attr_value).first()
```

**Explanation:**

- **SQLAlchemy Integration:** This repository class uses SQLAlchemy's session management to handle database transactions. The `add`, `update`, and `delete` methods wrap these transactions to ensure data integrity.
- **Query Methods:** The `get`, `get_all`, and `get_by_attribute` methods utilize SQLAlchemy's query interface to retrieve data from the database, mirroring the functionality of the in-memory repository.

**Step 2: Update the Facade**

Next, update your Facade class to use the `SQLAlchemyRepository` instead of the `InMemoryRepository`. This change is straightforward due to the interface-based design.

```python
class HBnBFacade:
    def __init__(self):
        self.user_repository = SQLAlchemyRepository(User)  # Switched to SQLAlchemyRepository
        self.place_repository = SQLAlchemyRepository(Place)
        self.review_repository = SQLAlchemyRepository(Review)
        self.amenity_repository = SQLAlchemyRepository(Amenity)

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repository.add(user)
        return user

    def get_user_by_id(self, user_id):
        return self.user_repository.get(user_id)

    def get_all_users(self):
        return self.user_repository.get_all()

    # Similarly, implement methods for other entities
```

**Explanation:**

- **Consistency in Facade:** The Facade's interface with the repository remains unchanged, making the transition seamless.
- **Entity-Specific Repositories:** The Facade initializes specific repositories for each entity, ensuring that the correct SQLAlchemy model is used.

#### Benefits of Using an Interface

By adhering to the `Repository` interface, the Facade and other components of your application are insulated from the specific details of data storage. This means:

- **Seamless Transition:** You can switch from in-memory storage to a database-backed solution without rewriting the core logic of your application.
- **Future Flexibility:** If you decide to switch to a different database or storage solution later, you can do so with minimal changes to your codebase, provided the new solution adheres to the same interface.

#### Conclusion

The transition from in-memory persistence to database persistence is a significant step in scaling your HBnB project. By leveraging the repository pattern and SQLAlchemy, you can ensure that your application remains modular, maintainable, and ready for production. The interface-based design you've implemented so far will make this transition smooth, maintaining the integrity and consistency of your codebase.

### Transitioning from In-Memory to Database Persistence: A Step-by-Step Guide

In the earlier stages of the HBnB project, you implemented an in-memory persistence mechanism using a custom repository pattern. This allowed for rapid development and testing, as data was stored temporarily in memory during runtime. However, as your application evolves, a more permanent and robust data storage solution is required. This guide will walk you through transitioning from in-memory persistence to a database-backed persistence using SQLAlchemy while maintaining consistency with the code and patterns you've already implemented.

#### Recap: In-Memory Repository Implementation

In Part 2, you implemented a repository interface and an in-memory repository that adheres to this interface. Here's a recap of the code provided:

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

This repository pattern provided a simple yet effective way to manage CRUD operations on your entities, with the flexibility to switch out the storage mechanism later on.

#### Transitioning to Database Persistence with SQLAlchemy

Now, it's time to transition from the in-memory storage to a database-backed storage using SQLAlchemy. The key advantage here is that the existing repository interface allows us to easily swap out the in-memory implementation for a SQLAlchemy-based one without affecting the rest of your codebase.

**Step 1: Implement the SQLAlchemy Repository**

You will create a new repository class that implements the `Repository` interface but uses SQLAlchemy to interact with the database. This repository will adhere to the same interface as your in-memory repository, ensuring consistency.

```python
from app import db  # Assuming you have set up SQLAlchemy in your Flask app
from app.models import User, Place, Review, Amenity  # Import your models

class SQLAlchemyRepository(Repository):
    def __init__(self, model):
        self.model = model

    def add(self, obj):
        db.session.add(obj)
        db.session.commit()

    def get(self, obj_id):
        return self.model.query.get(obj_id)

    def get_all(self):
        return self.model.query.all()

    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            db.session.commit()

    def delete(self, obj_id):
        obj = self.get(obj_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()

    def get_by_attribute(self, attr_name, attr_value):
        return self.model.query.filter(getattr(self.model, attr_name) == attr_value).first()
```

**Explanation:**

- **SQLAlchemy Integration:** This repository class uses SQLAlchemy's session management to handle database transactions. The `add`, `update`, and `delete` methods wrap these transactions to ensure data integrity.
- **Query Methods:** The `get`, `get_all`, and `get_by_attribute` methods utilize SQLAlchemy's query interface to retrieve data from the database, mirroring the functionality of the in-memory repository.

**Step 2: Update the Facade**

Next, update your Facade class to use the `SQLAlchemyRepository` instead of the `InMemoryRepository`. This change is straightforward due to the interface-based design.

```python
class HBnBFacade:
    def __init__(self):
        self.user_repository = SQLAlchemyRepository(User)  # Switched to SQLAlchemyRepository
        self.place_repository = SQLAlchemyRepository(Place)
        self.review_repository = SQLAlchemyRepository(Review)
        self.amenity_repository = SQLAlchemyRepository(Amenity)

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repository.add(user)
        return user

    def get_user_by_id(self, user_id):
        return self.user_repository.get(user_id)

    def get_all_users(self):
        return self.user_repository.get_all()

    # Similarly, implement methods for other entities
```

**Explanation:**

- **Consistency in Facade:** The Facade's interface with the repository remains unchanged, making the transition seamless.
- **Entity-Specific Repositories:** The Facade initializes specific repositories for each entity, ensuring that the correct SQLAlchemy model is used.

#### Benefits of Using an Interface

By adhering to the `Repository` interface, the Facade and other components of your application are insulated from the specific details of data storage. This means:

- **Seamless Transition:** You can switch from in-memory storage to a database-backed solution without rewriting the core logic of your application.
- **Future Flexibility:** If you decide to switch to a different database or storage solution later, you can do so with minimal changes to your codebase, provided the new solution adheres to the same interface.

#### Conclusion

The transition from in-memory persistence to database persistence is a significant step in scaling your HBnB project. By leveraging the repository pattern and SQLAlchemy, you can ensure that your application remains modular, maintainable, and ready for production. The interface-based design you've implemented so far will make this transition smooth, maintaining the integrity and consistency of your codebase.

### Task1: Modify the User Model to Include Password Hashing

#### Objective
Update the `User` model to securely store a hashed password using **bcrypt**. Modify the user registration endpoint to accept the `password` field and ensure that it is hashed before storing it. The password should **not** be returned in any `GET` requests.

#### Context
In previous tasks, the `User` model was created, but it did not handle passwords. In this task, you will enhance the `User` model to support password hashing using **bcrypt**, ensuring passwords are securely stored. Additionally, you will update the user registration endpoint to accept and hash passwords before storing them. Passwords will not be returned in any `GET` requests.

#### Instructions

1. **Install the `flask-bcrypt` plugin**
   - In your `requirements.txt` file, add the following line:
     ```
     flask-bcrypt
     ```
   - Run the following command to install it:
     ```bash
     pip install flask-bcrypt
     ```

2. **Register the plugin within the Application**
   - In the `app/__init__.py` file:
     - Import `Bcrypt` from `flask_bcrypt` package and instantiate it.

       ```python
       from flask_bcrypt import Bcrypt

       bcrypt = Bcrypt()
       ```

     - Initialize the instance in the `create_app()` function.
       ```python
       def create_app(config_class=config.DevelopmentConfig):
          #
          # Existent code with app Flask instance
          # ...
          bcrypt.init_app(app)
       ```

2. **Update the `User` Model to Include Password Hashing**
   - In the `models/user.py` file:
      - update the `User` class to include a `password` attribute. This field will store the hashed version of the user's password.

   - Implement the following methods in the `User` class:
     - **hash_password(password):** This function should take a plaintext password, hash it using **bcrypt**, and store the hashed version in the `password` field.

       ```python
       def hash_password(self, password):
           """Hashes the password before storing it."""
           self.password = bcrypt.generate_password_hash(password).decode('utf-8')
       ```

     - **verify_password(password):** This function should compare a plaintext password with the hashed password stored in the `password` field, returning `True` if they match and `False` otherwise.

       ```python
       def verify_password(self, password):
           """Verifies if the provided password matches the hashed password."""
           return bcrypt.check_password_hash(self.password, password)
       ```

3. **Modify the User Registration Endpoint (`POST /api/v1/users/`)**
   - Modify the user registration endpoint to accept a `password` field in addition to the first name, last name, and email.
   - Ensure that the `password` is hashed using the `hash_password` function before storing the user in the repository.
   - After registering the user, do **not** return the password in the response. You will only return the user's ID and a success message.

4. **Modify the User Retrieval Endpoint (`GET /api/v1/users/<user_id>`)**
   - Update the `GET` endpoint to **exclude** the `password` from the response when retrieving a user's details.

5. **Test the Password Hashing Logic**
   - Use Postman or cURL to test the POST /api/v1/users/ endpoint, ensuring that the password is hashed and not returned in the response.
   - Verify that the GET /api/v1/users/<user_id> endpoint does not expose the password field.

#### Resources
- **Flask-Bcrypt Documentation:** [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/)
- **Password Hashing Best Practices:** [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

#### Expected Outcome
By the end of this task, the `User` model will securely hash and store passwords using **bcrypt**. The `POST /api/v1/users/` endpoint will accept passwords and securely hash them before storing. Passwords will not be returned in any `GET` requests.

### Task2: Implement JWT Authentication with `flask-jwt-extended`

#### Objective
Set up JWT-based authentication for the HBnB application, enabling secure login functionality. This task involves configuring the API to generate and verify JWT tokens using the `flask-jwt-extended` extension. Tokens will be issued upon successful login and required for accessing protected endpoints.

#### Context
JWT (JSON Web Token) allows secure authentication by providing a token that clients can use to access protected resources without having to re-authenticate on every request. JWT is stateless, meaning the server doesn’t need to store user sessions, making it ideal for scalable applications. JWT tokens also allow embedding additional claims (such as user roles), which is useful for authorization.

In this task, we will set up user login, issue JWT tokens, and use these tokens to protect specific API endpoints.

Here is a **Mermaid.js diagram** that shows the interaction between the client and the API for obtaining a JWT token and using it to make authenticated requests:

##### Adding a Middleware

In Flask, **middleware** is software that sits between the request and the final handling of that request by your Flask routes. Middleware can manipulate requests, responses, or both.

In the context of JWT authentication, middleware is responsible for verifying the JWT token with each incoming request. Flask-JWT-Extended provides decorators like `@jwt_required()` that act as middleware, ensuring that a valid token is present before allowing access to protected resources.

- **What does middleware do in JWT?**:
Middleware intercepts the request and checks if the token is present and valid. If the token is invalid or missing, the middleware prevents the request from reaching the route handler and instead returns an error response.

- **How does Flask-JWT-Extended handle this?**:
Flask-JWT-Extended makes use of decorators such as `@jwt_required()` and `@jwt_optional()`. These decorators ensure that protected routes are only accessible if the user has a valid token.

```mermaid
sequenceDiagram
    participant Client
    participant API
    participant JWTManager

    Client->>+API: POST /api/v1/auth/login (email, password)
    API->>+JWTManager: Validate credentials and generate JWT
    JWTManager-->>-API: Returns JWT token
    API-->>-Client: Returns JWT token in response

    Client->>+API: GET /api/v1/protected (Authorization: Bearer JWT)
    API->>+JWTManager: Validate JWT token
    JWTManager-->>-API: Valid token, return user info
    API-->>-Client: Protected data response
```

This sequence diagram visualizes the flow where:

1. **Client Login Request**:
   - The client initiates the login process by sending a `POST` request to the API endpoint (`/api/v1/auth/login`). In the request, the client provides the user's credentials (email and password).

2. **API and JWT Token Generation**:
   - The API checks the provided credentials, and if they are valid, the API uses the **JWTManager** to generate a JWT (JSON Web Token). This token is a secure representation of the user’s identity, containing claims like `is_admin` and an expiration time.

3. **JWT Token Response**:
   - The API responds to the client with the generated JWT token. The token is sent in the body of the response and is used by the client to authenticate further API requests.

4. **Client Makes Authenticated Requests**:
   - After obtaining the JWT token, the client sends another request to a protected endpoint (e.g., `GET /api/v1/protected`). This time, the request includes the token in the `Authorization` header as `Bearer JWT_TOKEN`.

5. **JWT Token Validation**:
   - The API uses the **JWTManager** to validate the token. If the token is valid (not expired, tampered with, or revoked), the API proceeds to process the request.

6. **Protected Resource Access**:
   - Upon successful validation, the API returns the protected data. If the token is invalid or expired, the API responds with an error message, often a `401 Unauthorized` response.

---

#### Instructions

1. **Install the `flask-jwt-extended` Library**
   - In your `requirements.txt` file, add the following line:
     ```
     flask-jwt-extended
     ```
   - Run the following command to install it:
     ```bash
     pip install flask-jwt-extended
     ```

2. **Configure JWT in the Flask Application**
   - In the `app/__init__.py` file, import and instantiate the `JWTManager` class provided by `flask-jwt-extended` to enable JWT handling in your Flask application.

     ```python
     from flask_jwt_extended import JWTManager

     jwt = JWTManager()
     ```

   - In the `create_app()` function, register the middleware with the application instance.

     ```python
     def create_app(config_class=config.DevelopmentConfig):
          #
          # Existent code with app Flask instance
          # ...
         jwt.init_app(app)

     ```

     > [!IMPORTANT]
     > The `flask-jwt-extended` uses a key stored in [`JWT_SECRET_KEY`](https://flask-jwt-extended.readthedocs.io/en/stable/options.html#JWT_SECRET_KEY) for securely signing the session cookie.
     > In this project we're going to use Flask's [SECRET_KEY](https://flask.palletsprojects.com/en/stable/config/#SECRET_KEY) that we've already set in the Configuration Class and can also be used by the plugin.

3. **Create a Login Endpoint (`POST /api/v1/login`)**
   - The login endpoint will authenticate the user, generate a JWT token, and return it to the client. The token will include the user's `id` and `is_admin` claim to differentiate between regular users and admins.

   - In `api/v1/auth.py`, create the following endpoint:
     ```python
     from flask_restx import Namespace, Resource, fields
     from flask_jwt_extended import create_access_token
     from app.services import facade

     api = Namespace('auth', description='Authentication operations')

     # Model for input validation
     login_model = api.model('Login', {
         'email': fields.String(required=True, description='User email'),
         'password': fields.String(required=True, description='User password')
     })

     @api.route('/login')
     class Login(Resource):
         @api.expect(login_model)
         def post(self):
             """Authenticate user and return a JWT token"""
             credentials = api.payload  # Get the email and password from the request payload

             # Step 1: Retrieve the user based on the provided email
             user = facade.get_user_by_email(credentials['email'])

             # Step 2: Check if the user exists and the password is correct
             if not user or not user.verify_password(credentials['password']):
                 return {'error': 'Invalid credentials'}, 401

             # Step 3: Create a JWT token with the user's id and is_admin flag
             access_token = create_access_token(identity={'id': str(user.id), 'is_admin': user.is_admin})

             # Step 4: Return the JWT token to the client
             return {'access_token': access_token}, 200
     ```

   **Explanation:**
   - `create_access_token`: This function generates a JWT token. The token includes an **identity**, which in this case is a dictionary containing the `user.id` and `is_admin` flag. This allows the token to carry claims that we can later use for authorization.
   - **Token Claims**: By adding claims like `id` and `is_admin` to the token, we can embed information about the user's identity and permissions within the token itself. This way, we don't need to query the database for every request to check if a user is an admin.

   **Steps Breakdown:**
   - **Step 1**: Retrieve the user by email using the `get_user_by_email` method from the `HBnBFacade`. This method will query the repository (in-memory or database, depending on the part of the project) for a user with the provided email.
   - **Step 2**: Use the `verify_password` method (which should have been implemented in the `User` model) to check if the provided password matches the hashed password stored in the repository.
   - **Step 3**: If the credentials are valid, generate a JWT token with the `create_access_token` function. We embed the `user.id` and `is_admin` flag as part of the token claims, allowing us to identify the user and their role in subsequent requests.
   - **Step 4**: Return the generated token to the client as part of the response body. This token can be used by the client to authenticate future requests.

4. **Protect Endpoints with JWT**
   - Once the JWT is generated, you can protect sensitive API endpoints by requiring that the user include the token in the `Authorization` header of their request. Use the `@jwt_required()` decorator to enforce this.

   Example:
   ```python
   from flask_jwt_extended import jwt_required, get_jwt_identity

   @api.route('/protected')
   class ProtectedResource(Resource):
       @jwt_required()
       def get(self):
           """A protected endpoint that requires a valid JWT token"""
           current_user = get_jwt_identity()  # Retrieve the user's identity from the token
           return {'message': f'Hello, user {current_user["id"]}'}, 200
   ```

   **Explanation:**
   - **@jwt_required()**: This decorator ensures that the endpoint can only be accessed if a valid JWT is provided in the request. If the token is missing or invalid, the request will be rejected.
   - **get_jwt_identity()**: This function extracts the identity (in this case, the `user.id` and `is_admin` claims) from the token. We can then use this information to personalize responses or enforce role-based access.

5. **Test the Authentication Flow**
   Use `curl` to test the login and authentication functionality:

   **Login and Get JWT:**
   ```bash
   curl -X POST "http://127.0.0.1:5000/api/v1/auth/login" -H "Content-Type: application/json" -d '{
     "email": "john.doe@example.com",
     "password": "your_password"
   }'
   ```
   **Expected Response:**
   ```json
   {
       "access_token": "your_generated_jwt_token"
   }
   ```

   **Access a Protected Endpoint:**
   ```bash
   curl -X GET "http://127.0.0.1:5000/api/v1/protected" -H "Authorization: Bearer your_generated_jwt_token"
   ```
   **Expected Response:**
   ```json
   {
       "message": "Hello, user 3fa85f64-5717-4562-b3fc-2c963f66afa6"
   }
   ```

#### Resources
- **JWT Authentication**: [JWT.io](https://jwt.io/)
- **Flask-JWT-Extended Documentation:** [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
- **JWT Best Practices:** [OWASP JWT Security](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_Cheat_Sheet_for_Java.html)

#### Expected Outcome
By the end of this task, students will have implemented user login functionality using JWT. They will be able to generate and verify JWT tokens, protect specific API endpoints, and embed claims (like `is_admin`) within the token for future authorization checks.

### Task4: Implement Authenticated User Access Endpoints

#### Objective
Secure various API endpoints to allow only authenticated users to perform specific actions, including creating and modifying places and reviews, as well as updating their own user details. Access will be controlled via JWT authentication, with additional validation to ensure users can only modify data that belongs to them (e.g., places they own, reviews they created).

#### Context
Authenticated user access is a critical part of securing an API. By ensuring that only authorized users can perform specific actions, the integrity of the data is protected. This task focuses on securing endpoints related to creating and modifying places and reviews, while also allowing users to modify their own data.

In this task, you will:
1. Secure endpoints to ensure only authenticated users can create, update, and delete resources.
2. Add logic to validate ownership of places and reviews.
3. Implement logic to prevent users from reviewing places they own or reviewing a place multiple times.
4. Verify that public users can access the **PUBLIC** endpoints without a JWT token.

---

#### Instructions

1. **Secure the Endpoints with JWT Authentication**
   The following endpoints will be protected by JWT authentication, and additional validation will be added to ensure that users can only modify their own data:

   - **POST /api/v1/places/**: Create a new place.
   - **PUT /api/v1/places/<place_id>**: Update a place's details. Only the owner of the place can modify its information.
   - **POST /api/v1/reviews/**: Create a new review. Users can only review places they do **not** own and can only create **one** review per place.
   - **PUT /api/v1/reviews/<review_id>**: Update a review. Users can only modify reviews they created.
   - **DELETE /api/v1/reviews/<review_id>**: Delete a review. Users can only delete reviews they created.
   - **PUT /api/v1/users/<user_id>**: Modify user information. Users can only modify their own details (excluding email and password).

2. **Identify Public Endpoints**
   - The following endpoints will be publicly accessible:
     - **GET** `/api/v1/places/`: Retrieve a list of available places.
     - **GET** `/api/v1/places/<place_id>`: Retrieve detailed information about a specific place.

3. **Implement the Logic for JWT Authentication**
   Use the `@jwt_required()` decorator from `flask-jwt-extended` to enforce JWT authentication on the above endpoints. The `get_jwt_identity()` function will be used to identify the currently logged-in user.

   **Example:**
   ```python
   from flask_restx import Namespace, Resource, fields
   from flask_jwt_extended import jwt_required, get_jwt_identity

   api = Namespace('places', description='Place operations')

   @api.route('/')
   class PlaceList(Resource):
       @jwt_required()
       def post(self):
           """Create a new place"""
           current_user = get_jwt_identity()
           # Logic to create a new place for the logged-in user
           pass
   ```

4. **Validation Logic**

   - **Create Place (POST /api/v1/places/):**
     - Ensure the user is authenticated.
     - The `owner_id` of the place must be set to the ID of the authenticated user (retrieved using `get_jwt_identity()`).

    **Example:**
    ```python
    @api.route('/<place_id>')
    class PlaceResource(Resource):
        @jwt_required()
        def put(self, place_id):
            current_user = get_jwt_identity()
            place = facade.get_place(place_id)
            if place.owner_id != current_user:
                return {'error': 'Unauthorized action'}, 403
            # Logic to update the place
            pass
    ```

   - **Update Place (PUT /api/v1/places/<place_id>):**
     - Ensure the user is authenticated.
     - Check that the `owner_id` of the place matches the ID of the authenticated user.
     - If the user is not the owner, return a 403 error with the message "Unauthorized action."

   - **Create Review (POST /api/v1/reviews/):**
     - Ensure the user is authenticated.
     - Check that the `place_id` in the request belongs to a place the user does **not** own.
     - Check that the user has not already reviewed this place.
     - If the user is the owner of the place, return a 400 error with the message "You cannot review your own place."
     - If the user has already reviewed the place, return a 400 error with the message "You have already reviewed this place."

   - **Update Review (PUT /api/v1/reviews/<review_id>):**
     - Ensure the user is authenticated.
     - Check that the `user_id` of the review matches the authenticated user.
     - If the user did not create the review, return a 403 error with the message "Unauthorized action."

   - **Delete Review (DELETE /api/v1/reviews/<review_id>):**
     - Ensure the user is authenticated.
     - Check that the `user_id` of the review matches the authenticated user.
     - If the user did not create the review, return a 403 error with the message "Unauthorized action."

   - **Modify User Information (PUT /api/v1/users/<user_id>):**
     - Ensure the user is authenticated.
     - Check that the `user_id` in the URL matches the authenticated user.
     - Prevent the user from modifying their `email` and `password` in this endpoint.
     - If the user tries to modify their email or password, return a 400 error with the message "You cannot modify email or password."
     - If the user is trying to modify another user's data, return a 403 error with the message "Unauthorized action."

---

5. **Test the Authenticated Endpoints**

   Use Postman or cURL to test these authenticated endpoints. Ensure that unauthorized actions (e.g., modifying a place that the user does not own) return the appropriate error messages.

   **Test Place Creation (POST /api/v1/places/):**
   ```bash
   curl -X POST "http://127.0.0.1:5000/api/v1/places/" -d '{"title": "New Place"}' -H "Authorization: Bearer <your_token>" -H "Content-Type: application/json"
   ```

   **Test Unauthorized Place Update (PUT /api/v1/places/<place_id>):**
   ```bash
   curl -X PUT "http://127.0.0.1:5000/api/v1/places/<place_id>" -d '{"title": "Updated Place"}' -H "Authorization: Bearer <your_token>" -H "Content-Type: application/json"
   ```

   **Expected Response for Unauthorized Action:**
   ```json
   {
       "error": "Unauthorized action"
   }
   ```

   **Test Creating a Review (POST /api/v1/reviews/):**
   ```bash
   curl -X POST "http://127.0.0.1:5000/api/v1/reviews/" -d '{"place_id": "<place_id>", "text": "Great place!"}' -H "Authorization: Bearer <your_token>" -H "Content-Type: application/json"
   ```

   **Test Updating a Review (PUT /api/v1/reviews/<review_id>):**
   ```bash
   curl -X PUT "http://127.0.0.1:5000/api/v1/reviews/<review_id>" -d '{"text": "Updated review"}' -H "Authorization: Bearer <your_token>" -H "Content-Type: application/json"
   ```

   **Test Deleting a Review (DELETE /api/v1/reviews/<review_id>):**
   ```bash
   curl -X DELETE "http://127.0.0.1:5000/api/v1/reviews/<review_id>" -H "Authorization: Bearer <your_token>"
   ```

   **Test Modifying User Data (PUT /api/v1/users/<user_id>):**
   ```bash
   curl -X PUT "http://127.0.0.1:5000/api/v1/users/<user_id>" -d '{"first_name": "Updated Name"}' -H "Authorization: Bearer <your_token>" -H "Content-Type: application/json"
   ```

6. **Test the Public Endpoints**
   - Test the endpoints to verify they can be accessed without a JWT token.

   **Example Test Using cURL:**
   - Retrieve a list of places:
     ```bash
     curl -X GET "http://127.0.0.1:5000/api/v1/places/"
     ```

   **Expected Response:**
   ```json
   [
       {
           "id": "1fa85f64-5717-4562-b3fc-2c963f66afa6",
           "title": "Cozy Apartment",
           "price": 100.0
       },
       {
           "id": "2fa85f64-5717-4562-b3fc-2c963f66afa6",
           "title": "Luxury Condo",
           "price": 200.0
       }
   ]
   ```

   - Retrieve detailed information about a specific place:
     ```bash
     curl -X GET "http://127.0.0.1:5000/api/v1/places/1fa85f64-5717-4562-b3fc-2c963f66afa6"
     ```

   **Expected Response:**
   ```json
   {
       "id": "1fa85f64-5717-4562-b3fc-2c963f66afa6",
       "title": "Cozy Apartment",
       "description": "A comfortable and affordable place to stay.",
       "price": 100.0,
       "latitude": 37.7749,
       "longitude": -122.4194
   }
   ```

---

#### Resources

1. **Flask-JWT-Extended Documentation:** [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
2. **Testing REST APIs with cURL:** [Everything cURL](https://everything.curl.dev/)

---

#### Expected Outcome

By the end of this task, the following endpoints will be secured, allowing only authenticated users to perform actions based on their ownership of places and reviews:
- Create, update, and delete places (with ownership checks).
- Create and update reviews (with restrictions on reviewing owned places and duplicate reviews).
- Modify user details (excluding email and password).

### Task5: Implement Administrator Access Endpoints

#### Objective
Restrict access to specific API endpoints so that only users with administrative privileges can perform certain actions. These actions include creating new users, modifying any user's details (including email and password), and adding or modifying amenities. Additionally, administrators can perform the same tasks as authenticated users without being restricted by ownership of places and reviews.

#### Context
Role-based access control (RBAC) is crucial in API security. Administrators have the highest level of privileges, and this task will allow them to bypass restrictions that regular users face. This includes the ability to manage any user or resource in the system.

In this task, you will:
1. Implement logic for restricting access to specific endpoints based on the user's role (`is_admin`).
2. Ensure that administrators can manage user accounts, including creating and modifying user details.
3. Allow administrators to bypass ownership restrictions for places and reviews.

---

#### Instructions

1. **Define Administrator Permissions**
   The following endpoints will be restricted to administrators only:
   - **POST /api/v1/users/**: Create a new user.
   - **PUT /api/v1/users/<user_id>**: Modify a user's details, including email and password.
   - **POST /api/v1/amenities/**: Add a new amenity.
   - **PUT /api/v1/amenities/<amenity_id>**: Modify the details of an amenity.

   Administrators will also be able to:
   - Modify or delete any place or review, bypassing the ownership restrictions that regular users face.

2. **Add Role-Based Access Control (RBAC)**
   Use the `@jwt_required()` decorator to ensure that only authenticated users can access these endpoints. The `get_jwt()` function retrieves the JWT claims, allowing you to check the `is_admin` flag.

   **Example for Checking Admin Status:**
   ```python
   from flask_restx import Namespace, Resource
   from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

   api = Namespace('admin', description='Admin operations')

   @api.route('/users/<user_id>')
   class AdminUserResource(Resource):
       @jwt_required()
       def put(self, user_id):
           current_user = get_jwt_identity()

           # If 'is_admin' is part of the identity payload
           if not current_user.get('is_admin'):
               return {'error': 'Admin privileges required'}, 403

           data = request.json
           email = data.get('email')

           if email:
               # Check if email is already in use
               existing_user = facade.get_user_by_email(email)
               if existing_user and existing_user.id != user_id:
                   return {'error': 'Email is already in use'}, 400

           # Logic to update user details, including email and password
           pass
   ```

3. **Implement Endpoint Logic**

   - **Create User (POST /api/v1/users/):**
     Administrators can create new users. The email must be unique.
     ```python
     @api.route('/users/')
     class AdminUserCreate(Resource):
         @jwt_required()
         def post(self):
             current_user = get_jwt_identity()
             if not current_user.get('is_admin'):
                 return {'error': 'Admin privileges required'}, 403

             user_data = request.json
             email = user_data.get('email')

             # Check if email is already in use
             if facade.get_user_by_email(email):
                 return {'error': 'Email already registered'}, 400

             # Logic to create a new user
             pass
     ```

   - **Modify User (PUT /api/v1/users/<user_id>):**
     Administrators can modify any user, including changing the email and password, but must ensure that the email is not duplicated.
     ```python
     @api.route('/users/<user_id>')
     class AdminUserModify(Resource):
         @jwt_required()
         def put(self, user_id):
             current_user = get_jwt_identity()
             if not current_user.get('is_admin'):
                 return {'error': 'Admin privileges required'}, 403

             data = request.json
             email = data.get('email')

             # Ensure email uniqueness
             if email:
                 existing_user = facade.get_user_by_email(email)
                 if existing_user and existing_user.id != user_id:
                     return {'error': 'Email already in use'}, 400

             # Logic to update user details
             pass
     ```

   - **Add Amenity (POST /api/v1/amenities/):**
     ```python
     @api.route('/amenities/')
     class AdminAmenityCreate(Resource):
         @jwt_required()
         def post(self):
             current_user = get_jwt_identity()
             if not current_user.get('is_admin'):
                 return {'error': 'Admin privileges required'}, 403

             # Logic to create a new amenity
             pass
     ```

   - **Modify Amenity (PUT /api/v1/amenities/<amenity_id>):**
     ```python
     @api.route('/amenities/<amenity_id>')
     class AdminAmenityModify(Resource):
         @jwt_required()
         def put(self, amenity_id):
             current_user = get_jwt_identity()
             if not current_user.get('is_admin'):
                 return {'error': 'Admin privileges required'}, 403

             # Logic to update an amenity
             pass
     ```

4. **Allow Admins to Bypass Ownership Restrictions**
   When an admin attempts to modify or delete a place or review, ownership checks will be bypassed.

   **Example for Modifying a Place (PUT /api/v1/places/<place_id>):**
   ```python
   @api.route('/places/<place_id>')
   class AdminPlaceModify(Resource):
       @jwt_required()
       def put(self, place_id):
           current_user = get_jwt_identity()

           # Set is_admin default to False if not exists
           is_admin = current_user.get('is_admin', False)
           user_id = current_user.get('id')

           place = facade.get_place(place_id)
           if not is_admin and place.owner_id != user_id:
               return {'error': 'Unauthorized action'}, 403

           # Logic to update the place
           pass
   ```

5. **Test the Admin Endpoints**

    > [!IMPORTANT] Unauthorized action
    > At this point, you should have realized that you'll need a user with administrative permissions to test the admin endpoints.
    > Discuss different strategies with your team to overcome this problem.

   - **Create a New User as an Admin:**
     ```bash
     curl -X POST "http://127.0.0.1:5000/api/v1/users/" -d '{"email": "newuser@example.com", "first_name": "Admin", "last_name": "User"}' -H "Authorization: Bearer <admin_token>" -H "Content-Type: application/json"
     ```

   - **Modify Another User’s Data as an Admin:**
     ```bash
     curl -X PUT "http://127.0.0.1:5000/api/v1/users/<user_id>" -d '{"email": "updatedemail@example.com"}' -H "Authorization: Bearer <admin_token>" -H "Content-Type: application/json"
     ```

   - **Add a New Amenity as an Admin:**
     ```bash
     curl -X POST "http://127.0.0.1:5000/api/v1/amenities/" -d '{"name": "Swimming Pool"}' -H "Authorization: Bearer <admin_token>" -H "Content-Type: application/json"
     ```

   - **Modify an Amenity as an Admin:**
     ```bash
     curl -X PUT "http://127.0.0.1:5000/api/v1/amenities/<amenity_id>" -d '{"name": "Updated Amenity"}' -H "Authorization: Bearer <admin_token>" -H "Content-Type: application/json"
     ```

---

#### Resources

1. **Flask-JWT-Extended Documentation:** [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
2. **Bcrypt Documentation:** [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/)

#### Expected Outcome
By the end of this task, admins will be able to:
- Create new users.
- Modify any user’s data, including email and password (with validation for unique emails).
- Add and modify amenities.
- Bypass ownership restrictions on places and reviews.

### Task6: Implement SQLAlchemy Repository

#### Objective
Replace the in-memory repository with a SQLAlchemy-based repository for persistence. In this task, you will create the `SQLAlchemyRepository` and integrate it into the project for managing database interactions. This task will lay the foundation for further model mapping and database setup in subsequent tasks.

#### Context
In the previous parts of the project, the persistence layer was managed using an in-memory repository. This task introduces SQLAlchemy to persist data in an SQLite database during development, preparing the application for a production-ready relational database. The repository pattern remains the same, but the implementation will now interact with SQLAlchemy for all CRUD operations. Due to the fact that the database has not yet been initialized, this task focuses only on creating the repository. Model mapping and database initialization will follow in the next task.

You will:
1. Create the SQLAlchemy repository that implements the existing repository interface.
2. Refactor the existing Facade to utilize the SQLAlchemy-based repository for user operations.
3. Provide code and detailed instructions for integration, but no database initialization will be performed yet.

> [!IMPORTANT]
> Read this guide before start:  [Transitioning from In-Memory to Database Persistence: A Step-by-Step Guide](./concept-memory_to_db.md)

---

#### Instructions

1. **Set Up SQLAlchemy in the Project**

   - Add the necessary dependencies for SQLAlchemy to your `requirements.txt`:
     ```txt
     sqlalchemy
     flask-sqlalchemy
     ```

   - Initialize SQLAlchemy in `app/__init__.py`, but note that database initialization (e.g., table creation) will happen in the next task:
     ```python
     from flask import Flask
     from flask_sqlalchemy import SQLAlchemy

     db = SQLAlchemy()

     def create_app(config_class=config.DevelopmentConfig):
         #
         # Existent code with app Flask instance
         #
         db.init_app(app)

         # ...
     ```

2. **Add configuration parameters for SQLAlchemy**

   - Add the following configuration keys to the `DevelopmentConfig` Class in the `config.py` file
     ```python
     import os

     class Config:
         SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
         DEBUG = False

     class DevelopmentConfig(Config):
         DEBUG = True
         SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'
         SQLALCHEMY_TRACK_MODIFICATIONS = False

     config = {
         'development': DevelopmentConfig,
         'default': DevelopmentConfig
     }
     ```

   - `SQLALCHEMY_DATABASE_URI`: Sets the URI for the SQLite database.
   - `SQLALCHEMY_TRACK_MODIFICATIONS`: Disables tracking of object modifications, which is a feature that can consume additional memory.

2. **Create the SQLAlchemy Repository**

   - The `SQLAlchemyRepository` class will implement the `Repository` interface from **app/persistence/repository.py**, which was provided in the earlier tasks of the project.
   - The repository will handle database CRUD operations using SQLAlchemy, adhering to the same structure as the in-memory repository.

   ```python
   from app import db

   class SQLAlchemyRepository(Repository):
       def __init__(self, model):
           self.model = model

       def add(self, obj):
           db.session.add(obj)
           db.session.commit()

       def get(self, obj_id):
           return self.model.query.get(obj_id)

       def get_all(self):
           return self.model.query.all()

       def update(self, obj_id, data):
           obj = self.get(obj_id)
           if obj:
               for key, value in data.items():
                   setattr(obj, key, value)
               db.session.commit()

       def delete(self, obj_id):
           obj = self.get(obj_id)
           if obj:
               db.session.delete(obj)
               db.session.commit()

       def get_by_attribute(self, attr_name, attr_value):
           return self.model.query.filter_by(**{attr_name: attr_value}).first()
   ```

   - This `SQLAlchemyRepository` will be flexible and reusable for different entities in the project (e.g., `User`, `Place`, `Review`).

3. **Refactor the Facade**

   - The Facade class should now rely on the `SQLAlchemyRepository` for interacting with the database. Since no model mapping or database initialization has occurred yet, only the structure will be set up for now.
   - Refactor the `HBnBFacade` in `app/services/facade.py` to replace the in-memory repository with the SQLAlchemy-based repository:

     ```python
     from app.models.user import User
     from app.persistence.repository import SQLAlchemyRepository

     class HBnBFacade:
         def __init__(self):
             self.user_repo = SQLAlchemyRepository(User)

         def create_user(self, user_data):
             user = User(**user_data)
             self.user_repo.add(user)
             return user

         def get_user(self, user_id):
             return self.user_repo.get(user_id)
     ```

4. **Hold Off on Database Testing**
   - **Important:** Since the models have not been mapped yet, you will not be able to fully test or initialize the database at this stage. In the next task, the `User` model will be mapped to the database, at which point you can create tables and initialize the database schema.
   - The testing and verification of the persistence layer will be covered once the model mapping is complete.

---

#### Resources

- **SQLAlchemy Documentation:** [SQLAlchemy](https://docs.sqlalchemy.org/en/20/)
- **Flask-SQLAlchemy Documentation:** [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

---

#### Expected Outcome
By the end of this task, you will have implemented the `SQLAlchemyRepository` and refactored the Facade to use this new repository for data persistence. However, since the model mapping and database initialization will be performed in the next task, the actual integration testing will be delayed until the next step.

### Task7: Map the User Entity to SQLAlchemy Model

#### Objective
Map the `User` entity to a SQLAlchemy model, ensuring the correct database relationships, attribute definitions, and CRUD operations are implemented. You will incorporate the ORM functionality within the repository layer, service layer (Facade), and API layer for full integration. The password hashing mechanism from the previous task should remain functional.

#### Context
In the previous task, the repository was updated to use SQLAlchemy for database persistence, replacing the in-memory repository. This task extends that functionality by mapping the `User` entity to the database using SQLAlchemy. The new `UserRepository` will be responsible for handling user-specific queries, enhancing the flexibility and maintainability of the application.
As we're also using a BaseClass to handle the common attributes for all the Business Logic classes, we'll update this class first to manage the mapping.

In this task, you will:
1. Map the `BaseModel` class to a SQLAlchemy model, including the `id`, `created_at` and `updated_at` attributes.
2. Map the `User` entity to a SQLAlchemy model, including attributes like `first_name`, `last_name`, `email`, `password`, and `is_admin`.
3. Implement the `UserRepository` class to interact with the database using SQLAlchemy.
4. Refactor the `Facade` to use the `UserRepository` for user-related operations.

---

#### Instructions


1. **Map the BaseModel class**

   In the `models/baseclass.py` file, define the `BaseModel` class as a SQLAlchemy model:
   - Each attribute (e.g., `id`, `created_at`, `updated_at`) should map to a column in the database.
   - Add relevant constraints such as Primary keys or default values.

    ```python
    from app import db
    import uuid
    from datetime import datetime

    class BaseModel(db.Model):
        __abstract__ = True  # This ensures SQLAlchemy does not create a table for BaseModel

        id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
        created_at = db.Column(db.DateTime, default=datetime.utcnow)
        updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

        # ...
    ```

2. **Map the User Entity**

   In the `models/user.py` file, define the `User` class to inherit from `BaseModel` (also a SQLAlchemy model):
   - Each attribute (e.g., `first_name`, `last_name`, `email`, `password`, `is_admin`) should map to a column in the database.
   - Add relevant constraints such as `unique=True` for the `email` column to ensure no duplicate emails are allowed.

   **Example:**
   ```python
   from app import db, bcrypt
   import uuid
   from .base_model import BaseModel  # Import BaseModel from its module

   class User(BaseModel):
        __tablename__ = 'users'

        first_name = db.Column(db.String(50), nullable=False)
        last_name = db.Column(db.String(50), nullable=False)
        email = db.Column(db.String(120), nullable=False, unique=True)
        password = db.Column(db.String(128), nullable=False)
        is_admin = db.Column(db.Boolean, default=False)

       def hash_password(self, password):
           """Hash the password before storing it."""
           self.password = bcrypt.generate_password_hash(password).decode('utf-8')

       def verify_password(self, password):
           """Verify the hashed password."""
           return bcrypt.check_password_hash(self.password, password)
   ```

> [!NOTE]
> At this point you've already developed some methods (probably setters) to validate the Entities input attributes. You can also add specific validators for SQLAlchemy using the [`validates()` decorator](https://docs.sqlalchemy.org/en/20/orm/mapped_attributes.html).
> Be sure to read [this section about using Descriptors and Hybrids](https://docs.sqlalchemy.org/en/20/orm/mapped_attributes.html#using-descriptors-and-hybrids)

3. **Implement the UserRepository**

   Instead of relying solely on the generic `SQLAlchemyRepository`, create a specific `UserRepository` class that extends from the base repository.

   Creating a specific `UserRepository` class offers several key benefits:

   1. **Entity-Specific Behavior**: While `SQLAlchemyRepository` provides the basic CRUD operations, different entities often require unique operations or queries that are specific to their domain. For instance, the `UserRepository` might need to implement operations like finding a user by email or checking for password reset conditions, which are unique to the user entity. A custom `UserRepository` can encapsulate these entity-specific behaviors, making the code cleaner and more maintainable.
   2. **Encapsulation of Business Logic**: A specific `UserRepository` helps encapsulate user-related logic that interacts with the database in one place. It allows for better code organization by keeping `User`-related queries in their own repository, thus avoiding bloating the generic repository with complex user-specific queries.
   3. **Extensibility**: If new features or more complex logic are needed for the `User` entity (like authentication, logging, or role management), a dedicated repository class makes it easier to extend functionality in the future. This structure allows for better scaling and customization without cluttering the core repository.
   4. **Separation of Concerns**: A specialized `UserRepository` maintains the repository pattern’s principle of separating data access logic from the business logic. This keeps the business layer agnostic to changes in how the data is persisted or queried while still allowing user-specific operations to remain isolated.

   By creating a dedicated `UserRepository`, you achieve a more focused, maintainable, and extendable architecture, especially when working with entities that require specific behaviors beyond generic CRUD operations.

   **Example:**
   ```python
   from app.models.user import User
   from app import db
   from app.persistence.repository import SQLAlchemyRepository

   class UserRepository(SQLAlchemyRepository):
       def __init__(self):
           super().__init__(User)

       def get_user_by_email(self, email):
           return self.model.query.filter_by(email=email).first()
   ```

   **Explanation:**
   - `get_user_by_email`: This method allows you to search for a user by email, something specific to the `User` entity. This kind of custom behavior is what makes having a dedicated `UserRepository` useful over the generic repository.

4. **Refactor the Facade to Use the UserRepository**

   Update the `HBnBFacade` class to use the newly created `UserRepository` for all user-related operations, ensuring that the facade communicates with the database through the repository layer.

   **Example:**
   ```python
   from app.services.repositories.user_repository import UserRepository

   class HBnBFacade:
       def __init__(self):
           self.user_repo = UserRepository()

       def create_user(self, user_data):
           user = User(**user_data)
           user.hash_password(user_data['password'])
           self.user_repo.add(user)
           return user

       def get_user(self, user_id):
           return self.user_repo.get(user_id)

       def get_user_by_email(self, email):
           return self.user_repo.get_user_by_email(email)
   ```

   **Explanation:**
   - `create_user`: When creating a user, the password is hashed before saving the user in the database.
   - `get_user_by_email`: This method uses the `UserRepository`'s `get_user_by_email` function to retrieve users by email.

5. **Initialize the Database and Test the Integration**

   Now that the `User` model is defined and the repository is set up, you need to initialize the database to create the `users` table.

   - To initialize the database and create the table, run:
     ```bash
     flask shell
     >>> from app import db
     >>> db.create_all()
     ```

   - Test user creation and retrieval using Postman or cURL. For example, create a new user:
     ```bash
     curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{
       "first_name": "John",
       "last_name": "Doe",
       "email": "john.doe@example.com",
       "password": "password123"
     }'
     ```

   - Then retrieve the user by ID:
     ```bash
     curl -X GET "http://127.0.0.1:5000/api/v1/users/<user_id>"
     ```

---

#### Resources
1. **SQLAlchemy Documentation:** [SQLAlchemy](https://docs.sqlalchemy.org/en/20/)
2. **Flask-SQLAlchemy Documentation:** [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
3. **Flask-Bcrypt Documentation:** [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/)
4. **Testing REST APIs with cURL:** [Everything cURL](https://everything.curl.dev/)

#### Expected Outcome
By the end of this task, the `User` entity will be fully mapped to a SQLAlchemy model, and the repository pattern will be updated to interact with the database using SQLAlchemy. You will have refactored the `Facade` to use the new `UserRepository`, and the application will now store user data in the database persistently.

### Task8: Map the Place, Review, and Amenity Entities

#### Objective
Map the `Place`, `Review`, and `Amenity` entities to SQLAlchemy models. This task requires you to apply the knowledge gained from mapping the `User` entity in the previous task to these new entities. You will implement the core database attributes for each entity, and in subsequent tasks, relationships between entities will be defined. No relationships between these entities should be added at this point.

#### Context
In the previous tasks, you mapped the `User` entity and implemented the `UserRepository` to interact with the database through SQLAlchemy. Now, you will extend this mapping to the `Place`, `Review`, and `Amenity` entities. These mappings will prepare the foundation for the relationships that will be added later between places, reviews, amenities, and users.

In this task, you will:
1. Map the core attributes for `Place`, `Review`, and `Amenity` entities.
2. Ensure that each entity has basic CRUD functionality through the repository pattern.
3. Follow the same process you used to map the `User` entity in the previous tasks.

---

#### Instructions

1. **Map the Place, Review, and Amenity Entities**

   - Use SQLAlchemy to map the core attributes of the `Place`, `Review`, and `Amenity` entities.
   - For each entity, define the SQLAlchemy model with the appropriate attributes, making sure to assign primary keys and relevant constraints (e.g., `nullable=False` for required fields).

> [!WARNING]
> Do **not** include relationships between entities yet (these will be added later).

   The attributes for each entity and their expected data types are as follows:
   - **Place:**
     - `id` (Integer): Unique identifier (primary key).
     - `title` (String): Title of the place.
     - `description` (String): Description of the place.
     - `price` (Float): Price per night.
     - `latitude` (Float): Latitude of the place.
     - `longitude` (Float): Longitude of the place.

   - **Review:**
     - `id` (Integer): Unique identifier (primary key).
     - `text` (String): Text of the review.
     - `rating` (Integer): Rating (from 1 to 5).

   - **Amenity:**
     - `id` (Integer): Unique identifier (primary key).
     - `name` (String): Name of the amenity.

2. **Follow the Same Steps as the `User` Entity**
   Just as you mapped the `User` entity in the previous task, apply the same structure for defining models, repositories, and facade methods for `Place`, `Review`, and `Amenity`. These models should now be persisted in the database using SQLAlchemy.

> [!IMPORTANT]
> You should provide valid entities when calling the API to comply with the Business Logic rules, but they shouldn't be mapped or persisted yet.

3. **Test the Entity Mappings**
   - Initialize the database using `flask shell` and `db.create_all()` after defining your models to create the corresponding tables.
   - Use Postman or cURL to test CRUD operations (Create, Read, Update, Delete) for each entity. This can be done similarly to how you tested the `User` entity.

---

#### Resources
1. **SQLAlchemy Documentation:** [SQLAlchemy](https://docs.sqlalchemy.org/en/20/)
2. **Flask-SQLAlchemy Documentation:** [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
3. **SQLAlchemy Relationship Patterns:** [SQLAlchemy ORM Relationships](https://docs.sqlalchemy.org/en/20/orm/relationships.html)

---

#### Expected Outcome
By the end of this task, you should have mapped the `Place`, `Review`, and `Amenity` entities to SQLAlchemy models, ensuring that their basic attributes are stored in the database. The repositories and facade methods should be updated to handle CRUD operations for each entity. No relationships between entities should be implemented yet; this will be done in a later task.

### Task9: Map Relationships Between Entities Using SQLAlchemy

#### Objective
Map the relationships between the entities using SQLAlchemy. You will define both one-to-many and many-to-many relationships and apply the appropriate constraints and foreign keys in the models. This task will serve as a foundation for linking related data in your application.

#### Context
Now that you have defined the core entities like `User`, `Place`, `Review`, and `Amenity`, it's time to establish relationships between these entities. These relationships reflect the connections between the real-world concepts represented by the entities (e.g., a `User` can own many `Places`, a `Place` can have many `Reviews`). Defining relationships in the database ensures that related data can be easily queried and manipulated in a structured way.

In this task, you will define relationships between the entities, using SQLAlchemy’s ORM capabilities. Relationships like "one-to-many" and "many-to-many" allow for a clear and efficient organization of data, enforcing the logical structure of the database.

---

#### Explanation: Handling Relationships with SQLAlchemy

SQLAlchemy provides an intuitive way to define relationships between tables using `relationship()` in combination with foreign key constraints (`ForeignKey`). It supports various types of relationships, such as one-to-many and many-to-many, which allow for flexible and powerful querying between related data.

**Core SQLAlchemy relationship attributes:**

- **`backref`:** This creates a reverse relationship automatically. It adds a new property to the referenced table, allowing you to easily traverse the relationship from both sides.
- **`lazy`:** This determines when SQLAlchemy loads related data. Common options include:
  - `select`: Load related data when the parent object is accessed.
  - `subquery`: Load all related objects using a separate query when the parent object is accessed.

---

##### **1. One-to-Many Relationships**

In a one-to-many relationship, one record in a table can have many associated records in another table. For example, a customer may place many orders, but each order is associated with one customer.

**Example:**
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class Parent(db.Model):
    __tablename__ = 'parents'
    id = Column(Integer, primary_key=True)
    children = relationship('Child', backref='parent', lazy=True)

class Child(db.Model):
    __tablename__ = 'children'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parents.id'), nullable=False)
```

**Explanation:**
- A `Parent` can have many `Child` objects, but each `Child` has only one `Parent`.
- The `backref` argument in `relationship()` creates a bidirectional link, so you can access all children of a parent using `parent.children`.
- The `lazy=True` ensures that related `Child` objects are loaded when accessed, allowing you to query and work with related data easily.

---

##### **2. Many-to-Many Relationships**

In a many-to-many relationship, multiple records in one table can be related to multiple records in another table. For example, a student can enroll in multiple courses, and a course can have multiple students enrolled. As you already should know, this cannot be modeled directly in a Relational Database without [adding an additional table](https://help.claris.com/en/pro-help/content/many-to-many-relationships.html). For SQLAlchemy be able to relate this data, the [associate table should also be mapped](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#many-to-many).

**Example:**
```python
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app import db

# Association table for many-to-many relationship
student_course = db.Table('student_course',
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

class Student(db.Model):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    courses = relationship('Course', secondary=student_course, lazy='subquery',
                           backref=db.backref('students', lazy=True))

class Course(db.Model):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    course_name = Column(String, nullable=False)
```

**Explanation:**
- The `student_course` table is an association table that links `Student` and `Course`. Each entry in the table represents an enrollment of a student in a course.
- In the `Student` class, the `relationship()` function uses the `secondary` argument to point to the `student_course` association table, creating the many-to-many relationship.
- The `backref` in this example allows access from `Course` to its associated `students` through `course.students`.

---

#### Instructions

Now that you understand how SQLAlchemy handles relationships, you will map the relationships between entities such as `User`, `Place`, `Review`, and `Amenity` in your project.

##### **1. Relationships to Implement**

You need to implement the following relationships in your models:

- **User and Place (One-to-Many):** A `User` can create many `Places`, but each `Place` is associated with only one `User`.
- **Place and Review (One-to-Many):** A `Place` can have many `Reviews`, but each `Review` is associated with only one `Place`.
- **User and Review (One-to-Many):** A `User` can write many `Reviews`, but each `Review` is written by one `User`.
- **Place and Amenity (Many-to-Many):** A `Place` can have many `Amenities`, and an `Amenity` can be associated with many `Places`.

##### **2. Implement Relationships in Your Entities**

Using SQLAlchemy, you will define these relationships by adding foreign keys and using `relationship()` to create associations between models. Here's what you need to do for each relationship:

- **User and Place:**
  - Add a foreign key (`user_id`) in the `Place` model to reference the `User`.
  - Use `relationship()` in both models to link them.

- **Place and Review:**
  - Add a foreign key (`place_id`) in the `Review` model to reference the `Place`.
  - Use `relationship()` to establish the one-to-many relationship between `Place` and `Review`.

- **User and Review:**
  - Add a foreign key (`user_id`) in the `Review` model to reference the `User`.
  - Use `relationship()` to link `User` and `Review`.

- **Place and Amenity:**
  - Create an association table to manage the many-to-many relationship between `Place` and `Amenity`.
  - Use `relationship()` in both `Place` and `Amenity` to manage the connection through the association table.

##### **3. Test the Relationships**

After defining the relationships, you should test them using Postman or cURL. Be sure to test both ends of the relationships (e.g., retrieving a user's places, getting reviews for a place).

1. Initialize the database with `flask shell`:
   ```bash
   flask shell
   >>> from app import db
   >>> db.create_all()
   ```

2. Use Postman or cURL to create and link entities such as places, reviews, and amenities, verifying the relationships

---

#### Resources
1. **SQLAlchemy Documentation:** [SQLAlchemy](https://docs.sqlalchemy.org/en/14/)
2. **Flask-SQLAlchemy Documentation:** [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
3. **SQLAlchemy Relationship Patterns:** [SQLAlchemy ORM Relationships](https://docs.sqlalchemy.org/en/20/orm/relationships.html)

---

#### Expected Outcome

By the end of this task, you will have successfully mapped the relationships between entities using SQLAlchemy. These relationships will ensure data integrity and allow efficient querying of related data, enabling complex operations such as retrieving all reviews for a place or all places owned by a user. The correct use of `relationship()`, `backref`, and foreign keys will establish clear, bidirectional links between your entities.

### Task10: SQL Scripts for Table Generation and Initial Data

#### Objective
Create SQL scripts to generate the entire database schema for the HBnB project and populate it with initial data. The scripts should include all tables and relationships necessary to reflect the project’s model and insert the required initial data.

#### Context
In this task, you will focus on designing the database schema using raw SQL to generate tables and insert initial data. This includes creating tables for `User`, `Place`, `Review`, `Amenity`, and their relationships. The purpose of this task is to practice defining databases independently of any ORM, ensuring you understand how to design tables and relationships at the SQL level.

#### Instructions

1. **Generate SQL Scripts for Table Creation**

   Define SQL scripts for each of the following tables:

   - **User Table**:
     - `id`: `CHAR(36) PRIMARY KEY` (UUID format).
     - `first_name`: `VARCHAR(255)`.
     - `last_name`: `VARCHAR(255)`.
     - `email`: `VARCHAR(255) UNIQUE`.
     - `password`: `VARCHAR(255)`.
     - `is_admin`: `BOOLEAN DEFAULT FALSE`.

   - **Place Table**:
     - `id`: `CHAR(36) PRIMARY KEY` (UUID format).
     - `title`: `VARCHAR(255)`.
     - `description`: `TEXT`.
     - `price`: `DECIMAL(10, 2)`.
     - `latitude`: `FLOAT`.
     - `longitude`: `FLOAT`.
     - `owner_id`: `CHAR(36)` (Foreign key referencing `User(id)`).

   - **Review Table**:
     - `id`: `CHAR(36) PRIMARY KEY` (UUID format).
     - `text`: `TEXT`.
     - `rating`: `INT` (Between 1 and 5).
     - `user_id`: `CHAR(36)` (Foreign key referencing `User(id)`).
     - `place_id`: `CHAR(36)` (Foreign key referencing `Place(id)`).
     - Add a **unique constraint** on the combination of `user_id` and `place_id` to ensure that a user can only leave one review per place.

   - **Amenity Table**:
     - `id`: `CHAR(36) PRIMARY KEY` (UUID format).
     - `name`: `VARCHAR(255) UNIQUE`.

   - **Place_Amenity Table** (Many-to-Many relationship):
     - `place_id`: `CHAR(36)` (Foreign key referencing `Place(id)`).
     - `amenity_id`: `CHAR(36)` (Foreign key referencing `Amenity(id)`).
     - Add a **composite primary key** for `place_id` and `amenity_id`.

   **Ensure that**:
   - Foreign key constraints are correctly established for relationships.
   - UUIDs are properly generated for the `id` fields.

2. **Insert Initial Data**

   Insert initial data into the database using SQL `INSERT` statements:

   - **Administrator User**:
     - `id`: `36c9050e-ddd3-4c3b-9731-9f487208bbc1` (This ID is fixed).
     - `email`: `admin@hbnb.io`
     - `first_name`: `Admin`
     - `last_name`: `HBnB`
     - `password`: Hash the password `admin1234` using bcrypt2 (use a script or tool to generate the hash).
     - `is_admin`: `True`

   - **Initial Amenities**:
     Insert the following amenities into the `Amenity` table with a randomly generated UUID:
     - WiFi
     - Swimming Pool
     - Air Conditioning

     Generate the `UUID4` values for each `id` using an online UUID generator or a Python script.

3. **Test the SQL Scripts**

   - **Table Creation**: Ensure the tables are created successfully, with all constraints and relationships in place.
   - **Data Insertion**: Verify that the initial data is inserted correctly, ensuring the password is stored in hashed format.

   **Test CRUD Operations**:
   - Use `SELECT`, `INSERT`, `UPDATE`, and `DELETE` statements to test data integrity and CRUD functionality for each table.
   - Verify that the admin user is created with `is_admin = TRUE` and that the amenities are inserted correctly.

---

#### Resources
- **SQL Tutorial for Beginners**: [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)

#### Expected Outcome
By the end of this task, you should have:
- SQL scripts that generate the full database schema.
- Inserted an administrator user and amenities into the database.
- Tested CRUD operations to verify correct functionality of the schema and data.

### Task11: Generate Database Diagrams

#### Objective
Create Entity-Relationship (ER) diagrams to visually represent the structure of the database schema for the HBnB project using **Mermaid.js**. This task will help ensure that the database schema is accurately reflected and consistent with previous parts of the project. Students will use Mermaid.js to visualize tables and their relationships in a readable format.

#### Context
Visualizing database relationships is crucial for understanding the connections between entities. ER diagrams provide a high-level overview of the database's structure and serve as an essential reference for further development or debugging. Mermaid.js is a tool that allows you to create these diagrams in markdown-like syntax, making it easy to integrate them into documentation and collaboration platforms like GitHub or GitLab.

In this task, students will:
1. Learn to use Mermaid.js to create ER diagrams.
2. Generate diagrams that represent the `User`, `Place`, `Review`, `Amenity`, and `Place_Amenity` tables, along with their relationships.
3. Ensure consistency in the schema visualization, using Mermaid.js as the primary tool for diagram generation.

---

### Instructions

1. **Learn the Mermaid.js Syntax for ER Diagrams**

   Mermaid.js allows the generation of diagrams through simple text-based syntax. In this case, we'll focus on creating **ER diagrams** to visualize the structure of a relational database.

   Below is a general example of Mermaid.js syntax for an ER diagram:

   ```mermaid
   erDiagram
       PERSON {
           int id
           string first_name
           string last_name
           date birth_date
       }

       ADDRESS {
           int id
           string street
           string city
           string postal_code
       }

       COMPANY {
           int id
           string name
       }

       PERSON ||--o{ ADDRESS : has
       COMPANY ||--o{ PERSON : employs
   ```

   **Explanation**:
   - `PERSON`, `ADDRESS`, and `COMPANY` are entities (tables) in the database.
   - The `||--o{` notation is used to represent relationships:
     - `||` signifies a one-to-one relationship.
     - `o{` signifies a one-to-many relationship.
   - The attributes inside each entity represent the columns in the table, with types such as `int`, `string`, and `date`.

2. **Generate the Database Diagram for HBnB**

   After learning the syntax, create an ER diagram representing the core entities from your HBnB project: `User`, `Place`, `Review`, `Amenity`, and `Place_Amenity`.

   **Entities to include**:

   - **User**
     - Attributes: `id`, `first_name`, `last_name`, `email`, `password`, `is_admin`

   - **Place**
     - Attributes: `id`, `title`, `description`, `price`, `latitude`, `longitude`, `owner_id`
     - Relationships: `Place` has a foreign key `owner_id` referencing the `User` table.

   - **Review**
     - Attributes: `id`, `text`, `rating`, `user_id`, `place_id`
     - Relationships: `Review` has foreign keys `user_id` (references `User`) and `place_id` (references `Place`).

   - **Amenity**
     - Attributes: `id`, `name`

   - **Place_Amenity** (A join table to represent the many-to-many relationship between `Place` and `Amenity`)
     - Attributes: `place_id`, `amenity_id`
     - Relationships:
       - `Place_Amenity` has two foreign keys:
         - `place_id` (references `Place`)
         - `amenity_id` (references `Amenity`)

3. **Generate and Export the Diagram**

   After writing the Mermaid.js code for the ER diagram:

   - Use an online editor like [Mermaid Live Editor](https://mermaid-js.github.io/mermaid-live-editor/) to visualize your diagram.
   - Export the diagram as an image (e.g., PNG or SVG) for documentation purposes.

   You can also integrate Mermaid diagrams into platforms such as GitHub by including the diagram code directly in your markdown files.

4. **Test Your Understanding**

   To ensure you understand how relationships work, modify the diagram to include potential new entities, such as a `Reservation` or `Booking` table, and how they might relate to `User` and `Place`.

---

#### Resources

- **Mermaid.js Documentation**: [Mermaid.js Official Docs](https://mermaid-js.github.io/mermaid/)
- **Live Mermaid.js Editor**: [Mermaid Live Editor](https://mermaid-js.github.io/mermaid-live-editor/)
- **SQLAlchemy Relationship Documentation**: [SQLAlchemy ORM Relationships](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html)

---

#### Expected Outcome

By the end of this task, you should have:

- Created an ER diagram in Mermaid.js that accurately represents the database schema for HBnB.
- Understood the various types of relationships (one-to-many, many-to-many) and how they are represented visually.
- Exported the diagram to be included in your project documentation.


## PART4
### TASK Part4:
### Part 4 - Simple Web Client

In this phase, you'll be focusing on the front-end development of your application using HTML5, CSS3, and JavaScript ES6. Your task is to design and implement an interactive user interface that connects with the back-end services you have developed in previous parts of the project.

#### Objectives

- Develop a user-friendly interface following provided design specifications.
- Implement client-side functionality to interact with the back-end API.
- Ensure secure and efficient data handling using JavaScript.
- Apply modern web development practices to create a dynamic web application.

#### Learning Goals

- Understand and apply HTML5, CSS3, and JavaScript ES6 in a real-world project.
- Learn to interact with back-end services using AJAX/Fetch API.
- Implement authentication mechanisms and manage user sessions.
- Use client-side scripting to enhance user experience without page reloads.

#### Tasks Breakdown

1. **Design (Task 1)**
   - Complete provided HTML and CSS files to match the given design specifications.
   - Create pages for Login, List of Places, Place Details, and Add Review.

2. **Login (Task 2)**
   - Implement login functionality using the back-end API.
   - Store the JWT token returned by the API in a cookie for session management.

3. **List of Places (Task 3)**
   - Implement the main page to display a list of all places.
   - Fetch places data from the API and implement client-side filtering based on country selection.
   - Ensure the page redirects to the login page if the user is not authenticated.

4. **Place Details (Task 4)**
   - Implement the detailed view of a place.
   - Fetch place details from the API using the place ID.
   - Provide access to the add review form if the user is authenticated.

5. **Add Review (Task 5)**
   - Implement the form to add a review for a place.
   - Ensure the form is accessible only to authenticated users, redirecting others to the index page.

> [!WARNING]
> When testing your client against yout API you'll probably get a Cross-Origin Resource Sharing (CORS) error. You'll need to modify your API code to allow your client to fetch data from the API.
> Read [this article](https://medium.com/@mterrano1/cors-in-a-flask-api-38051388f8cc) for a depper understanding about CORS and how to configure your Flask API

#### Resources

- [HTML5 Documentation](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
- [CSS3 Documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
- [JavaScript ES6 Features](https://developer.mozilla.org/en-US/docs/Web/JavaScript/New_in_JavaScript/ECMAScript_2015)
- [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [Responsive Web Design Basics](https://web.dev/responsive-web-design-basics/)
- [Handling Cookies in JavaScript](https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie)
- [Client-Side Form Validation](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation)

---
task__00__design.md
### Task: Generate Database Diagrams

#### Objective
Create Entity-Relationship (ER) diagrams to visually represent the structure of the database schema for the HBnB project using **Mermaid.js**. This task will help ensure that the database schema is accurately reflected and consistent with previous parts of the project. Students will use Mermaid.js to visualize tables and their relationships in a readable format.

#### Context
Visualizing database relationships is crucial for understanding the connections between entities. ER diagrams provide a high-level overview of the database's structure and serve as an essential reference for further development or debugging. Mermaid.js is a tool that allows you to create these diagrams in markdown-like syntax, making it easy to integrate them into documentation and collaboration platforms like GitHub or GitLab.

In this task, students will:
1. Learn to use Mermaid.js to create ER diagrams.
2. Generate diagrams that represent the `User`, `Place`, `Review`, `Amenity`, and `Place_Amenity` tables, along with their relationships.
3. Ensure consistency in the schema visualization, using Mermaid.js as the primary tool for diagram generation.

---

### Instructions

1. **Learn the Mermaid.js Syntax for ER Diagrams**

   Mermaid.js allows the generation of diagrams through simple text-based syntax. In this case, we'll focus on creating **ER diagrams** to visualize the structure of a relational database.

   Below is a general example of Mermaid.js syntax for an ER diagram:

   ```mermaid
   erDiagram
       PERSON {
           int id
           string first_name
           string last_name
           date birth_date
       }

       ADDRESS {
           int id
           string street
           string city
           string postal_code
       }

       COMPANY {
           int id
           string name
       }

       PERSON ||--o{ ADDRESS : has
       COMPANY ||--o{ PERSON : employs
   ```

   **Explanation**:
   - `PERSON`, `ADDRESS`, and `COMPANY` are entities (tables) in the database.
   - The `||--o{` notation is used to represent relationships:
     - `||` signifies a one-to-one relationship.
     - `o{` signifies a one-to-many relationship.
   - The attributes inside each entity represent the columns in the table, with types such as `int`, `string`, and `date`.

2. **Generate the Database Diagram for HBnB**

   After learning the syntax, create an ER diagram representing the core entities from your HBnB project: `User`, `Place`, `Review`, `Amenity`, and `Place_Amenity`.

   **Entities to include**:

   - **User**
     - Attributes: `id`, `first_name`, `last_name`, `email`, `password`, `is_admin`

   - **Place**
     - Attributes: `id`, `title`, `description`, `price`, `latitude`, `longitude`, `owner_id`
     - Relationships: `Place` has a foreign key `owner_id` referencing the `User` table.

   - **Review**
     - Attributes: `id`, `text`, `rating`, `user_id`, `place_id`
     - Relationships: `Review` has foreign keys `user_id` (references `User`) and `place_id` (references `Place`).

   - **Amenity**
     - Attributes: `id`, `name`

   - **Place_Amenity** (A join table to represent the many-to-many relationship between `Place` and `Amenity`)
     - Attributes: `place_id`, `amenity_id`
     - Relationships:
       - `Place_Amenity` has two foreign keys:
         - `place_id` (references `Place`)
         - `amenity_id` (references `Amenity`)

3. **Generate and Export the Diagram**

   After writing the Mermaid.js code for the ER diagram:

   - Use an online editor like [Mermaid Live Editor](https://mermaid-js.github.io/mermaid-live-editor/) to visualize your diagram.
   - Export the diagram as an image (e.g., PNG or SVG) for documentation purposes.

   You can also integrate Mermaid diagrams into platforms such as GitHub by including the diagram code directly in your markdown files.

4. **Test Your Understanding**

   To ensure you understand how relationships work, modify the diagram to include potential new entities, such as a `Reservation` or `Booking` table, and how they might relate to `User` and `Place`.

---

#### Resources

- **Mermaid.js Documentation**: [Mermaid.js Official Docs](https://mermaid-js.github.io/mermaid/)
- **Live Mermaid.js Editor**: [Mermaid Live Editor](https://mermaid-js.github.io/mermaid-live-editor/)
- **SQLAlchemy Relationship Documentation**: [SQLAlchemy ORM Relationships](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html)

---

#### Expected Outcome

By the end of this task, you should have:

- Created an ER diagram in Mermaid.js that accurately represents the database schema for HBnB.
- Understood the various types of relationships (one-to-many, many-to-many) and how they are represented visually.
- Exported the diagram to be included in your project documentation.

task__01__login.md
### Task: Generate Database Diagrams

#### Objective
Create Entity-Relationship (ER) diagrams to visually represent the structure of the database schema for the HBnB project using **Mermaid.js**. This task will help ensure that the database schema is accurately reflected and consistent with previous parts of the project. Students will use Mermaid.js to visualize tables and their relationships in a readable format.

#### Context
Visualizing database relationships is crucial for understanding the connections between entities. ER diagrams provide a high-level overview of the database's structure and serve as an essential reference for further development or debugging. Mermaid.js is a tool that allows you to create these diagrams in markdown-like syntax, making it easy to integrate them into documentation and collaboration platforms like GitHub or GitLab.

In this task, students will:
1. Learn to use Mermaid.js to create ER diagrams.
2. Generate diagrams that represent the `User`, `Place`, `Review`, `Amenity`, and `Place_Amenity` tables, along with their relationships.
3. Ensure consistency in the schema visualization, using Mermaid.js as the primary tool for diagram generation.

---

### Instructions

1. **Learn the Mermaid.js Syntax for ER Diagrams**

   Mermaid.js allows the generation of diagrams through simple text-based syntax. In this case, we'll focus on creating **ER diagrams** to visualize the structure of a relational database.

   Below is a general example of Mermaid.js syntax for an ER diagram:

   ```mermaid
   erDiagram
       PERSON {
           int id
           string first_name
           string last_name
           date birth_date
       }

       ADDRESS {
           int id
           string street
           string city
           string postal_code
       }

       COMPANY {
           int id
           string name
       }

       PERSON ||--o{ ADDRESS : has
       COMPANY ||--o{ PERSON : employs
   ```

   **Explanation**:
   - `PERSON`, `ADDRESS`, and `COMPANY` are entities (tables) in the database.
   - The `||--o{` notation is used to represent relationships:
     - `||` signifies a one-to-one relationship.
     - `o{` signifies a one-to-many relationship.
   - The attributes inside each entity represent the columns in the table, with types such as `int`, `string`, and `date`.

2. **Generate the Database Diagram for HBnB**

   After learning the syntax, create an ER diagram representing the core entities from your HBnB project: `User`, `Place`, `Review`, `Amenity`, and `Place_Amenity`.

   **Entities to include**:

   - **User**
     - Attributes: `id`, `first_name`, `last_name`, `email`, `password`, `is_admin`

   - **Place**
     - Attributes: `id`, `title`, `description`, `price`, `latitude`, `longitude`, `owner_id`
     - Relationships: `Place` has a foreign key `owner_id` referencing the `User` table.

   - **Review**
     - Attributes: `id`, `text`, `rating`, `user_id`, `place_id`
     - Relationships: `Review` has foreign keys `user_id` (references `User`) and `place_id` (references `Place`).

   - **Amenity**
     - Attributes: `id`, `name`

   - **Place_Amenity** (A join table to represent the many-to-many relationship between `Place` and `Amenity`)
     - Attributes: `place_id`, `amenity_id`
     - Relationships:
       - `Place_Amenity` has two foreign keys:
         - `place_id` (references `Place`)
         - `amenity_id` (references `Amenity`)

3. **Generate and Export the Diagram**

   After writing the Mermaid.js code for the ER diagram:

   - Use an online editor like [Mermaid Live Editor](https://mermaid-js.github.io/mermaid-live-editor/) to visualize your diagram.
   - Export the diagram as an image (e.g., PNG or SVG) for documentation purposes.

   You can also integrate Mermaid diagrams into platforms such as GitHub by including the diagram code directly in your markdown files.

4. **Test Your Understanding**

   To ensure you understand how relationships work, modify the diagram to include potential new entities, such as a `Reservation` or `Booking` table, and how they might relate to `User` and `Place`.

---

#### Resources

- **Mermaid.js Documentation**: [Mermaid.js Official Docs](https://mermaid-js.github.io/mermaid/)
- **Live Mermaid.js Editor**: [Mermaid Live Editor](https://mermaid-js.github.io/mermaid-live-editor/)
- **SQLAlchemy Relationship Documentation**: [SQLAlchemy ORM Relationships](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html)

---

#### Expected Outcome

By the end of this task, you should have:

- Created an ER diagram in Mermaid.js that accurately represents the database schema for HBnB.
- Understood the various types of relationships (one-to-many, many-to-many) and how they are represented visually.
- Exported the diagram to be included in your project documentation.

task__02__index.md
#### Objectives

- Implement the main page to display a list of all places.
- Fetch places data from the API and implement client-side filtering based on price.
- Show the login link only if the user is not authenticated.

#### Requirements

- Use the provided HTML structure in `index.html` to display the list of places.
- Make an AJAX request to the API to fetch the list of places.
- Populate the places list dynamically using JavaScript.
- Implement a client-side filter to allow users to filter places by price without reloading the page.
- Show or hide the login link based on user authentication.

#### Instructions

1. **Check User Authentication**:
   - On page load, check if the user is authenticated by verifying the presence of the JWT token in cookies.
   - If the token is not found, show the login link.
   - If the token is found, hide the login link.
   - Tip: Use a function to get the value of a cookie by its name.

2. **Fetch Places Data**:
   - Use the Fetch API to send a GET request to the endpoint that returns the list of places.
   - Ensure the request includes the JWT token for authentication if available.
   - Tip: Include the token in the `Authorization` header of your request.

3. **Populate Places List**:
   - Dynamically create HTML elements to display each place's information (e.g., name, description, location).
   - Append these elements to the `#places-list` section.
   - Tip: Use `document.createElement` and `element.innerHTML` to build the place elements.

4. **Implement Client-Side Filtering**:
   - Add an event listener to the price filter dropdown.
   - Filter the displayed places based on the selected price.
   - Ensure the filtering works without reloading the page.
   - Tip: Use `element.style.display` to show or hide places based on the filter.

#### Example Guidance

**scripts.js**

- **Check user authentication**:
  - Create a function to check for the JWT token in cookies and control the visibility of the login link.

  ```
  function checkAuthentication() {
      const token = getCookie('token');
      const loginLink = document.getElementById('login-link');

      if (!token) {
          loginLink.style.display = 'block';
      } else {
          loginLink.style.display = 'none';
          // Fetch places data if the user is authenticated
          fetchPlaces(token);
      }
  }
  function getCookie(name) {
      // Function to get a cookie value by its name
      // Your code here
  }
  ```

- **Fetch places data**:
  - Use the Fetch API to get the list of places and handle the response.

  ```
  async function fetchPlaces(token) {
      // Make a GET request to fetch places data
      // Include the token in the Authorization header
      // Handle the response and pass the data to displayPlaces function
  }
  ```

- **Populate places list**:

  - Create HTML elements for each place and append them to the `#places-list`.

  ```
  function displayPlaces(places) {
      // Clear the current content of the places list
      // Iterate over the places data
      // For each place, create a div element and set its content
      // Append the created element to the places list
  }
  ```

- **Implement client-side filtering**:
  - Add an event listener to the price filter dropdown to filter places based on the selected price.
  - The filter will set the top price for the places to be shown.
  - The dropdown must be loaded with the following options:
    - 10
    - 50
    - 100
    - All


  ```
  document.getElementById('price-filter').addEventListener('change', (event) => {
      // Get the selected price value
      // Iterate over the places and show/hide them based on the selected price
  });
  ```

6. **Testing**:
   - Test the functionality by logging in and viewing the list of places.
   - Verify that the client-side filter works as expected.
   - Ensure the login link appears only when the user is not authenticated.

#### Resources

- [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [Handling Cookies in JavaScript](https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie)
- [DOM Manipulation](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)


task__03__place.md
#### Objectives

- Implement the detailed view of a place.
- Fetch place details from the API using the place ID.
- Display detailed information about the place, including name, description, price, amenities and reviews.
- If the user is authenticated, provide access to the form for adding a review.

#### Requirements

- Use the provided HTML structure in `place.html` to display the detailed information of a place.
- Make an AJAX request to the API to fetch the details of the selected place.
- Populate the place details dynamically using JavaScript.
- Show the add review form only if the user is authenticated.

#### Instructions

1. **Get Place ID from URL**:
   - Extract the place ID from the URL query parameters.
   - Tip: Use `window.location.search` to get the query string.

2. **Check User Authentication**:
   - On page load, check if the user is authenticated by verifying the presence of the JWT token in cookies.
   - Store the token in a variable for later use in API requests.

3. **Fetch Place Details**:
   - Use the Fetch API to send a GET request to the endpoint that returns the details of the place.
   - Ensure the request includes the JWT token for authentication if available.
   - Tip: Include the token in the `Authorization` header of your request.

4. **Populate Place Details**:
   - Dynamically create HTML elements to display the place's detailed information (e.g., name, description, price, amenities and reviews).
   - Append these elements to the `#place-details` section.

5. **Show Add Review Form**:
   - If the user is authenticated, display the add review form.
   - Hide the form if the user is not authenticated.

#### Example Guidance

**scripts.js**

- **Get place ID from URL**:
  - Create a function to extract the place ID from the query parameters.

  ```javascript
  function getPlaceIdFromURL() {
      // Extract the place ID from window.location.search
      // Your code here
  }
  ```

- **Check user authentication**:
  - Create a function to check for the JWT token in cookies and store it in a variable.

  ```javascript
  function checkAuthentication() {
      const token = getCookie('token');
      const addReviewSection = document.getElementById('add-review');

      if (!token) {
          addReviewSection.style.display = 'none';
      } else {
          addReviewSection.style.display = 'block';
          // Store the token for later use
          fetchPlaceDetails(token, placeId);
      }
  }

  function getCookie(name) {
      // Function to get a cookie value by its name
      // Your code here
  }
  ```

- **Fetch place details**:
  - Use the Fetch API to get the details of the place and handle the response.

  ```javascript
  async function fetchPlaceDetails(token, placeId) {
      // Make a GET request to fetch place details
      // Include the token in the Authorization header
      // Handle the response and pass the data to displayPlaceDetails function
  }
  ```

- **Populate place details**:
  - Create HTML elements for the place details and append them to the `#place-details` section.

  ```javascript
  function displayPlaceDetails(place) {
      // Clear the current content of the place details section
      // Create elements to display the place details (name, description, price, amenities and reviews)
      // Append the created elements to the place details section
  }
  ```

6. **Testing**:
   - Test the functionality by navigating to the place details page and verifying the displayed information.
   - Ensure that the add review form appears only when the user is authenticated.

#### Resources

- [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [Handling Cookies in JavaScript](https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie)
- [DOM Manipulation](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)

task__04__add_review.md
#### Objectives

- Implement the form to add a review for a place.
- Ensure only authenticated users can submit reviews.
- Redirect unauthenticated users to the index page.
- Send the review data to the API endpoint and handle the response.

#### Requirements

- Use the provided HTML structure in `add_review.html` to create the review form.
- Make an AJAX request to the API to submit the review data.
- If the user is not authenticated, redirect them to the index page.
- Display a success message upon successful submission and handle errors appropriately.

#### Instructions

1. **Check User Authentication**:
   - On page load, check if the user is authenticated by verifying the presence of the JWT token in cookies.
   - If the token is not found, redirect the user to the index page.
   - Store the token in a variable for later use in API requests.

2. **Get Place ID from URL**:
   - Extract the place ID from the URL query parameters.
   - Tip: Use `window.location.search` to get the query string.

3. **Setup Event Listener for Review Form**:
   - Add an event listener to the review form to handle the form submission.
   - Use `preventDefault` to prevent the default form submission behavior.

4. **Make AJAX Request to Submit Review**:
   - Use the Fetch API to send a POST request to the endpoint that submits the review data.
   - Include the JWT token in the `Authorization` header.
   - Send the review text and place ID in the request body as a JSON object.

5. **Handle API Response**:
   - If the submission is successful, display a success message and clear the form.
   - If the submission fails, display an error message to the user.

#### Example Guidance

**scripts.js**

- **Check user authentication**:
  - Create a function to check for the JWT token in cookies and redirect unauthenticated users.

  ```javascript
  function checkAuthentication() {
      const token = getCookie('token');
      if (!token) {
          window.location.href = 'index.html';
      }
      return token;
  }

  function getCookie(name) {
      // Function to get a cookie value by its name
      // Your code here
  }
  ```

- **Get place ID from URL**:
  - Create a function to extract the place ID from the query parameters.

  ```javascript
  function getPlaceIdFromURL() {
      // Extract the place ID from window.location.search
      // Your code here
  }
  ```

- **Setup event listener for review form**:
  - Add an event listener for the form submission to handle the review data.

  ```javascript
  document.addEventListener('DOMContentLoaded', () => {
      const reviewForm = document.getElementById('review-form');
      const token = checkAuthentication();
      const placeId = getPlaceIdFromURL();

      if (reviewForm) {
          reviewForm.addEventListener('submit', async (event) => {
              event.preventDefault();
              // Get review text from form
              // Make AJAX request to submit review
              // Handle the response
          });
      }
  });
  ```

- **Make AJAX request to submit review**:
  - Use the Fetch API to send a POST request with the review data.

  ```javascript
  async function submitReview(token, placeId, reviewText) {
      // Make a POST request to submit review data
      // Include the token in the Authorization header
      // Send placeId and reviewText in the request body
      // Handle the response
  }
  ```

- **Handle API response**:
  - Display a success message if the submission is successful and clear the form.
  - Display an error message if the submission fails.

  ```javascript
  function handleResponse(response) {
      if (response.ok) {
          alert('Review submitted successfully!');
          // Clear the form
      } else {
          alert('Failed to submit review');
      }
  }
  ```

6. **Testing**:
   - Test the functionality by submitting reviews for a place as an authenticated user.
   - Verify that unauthenticated users are redirected to the index page.
   - Ensure that success and error messages are displayed appropriately.

#### Resources

- [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [Handling Cookies in JavaScript](https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie)
- [DOM Manipulation](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)
- [FormData API](https://developer.mozilla.org/en-US/docs/Web/API/FormData)
