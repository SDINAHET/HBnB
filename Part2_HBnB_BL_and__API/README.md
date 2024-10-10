!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="google" content="notranslate">
    <title>Project: HBnB - BL and API | Holberton Rennes, France Intranet</title>
      <link rel="stylesheet" href="https://use.typekit.net/xgz4ilr.css">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css">
      <link rel="stylesheet" media="all" href="/assets/application-68fac413f2c4d23a85e919ed5d02662578784fc099dd82e9b86a284109579b61.css" />
      <script src="https://www.gstatic.com/charts/loader.js"></script>
      <meta name="action-cable-url" content="/cable" />
      <script src="/assets/application-3a407075aefaefeee1ca133ceb43465083dcc4ed64b113a0deeb4869a4d7808a.js"></script>
      <link rel="shortcut icon" type="image/x-icon" href="/favicon.ico" />
      <meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="vRsABUyJbtlkYOrVn0uCzkAJZGIMUVvGbGCRk6G5LYl7l51bC-n-piBPSluYo62qa_P0QJQ46rD41XV5T96L1Q" />
      <link rel="apple-touch-icon" href="/apple-touch-icon.png">
      <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
      <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
        <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
      <![endif]-->
      <!-- Store user timezone -->
      <script>
        Cookies.set('timezone', (new Date()).getTimezoneOffset() / -60.0);
      </script>
      <!-- intro.js for interactive onboarding -->
        <script src="https://unpkg.com/intro.js/minified/intro.min.js"></script>
        <link rel="stylesheet" media="screen" href="https://unpkg.com/intro.js/minified/introjs.min.css" />
      <!-- React -->
      <script src="/packs/js/application-77628fd8c7309f6d4c21.js"></script>
      <link rel="stylesheet" media="screen" href="/packs/css/application-87456da7.css" />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"
    />
  </head>
  <body class="
    signed_in
    env_production

    "
    translate="no"
    class="notranslate"
    data-theme-suffix=""
    data-checker-special-theme="">
      <input type="hidden" id="hbtn-slack-url" value="https://holberton-school-org.slack.com">
      <nav class="navbar navbar-default navbar-fixed-top topbar visible-xs">
  <div class="navbar-header">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-mobile" aria-expanded="false">
      <span class="sr-only">Toggle navigation</span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
    </button>

    <a class="navbar-brand" href="/">
      <div class="logo"></div>
</a>  </div>

  <div class="collapse navbar-collapse navigation" id="navbar-mobile">
    <ul class="nav navbar-nav">

    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Help"><a target="_blank" href="https://students-support.hbtn.io/hc"><div class="icon "><i aria-hidden="true" class="fa fa-info-circle "></i></div><div class="visible-xs">Help</div></a></li>



    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-current-projects-item" title="Projects"><a href="/projects/current"><div class="icon "><i aria-hidden="true" class="fa fa-code-fork "></i></div><div class="visible-xs">Projects</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="My reports"><a href="/users/my_reports"><div class="icon "><i aria-hidden="true" class="fa fa-sticky-note-o "></i></div><div class="visible-xs">My reports</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="QA Reviews I can make"><a href="/corrections/to_review"><div class="icon "><i aria-hidden="true" class="fa fa-check "></i></div><div class="visible-xs">QA Reviews I can make</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Mock interviews"><a href="/dashboards/my_current_reefineries"><div class="icon "><i aria-hidden="true" class="fa fa-commenting-o "></i></div><div class="visible-xs">Mock interviews</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Evaluation quizzes"><a href="/dashboards/my_current_evaluation_quizzes"><div class="icon "><i aria-hidden="true" class="fa fa-question "></i></div><div class="visible-xs">Evaluation quizzes</div></a></li>

    <hr title="My resources">


    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-concepts-item" title="Concepts"><a href="/concepts"><div class="icon "><i aria-hidden="true" class="fa fa-file-text "></i></div><div class="visible-xs">Concepts</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Servers"><a href="/servers"><div class="icon "><i aria-hidden="true" class="fa fa-server "></i></div><div class="visible-xs">Servers</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-my-containers" title="Sandboxes"><a href="/user_sandboxes"><div class="icon "><i aria-hidden="true" class="fa fa-terminal "></i></div><div class="visible-xs">Sandboxes</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Tools"><a href="/dashboards/my_tools"><div class="icon "><i aria-hidden="true" class="fa fa-wrench "></i></div><div class="visible-xs">Tools</div></a></li>

      <hr title="My campus">


      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Peers"><a href="/users/peers"><div class="icon "><i aria-hidden="true" class="fa fa-users "></i></div><div class="visible-xs">Peers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Captain&#39;s Logs"><a href="/dashboards/my_captain_log"><div class="icon "><i aria-hidden="true" class="fa fa-book "></i></div><div class="visible-xs">Captain&#39;s Logs</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Officers"><a href="/dashboards/my_officers"><div class="icon "><i aria-hidden="true" class="fa fa-building "></i></div><div class="visible-xs">Officers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Speakers of the Day"><a href="/dashboards/my_speakers_of_the_day"><div class="icon "><i aria-hidden="true" class="fa fa-microphone "></i></div><div class="visible-xs">Speakers of the Day</div></a></li>


<hr class="visible-xs">

<li>
    <div
      data-container="body"
      data-placement="right"
      data-toggle="tooltip"
      title="Slack">
      <a target="_blank" href="https://holberton-school-org.slack.com">
        <div class="image slack">
          <div class="inner"></div>
        </div>
        <div class="visible-xs">Slack</div>
</a>    </div>

    <div
      data-container="body"
      data-placement="right"
      data-toggle="modal"
      data-target="#search-modal"
      title="Search">
      <a href="#">
          <div class="icon" data-toggle="tooltip" data-placement="right" data-container="body" title="Search">
            <i aria-hidden="true" class="fa fa-search "></i>
          </div>
        <div class="visible-xs">Search</div>
</a>    </div>

  <div
    data-container="body"
    data-placement="right"
    data-toggle="tooltip"
    title="My Profile">
    <a href="/users/my_profile">
        <div class="image ">
          <div class="inner" style="background-image: url('https://s3.eu-west-3.amazonaws.com/hbtn.intranet/users/photos/000/009/546/thumb/Capture_d%E2%80%99%C3%A9cran_2024-06-03_111954.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20241009%2Feu-west-3%2Fs3%2Faws4_request&amp;X-Amz-Date=20241009T194044Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=400443f89b37b3fe923afb83e9afd9c93f8526920d71f189c65850c03471308b')"></div>
        </div>

      <div class="visible-xs">My Profile</div>
</a>  </div>
</li>


    </ul>
  </div>
</nav>

      <div class="hidden-xs navigation sidebar">
  <a class="logo-container" href="/">
    <div class="logo"></div>
</a>
  <ul>

    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Help"><a target="_blank" href="https://students-support.hbtn.io/hc"><div class="icon "><i aria-hidden="true" class="fa fa-info-circle "></i></div><div class="visible-xs">Help</div></a></li>



    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-current-projects-item" title="Projects"><a href="/projects/current"><div class="icon "><i aria-hidden="true" class="fa fa-code-fork "></i></div><div class="visible-xs">Projects</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="My reports"><a href="/users/my_reports"><div class="icon "><i aria-hidden="true" class="fa fa-sticky-note-o "></i></div><div class="visible-xs">My reports</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="QA Reviews I can make"><a href="/corrections/to_review"><div class="icon "><i aria-hidden="true" class="fa fa-check "></i></div><div class="visible-xs">QA Reviews I can make</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Mock interviews"><a href="/dashboards/my_current_reefineries"><div class="icon "><i aria-hidden="true" class="fa fa-commenting-o "></i></div><div class="visible-xs">Mock interviews</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Evaluation quizzes"><a href="/dashboards/my_current_evaluation_quizzes"><div class="icon "><i aria-hidden="true" class="fa fa-question "></i></div><div class="visible-xs">Evaluation quizzes</div></a></li>

    <hr title="My resources">


    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-concepts-item" title="Concepts"><a href="/concepts"><div class="icon "><i aria-hidden="true" class="fa fa-file-text "></i></div><div class="visible-xs">Concepts</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Servers"><a href="/servers"><div class="icon "><i aria-hidden="true" class="fa fa-server "></i></div><div class="visible-xs">Servers</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-my-containers" title="Sandboxes"><a href="/user_sandboxes"><div class="icon "><i aria-hidden="true" class="fa fa-terminal "></i></div><div class="visible-xs">Sandboxes</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Tools"><a href="/dashboards/my_tools"><div class="icon "><i aria-hidden="true" class="fa fa-wrench "></i></div><div class="visible-xs">Tools</div></a></li>

      <hr title="My campus">


      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Peers"><a href="/users/peers"><div class="icon "><i aria-hidden="true" class="fa fa-users "></i></div><div class="visible-xs">Peers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Captain&#39;s Logs"><a href="/dashboards/my_captain_log"><div class="icon "><i aria-hidden="true" class="fa fa-book "></i></div><div class="visible-xs">Captain&#39;s Logs</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Officers"><a href="/dashboards/my_officers"><div class="icon "><i aria-hidden="true" class="fa fa-building "></i></div><div class="visible-xs">Officers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Speakers of the Day"><a href="/dashboards/my_speakers_of_the_day"><div class="icon "><i aria-hidden="true" class="fa fa-microphone "></i></div><div class="visible-xs">Speakers of the Day</div></a></li>


<hr class="visible-xs">

<li>
    <div
      data-container="body"
      data-placement="right"
      data-toggle="tooltip"
      title="Slack">
      <a target="_blank" href="https://holberton-school-org.slack.com">
        <div class="image slack">
          <div class="inner"></div>
        </div>
        <div class="visible-xs">Slack</div>
</a>    </div>

    <div
      data-container="body"
      data-placement="right"
      data-toggle="modal"
      data-target="#search-modal"
      title="Search">
      <a href="#">
          <div class="icon" data-toggle="tooltip" data-placement="right" data-container="body" title="Search">
            <i aria-hidden="true" class="fa fa-search "></i>
          </div>
        <div class="visible-xs">Search</div>
</a>    </div>

  <div
    data-container="body"
    data-placement="right"
    data-toggle="tooltip"
    title="My Profile">
    <a href="/users/my_profile">
        <div class="image ">
          <div class="inner" style="background-image: url('https://s3.eu-west-3.amazonaws.com/hbtn.intranet/users/photos/000/009/546/thumb/Capture_d%E2%80%99%C3%A9cran_2024-06-03_111954.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20241009%2Feu-west-3%2Fs3%2Faws4_request&amp;X-Amz-Date=20241009T194044Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=400443f89b37b3fe923afb83e9afd9c93f8526920d71f189c65850c03471308b')"></div>
        </div>

      <div class="visible-xs">My Profile</div>
</a>  </div>
</li>


  </ul>
</div>

    <main>
      <div id="layout-bars">
        <div class="px-5 py-3" id="student-switch-curriculum">
  <div class="dropdown d-flex flex-column gap-1">
    <span class="fs-small text-muted">Curriculum</span>
    <div aria-haspopup="true" aria-expanded="false" class="align-items-center d-flex gap-3" data-toggle="dropdown" id="student-switch-curriculum-dropdown" role="button">
      <div class="d-flex flex-column" style="line-height: 16px">
        <span class="fs-4 fw-600">
            [C#24]
          HBnB v2
        </span>
        <span class="fs-small text-muted">
          Average: <span class="fw-500">90.0%</span>
        </span>
      </div>
      <div class="d-flex flex-column justify-content-center">
        <span style="margin-bottom: -4px">
          <i aria-hidden="true" class="fa fa-angle-up  fa-fw"></i>
        </span>
        <span style="margin-top: -4px">
          <i aria-hidden="true" class="fa fa-angle-down  fa-fw"></i>
        </span>
      </div>
    </div>
    <ul aria-labelledby="student-switch-curriculum-dropdown" class="dropdown-menu fs-5">
        <li>
          <a class="" href="/curriculums/327/observe/37959">
            <div class="align-items-center d-flex py-2">
              <div class="d-flex flex-column" style="line-height: 16px">
                <span class="fs-4 fw-500">
                    [C#24]
                  Foundations v2 - Part 1
                </span>
                <span class="text-muted">
                  Average: <span class="fw-500">97.39%
                          </span>
                </span>
              </div>
            </div>
</a>        </li>
        <li>
          <a class="" href="/curriculums/392/observe/45551">
            <div class="align-items-center d-flex py-2">
              <div class="d-flex flex-column" style="line-height: 16px">
                <span class="fs-4 fw-500">
                    [C#24]
                  HBnB v2
                </span>
                <span class="text-muted">
                  Average: <span class="fw-500">90.0%
                          </span>
                </span>
              </div>
                <span class="fw-600 text-info" style="margin-left: 42px">
                  <i aria-hidden="true" class="fa fa-check "></i>
                </span>
            </div>
</a>        </li>
        <li>
          <a class="" href="/curriculums/394/observe/45832">
            <div class="align-items-center d-flex py-2">
              <div class="d-flex flex-column" style="line-height: 16px">
                <span class="fs-4 fw-500">
                    [C#24]
                  Foundations v2 - Part 2
                </span>
                <span class="text-muted">
                  Average: <span class="fw-500">95.36%
                          </span>
                </span>
              </div>
            </div>
</a>        </li>
    </ul>
  </div>
</div>




      </div>
      <article class="">

<div class="project row container-max">

    <div class="sm-gap">
    <div data-react-class="projects/ProjectHeader" data-react-props="{&quot;metadata&quot;:{&quot;level&quot;:&quot;Novice&quot;,&quot;author&quot;:&quot;Javier Valenzani&quot;,&quot;weight&quot;:1,&quot;migrated_to_sasheck&quot;:true,&quot;task_level_review_type&quot;:&quot;Your score will be updated as you progress.&quot;,&quot;correction&quot;:{&quot;released&quot;:true,&quot;requires_manual_correction&quot;:true},&quot;team&quot;:{&quot;in_team_of&quot;:3,&quot;members&quot;:[&quot;Henri Mille&quot;,&quot;Louis Beaumois&quot;,&quot;Stéphane Dinahet&quot;]}},&quot;project&quot;:{&quot;completion&quot;:0.0,&quot;id&quot;:3211,&quot;index&quot;:0,&quot;isAccessible&quot;:true,&quot;isOptional&quot;:false,&quot;imagePath&quot;:&quot;/assets/pathway/001_color-bb105595db22648e67fe1bf13ccc170165764f9c481034cdfd49dbb416af34af.png&quot;,&quot;name&quot;:&quot;HBnB - BL and API&quot;,&quot;score&quot;:{&quot;mandatory&quot;:null,&quot;optional&quot;:null},&quot;tasksCount&quot;:0},&quot;slackLink&quot;:null,&quot;tags&quot;:[],&quot;videoRoomLink&quot;:null}" data-react-cache-id="projects/ProjectHeader-0"></div>
  </div>


  <div id="project_id" class="d-none" data-project-id="3211"></div>



    <div>
      <ul class="nav nav-pills nav-justified" role="tablist">
          <li class="active"><a href="#description" role="tab" data-toggle="tab">Description</a></li>
          <li class=""><a href="#concepts" role="tab" data-toggle="tab">Concepts</a></li>
      </ul>
      <div class="tab-content mt-4">
        <div role="tabpanel" class="tab-pane active" id="description">
          <div class="panel panel-default position-relative" id="project-description">
  <a id="btn-scroll-to-tasks" href="#" class="btn btn-primary fixed-button hidden-xs">
    Go to tasks <i class="ml-1 fa fa-arrow-down"></i>
  </a>
  <div class="panel-body text-justify">
    <h3>Part 2: Implementation of Business Logic and API Endpoints</h3>

<p>In this part of the HBnB Project, you will begin the implementation phase of the application based on the design developed in the previous part. The focus of this phase is to build the Presentation and Business Logic layers of the application using Python and Flask. You will implement the core functionality by defining the necessary classes, methods, and endpoints that will serve as the foundation for the application’s operation.</p>

<p>In this part, you will create the structure of the project, develop the classes that define the business logic, and implement the API endpoints. The goal is to bring the documented architecture to life by setting up the key functionalities, such as creating and managing users, places, reviews, and amenities, while adhering to best practices in API design.</p>

<p>It’s important to note that, at this stage, you will focus only on implementing the core functionality of the API. JWT authentication and role-based access control will be addressed in the next part. The services layer will be built using Flask and the <code>flask-restx</code> extension to create RESTful APIs.</p>

<h4>Objectives</h4>

<p>By the end of this project, you should be able to:</p>

<ol>
<li><p><strong>Set Up the Project Structure:</strong></p>

<ul>
<li>Organize the project into a modular architecture, following best practices for Python and Flask applications.</li>
<li>Create the necessary packages for the Presentation and Business Logic layers.</li>
</ul></li>
<li><p><strong>Implement the Business Logic Layer:</strong></p>

<ul>
<li>Develop the core classes for the business logic, including User, Place, Review, and Amenity entities.</li>
<li>Implement relationships between entities and define how they interact within the application.</li>
<li>Implement the facade pattern to simplify communication between the Presentation and Business Logic layers.</li>
</ul></li>
<li><p><strong>Build RESTful API Endpoints:</strong></p>

<ul>
<li>Implement the necessary API endpoints to handle CRUD operations for Users, Places, Reviews, and Amenities.</li>
<li>Use <code>flask-restx</code> to define and document the API, ensuring a clear and consistent structure.</li>
<li>Implement data serialization to return extended attributes for related objects. For example, when retrieving a Place, the API should include details such as the owner’s <code>first_name</code>, <code>last_name</code>, and relevant amenities.</li>
</ul></li>
<li><p><strong>Test and Validate the API:</strong></p>

<ul>
<li>Ensure that each endpoint works correctly and handles edge cases appropriately.</li>
<li>Use tools like Postman or cURL to test your API endpoints.</li>
</ul></li>
</ol>

<h4>Project Vision and Scope</h4>

<p>The implementation in this part is focused on creating a functional and scalable foundation for the application. You will be working on:</p>

<ul>
<li><p><strong>Presentation Layer:</strong> Defining the services and API endpoints using Flask and <code>flask-restx</code>. You’ll structure the endpoints logically, ensuring clear paths and parameters for each operation.</p></li>
<li><p><strong>Business Logic Layer:</strong> Building the core models and logic that drive the application’s functionality. This includes defining relationships, handling data validation, and managing interactions between different components.</p></li>
</ul>

<p>At this stage, you won’t need to worry about user authentication or access control. However, you should ensure that the code is modular and organized, making it easy to integrate these features in Part 3.</p>

<h4>Learning Objectives</h4>

<p>This part of the project is designed to help you achieve the following learning outcomes:</p>

<ol>
<li><strong>Modular Design and Architecture:</strong> Learn how to structure a Python application using best practices for modularity and separation of concerns.</li>
<li><strong>API Development with Flask and flask-restx:</strong> Gain hands-on experience in building RESTful APIs using Flask, focusing on creating well-documented and scalable endpoints.</li>
<li><strong>Business Logic Implementation:</strong> Understand how to translate documented designs into working code, implementing core business logic in a structured and maintainable manner.</li>
<li><strong>Data Serialization and Composition Handling:</strong> Practice returning extended attributes in API responses, handling nested and related data in a clear and efficient way.</li>
<li><strong>Testing and Debugging:</strong> Develop skills in testing and validating APIs, ensuring that your endpoints handle requests correctly and return appropriate responses.</li>
</ol>

<h4>Recommended Resources</h4>

<ol>
<li><p><strong>Flask and flask-restx Documentation:</strong></p>

<ul>
<li><a href="/rltoken/qG7iHbDtVAtXiNd6UPa5_w" title="Flask Official Documentation" target="_blank">Flask Official Documentation</a></li>
<li><a href="/rltoken/T3KzG_F4pi8xOxm_hv4m3A" title="flask-restx Documentation" target="_blank">flask-restx Documentation</a></li>
</ul></li>
<li><p><strong>RESTful API Design Best Practices:</strong></p>

<ul>
<li><a href="/rltoken/tsEeFwnOYBD523DKDBlF-A" title="Best Practices for Designing a Pragmatic RESTful API" target="_blank">Best Practices for Designing a Pragmatic RESTful API</a></li>
<li><a href="/rltoken/qSLFMktKT5s6HUNZuitwnw" title="REST API Tutorial" target="_blank">REST API Tutorial</a></li>
</ul></li>
<li><p><strong>Python Project Structure and Modular Design:</strong></p>

<ul>
<li><a href="/rltoken/yxYx77NPezEH_Rt9FGfuuQ" title="Structuring Your Python Project" target="_blank">Structuring Your Python Project</a></li>
<li><a href="/rltoken/st27KOWY_W8fOCuML6Yyqw" title="Modular Programming with Python" target="_blank">Modular Programming with Python</a></li>
</ul></li>
<li><p><strong>Facade Design Pattern:</strong></p>

<ul>
<li><a href="/rltoken/AMfTkS5vRskcnzTPI6grUQ" title="Facade Pattern in Python" target="_blank">Facade Pattern in Python</a></li>
</ul></li>
</ol>

<p>This introduction sets the stage for the implementation phase of the project, where you will focus on bringing the documented design to life through well-structured code. The tasks ahead will challenge you to apply object-oriented principles, build scalable APIs, and think critically about how different components of the application interact.</p>

  </div>
</div>
        </div>
        <div role="tabpanel" class="tab-pane " id="concepts">
            <div class="panel panel-default">
    <div class="panel-body">
      <p>
        <em>For this project, we expect you to look at these concepts:</em>
      </p>

      <ul>
          <li>
            <a href="/concepts/1238">Understanding In-Memory Persistence in HBnB</a>
          </li>
          <li>
            <a href="/concepts/1239">Understanding the Facade Pattern in the HBnB Project</a>
          </li>
      </ul>
    </div>
  </div>

        </div>
      </div>
    </div>

        <h2 id="task-container" class="gap">Tasks</h2>

  <div class="col-sm-12 col-md-12 col-lg-8 xol-xl-9">
      <div data-role="task31650" data-position="1" id="task-num-0">
        <div class="panel panel-default task-card " id="task-31650">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Project Setup and Package Initialization
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

<p>Set up the initial project structure for the HBnB application, ensuring the codebase is organized according to best practices for a modular Python application. The focus is on creating the necessary folders, packages, and files for the Presentation, Business Logic, and Persistence layers while preparing the code to integrate the Facade pattern. Although the Persistence layer will be fully implemented in Part 3 using SQL Alchemy, this task includes setting up the structure and providing the complete implementation of an in-memory repository to handle object storage and validation.</p>

<h4>Context</h4>

<p>Before diving into the implementation of the business logic and API endpoints, it’s essential to have a well-organized project structure. A clear and modular organization will help maintain the codebase, make it easier to integrate new features, and ensure that your application is scalable. Additionally, to simplify the implementation, you are provided with the complete in-memory repository code. This repository will later be replaced by a database-backed solution in Part 3.</p>

<p>In this task, you will:</p>

<ol>
<li>Set up the structure for the Presentation, Business Logic, and Persistence layers.</li>
<li>Prepare the project to use the Facade pattern for communication between layers.</li>
<li>Implement the in-memory repository to handle object storage and validation.</li>
<li>Plan for future integration of the Persistence layer, even though it won’t be fully implemented in this part.</li>
</ol>

<h4>Instructions</h4>

<p>-&gt; <a href="/rltoken/-s8prpwrPoVoY-wZCq2Raw" title="Find the detailed instructions for this task here" target="_blank">Find the detailed instructions for this task here</a> &lt;-</p>

<h4>Expected Outcome</h4>

<p>By the end of this task, you should have a well-organized project structure that accommodates the Presentation, Business Logic, and Persistence layers. The codebase should be modular and easy to maintain, with a clear separation of concerns. You’ll also have a functional Flask application that is ready to integrate API endpoints, business logic, and persistence in the upcoming tasks.</p>

<p>The in-memory repository and Facade pattern are now set up to streamline communication between layers. While the persistence layer is only using in-memory storage at this stage, it is designed to be easily replaced with a database-backed solution in Part 3.</p>

<h4>Resources</h4>

<ol>
<li><strong>Flask Documentation:</strong> <a href="/rltoken/qG7iHbDtVAtXiNd6UPa5_w" title="https://flask.palletsprojects.com/en/3.0.x/" target="_blank">https://flask.palletsprojects.com/en/3.0.x/</a></li>
<li><strong>Flask-RESTx Documentation:</strong> <a href="/rltoken/T3KzG_F4pi8xOxm_hv4m3A" title="https://flask-restx.readthedocs.io/en/latest/" target="_blank">https://flask-restx.readthedocs.io/en/latest/</a></li>
<li><strong>Python Project Structure Best Practices:</strong> <a href="/rltoken/yxYx77NPezEH_Rt9FGfuuQ" title="https://docs.python-guide.org/writing/structure/" target="_blank">https://docs.python-guide.org/writing/structure/</a></li>
<li><strong>Facade Design Pattern in Python:</strong> <a href="/rltoken/AMfTkS5vRskcnzTPI6grUQ" title="https://refactoring.guru/design-patterns/facade/python/example" target="_blank">https://refactoring.guru/design-patterns/facade/python/example</a></li>
</ol>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-hbnb</code></li>
            <li>Directory: <code>part2</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="31650" data-batch-id="843" data-toggle="modal" data-target="#task-31650-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-31650-users-done-modal" data-task-id="31650" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "0. Project Setup and Package Initialization"</h4>
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
              <span id="task-31650-score-info-score">0</span>/0
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

      </div>
      <div data-role="task31651" data-position="2" id="task-num-1">
        <div class="panel panel-default task-card " id="task-31651">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Implement Core Business Logic Classes
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

<p>Implement the core business logic classes that define the entities of the HBnB application, including the necessary attributes, methods, and relationships. This task focuses on creating the fundamental models (User, Place, Review, and Amenity) while considering the design choices made by students in Part 1. </p>

<h4>Context</h4>

<p>In Part 1, students designed the Business Logic layer, including defining entities and relationships. This task requires you to implement those designs while adhering to best practices for modular, maintainable code. You may have already created base classes with common attributes (e.g., <code>id</code>, <code>created_at</code>, and <code>updated_at</code>) to be inherited by concrete classes such as <code>User</code>, <code>Place</code>, <code>Review</code>, and <code>Amenity</code>.</p>

<p>In this task, you will:</p>

<ol>
<li>Implement the classes based on your Part 1 design.</li>
<li>Ensure relationships between entities are correctly implemented.</li>
<li>Handle attribute validation and updates according to the requirements.</li>
</ol>

<h4>Instructions</h4>

<p>-&gt; <a href="/rltoken/yS07eCcaxErW51_HjfYaUA" title="Find the detailed instructions for this task here" target="_blank">Find the detailed instructions for this task here</a> &lt;-</p>

<h4>Resources</h4>

<ol>
<li><strong>Python OOP Basics:</strong> <a href="/rltoken/gB7cc0nmujk0WB-CuRW6Vw" title="https://realpython.com/python3-object-oriented-programming/" target="_blank">https://realpython.com/python3-object-oriented-programming/</a></li>
<li><strong>Designing Classes and Relationships:</strong> <a href="/rltoken/UIITxjVKGbuphwCHWc8U2A" title="https://docs.python.org/3/tutorial/classes.html" target="_blank">https://docs.python.org/3/tutorial/classes.html</a></li>
<li><strong>Why You Should Use UUIDs:</strong> <a href="/rltoken/ZIUK7VUakGtGbt8er7kOeg" title="https://datatracker.ietf.org/doc/html/rfc4122" target="_blank">https://datatracker.ietf.org/doc/html/rfc4122</a></li>
</ol>

<h4>Expected Outcome</h4>

<p>By the end of this task, you should have fully implemented core business logic classes (User, Place, Review, Amenity) with the appropriate attributes, methods, and relationships. With these components in place, you will be ready to proceed to implementing the API endpoints in the next task. The implemented classes should support the necessary validation, relationships, and data integrity checks required for the application’s core functionality. Additionally, the relationships between entities should be fully operational, allowing seamless interactions like linking reviews to places or associating amenities with places.</p>

<p>With this solid foundation in place, the business logic will be prepared for further integration with the Presentation and Persistence layers in subsequent tasks.</p>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-hbnb</code></li>
            <li>Directory: <code>part2</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="31651" data-batch-id="843" data-toggle="modal" data-target="#task-31651-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-31651-users-done-modal" data-task-id="31651" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "1. Implement Core Business Logic Classes"</h4>
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
              <span id="task-31651-score-info-score">0</span>/
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

      </div>
      <div data-role="task31652" data-position="3" id="task-num-2">
        <div class="panel panel-default task-card " id="task-31652">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Implement the User Endpoints
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

<p>Implement the API endpoints needed for managing users in the HBnB application. This task involves setting up CRUD operations (Create, Read, Update) for users, ensuring that these endpoints are integrated with the Business Logic layer. The <code>DELETE</code> operation will <strong>not</strong> be implemented for users in this part of the project. Additionally, when retrieving user data, the password should <strong>not</strong> be included in the response. The API interface, return format, and status codes must be clearly defined since black-box testing will be performed later.</p>

<p>In this task, the full implementation for user creation (POST) and retrieval (GET) by ID is provided as a guide. You will be responsible for implementing the retrieval of the list of users (GET /api/v1/users/) and updating user information (PUT /api/v1/users/<user_id>). The approach for the remaining endpoints follows similar principles and should be implemented analogously. The same applies to the other entities (e.g., Place, Review, Amenity).</p>

<p>In this task, you will:</p>

<ol>
<li>Set up the <code>POST</code>, <code>GET</code>, and <code>PUT</code> endpoints for managing users.</li>
<li>Implement the logic for handling user-related operations in the Business Logic layer.</li>
<li>Integrate the Presentation layer (API) and Business Logic layer, utilizing the repository pattern.</li>
</ol>

<h4>Instructions</h4>

<p>-&gt; <a href="/rltoken/m2eQ4O4iOGAkEI-ps_r32A" title="Find the detailed instructions for this task here" target="_blank">Find the detailed instructions for this task here</a> &lt;-</p>

<h4>Resources</h4>

<ol>
<li><strong>Flask-RESTx Documentation:</strong> <a href="/rltoken/T3KzG_F4pi8xOxm_hv4m3A" title="https://flask-restx.readthedocs.io/en/latest/" target="_blank">https://flask-restx.readthedocs.io/en/latest/</a></li>
<li><strong>Testing REST APIs with cURL:</strong> <a href="/rltoken/tA6ap3q1tdnDL67caQc-qg" title="https://everything.curl.dev/" target="_blank">https://everything.curl.dev/</a></li>
<li><strong>Designing RESTful APIs:</strong> <a href="/rltoken/qSLFMktKT5s6HUNZuitwnw" title="https://restfulapi.net/" target="_blank">https://restfulapi.net/</a></li>
</ol>

<h4>Expected Outcome</h4>

<p>By the end of this task, you should have fully implemented the core user management endpoints, including the ability to create, read, and update users. The <code>DELETE</code> operation will not be implemented for users in this part. The provided implementation guide for the user registration endpoint should serve as a model for implementing the remaining user endpoints as well as endpoints for other entities (e.g., Place, Review, Amenity). The functionality should be documented and tested, ensuring that all user-related operations are handled smoothly within the HBnB application.</p>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-hbnb</code></li>
            <li>Directory: <code>part2</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="31652" data-batch-id="843" data-toggle="modal" data-target="#task-31652-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-31652-users-done-modal" data-task-id="31652" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "2. Implement the User Endpoints"</h4>
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
              <span id="task-31652-score-info-score">0</span>/
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

      </div>
      <div data-role="task31653" data-position="4" id="task-num-3">
        <div class="panel panel-default task-card " id="task-31653">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Implement the Amenity Endpoints
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

<p>Implement the API endpoints required for managing amenities in the HBnB application. This task involves setting up the endpoints to handle CRUD operations (Create, Read, Update) for amenities, while ensuring integration with the Business Logic layer via the Facade pattern. The <code>DELETE</code> operation will not be implemented for amenities in this part of the project.</p>

<p>In this task, you will:</p>

<ol>
<li>Set up the <code>POST</code>, <code>GET</code>, and <code>PUT</code> endpoints for managing amenities.</li>
<li>Implement the necessary logic for handling amenity-related operations in the Business Logic layer.</li>
<li>Integrate the Presentation layer (API) and Business Logic layer through the Facade.</li>
</ol>

<h4>Instructions</h4>

<p>-&gt; <a href="/rltoken/dgSGjXTNLi2JYeQv1lhFwQ" title="Find the detailed instructions for this task here" target="_blank">Find the detailed instructions for this task here</a> &lt;-</p>

<h4>Resources</h4>

<ol>
<li><strong>Flask-RESTx Documentation:</strong> <a href="/rltoken/T3KzG_F4pi8xOxm_hv4m3A" title="https://flask-restx.readthedocs.io/en/latest/" target="_blank">https://flask-restx.readthedocs.io/en/latest/</a></li>
<li><strong>Testing REST APIs with cURL:</strong> <a href="/rltoken/tA6ap3q1tdnDL67caQc-qg" title="https://everything.curl.dev/" target="_blank">https://everything.curl.dev/</a></li>
<li><strong>Designing RESTful APIs:</strong> <a href="/rltoken/qSLFMktKT5s6HUNZuitwnw" title="https://restfulapi.net/" target="_blank">https://restfulapi.net/</a></li>
</ol>

<h4>Expected Outcome</h4>

<p>By the end of this task, you should have fully implemented the core amenity management endpoints, including the ability to create, read, and update amenities. The <code>DELETE</code> operation will not be implemented for amenities in this part. The provided placeholders should guide you in implementing the logic based on the example provided for user registration. The functionality should be documented and tested, ensuring that all amenity-related operations are handled smoothly within the HBnB application.</p>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-hbnb</code></li>
            <li>Directory: <code>part2</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="31653" data-batch-id="843" data-toggle="modal" data-target="#task-31653-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-31653-users-done-modal" data-task-id="31653" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "3. Implement the Amenity Endpoints"</h4>
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
              <span id="task-31653-score-info-score">0</span>/
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

      </div>
      <div data-role="task31654" data-position="5" id="task-num-4">
        <div class="panel panel-default task-card " id="task-31654">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Implement the Place Endpoints
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

<p>Implement the API endpoints needed for managing places in the HBnB application. This task involves setting up CRUD operations (Create, Read, Update) for places, ensuring that these endpoints are integrated with the Business Logic layer through the Facade pattern. The <code>DELETE</code> operation will <strong>not</strong> be implemented for places in this part of the project.</p>

<p>Given that the <code>Place</code> entity has relationships with other entities, such as <code>User</code> (owner) and <code>Amenity</code>, you’ll need to handle these relationships carefully while maintaining the integrity of the application logic. The <code>Review</code> entity will be implemented in the next task, so it should not be included in this task.</p>

<p>In this task, you will:</p>

<ol>
<li>Set up the <code>POST</code>, <code>GET</code>, and <code>PUT</code> endpoints for managing places.</li>
<li>Implement the logic for handling place-related operations in the Business Logic layer.</li>
<li>Integrate the Presentation layer (API) and Business Logic layer through the Facade.</li>
<li>Implement validation for specific attributes like <code>price</code>, <code>latitude</code>, and <code>longitude</code>.</li>
<li>Ensure that related data such as <code>owner</code> details and <code>amenities</code> are properly handled and returned with the Place data.</li>
</ol>

<h4>Instructions</h4>

<p>-&gt; <a href="/rltoken/1sF0lHD3AL9_wRX26O0YlA" title="Find the detailed instructions for this task here" target="_blank">Find the detailed instructions for this task here</a> &lt;-</p>

<h3>Resources</h3>

<ol>
<li><strong>Flask-RESTx Documentation:</strong> <a href="/rltoken/T3KzG_F4pi8xOxm_hv4m3A" title="https://flask-restx.readthedocs.io/en/latest/" target="_blank">https://flask-restx.readthedocs.io/en/latest/</a></li>
<li><strong>Testing REST APIs with cURL:</strong> <a href="/rltoken/tA6ap3q1tdnDL67caQc-qg" title="https://everything.curl.dev/" target="_blank">https://everything.curl.dev/</a></li>
<li><strong>Designing RESTful APIs:</strong> <a href="/rltoken/qSLFMktKT5s6HUNZuitwnw" title="https://restfulapi.net/" target="_blank">https://restfulapi.net/</a></li>
</ol>

<h3>Expected Outcome</h3>

<p>By the end of this task, you should have implemented the core place management endpoints, including the ability to create, read, and update places. The <code>DELETE</code> operation will not be implemented for places in this part. You will have handled the relationships between places, owners, and amenities, including validating specific attributes like price, latitude, and longitude. The functionality should be documented and tested, ensuring smooth operation within the HBnB application.</p>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-hbnb</code></li>
            <li>Directory: <code>part2</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="31654" data-batch-id="843" data-toggle="modal" data-target="#task-31654-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-31654-users-done-modal" data-task-id="31654" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "4. Implement the Place Endpoints"</h4>
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
              <span id="task-31654-score-info-score">0</span>/
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

      </div>
      <div data-role="task31655" data-position="6" id="task-num-5">
        <div class="panel panel-default task-card " id="task-31655">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      5. Implement the Review Endpoints
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

<p>Implement the API endpoints needed for managing reviews in the HBnB application. This task involves setting up CRUD operations (Create, Read, Update, Delete) for reviews, ensuring that these endpoints are integrated with the Business Logic layer through the Facade pattern. The <code>DELETE</code> operation <strong>will</strong> be implemented for reviews, making it the only entity for which deletion is supported in this part of the project.</p>

<p>In this task, you will:</p>

<ol>
<li>Set up the <code>POST</code>, <code>GET</code>, <code>PUT</code>, and <code>DELETE</code> endpoints for managing reviews.</li>
<li>Implement the logic for handling review-related operations in the Business Logic layer.</li>
<li>Integrate the Presentation layer (API) and Business Logic layer through the Facade.</li>
<li>Implement validation for specific attributes like the text of the review and ensure that the review is associated with both a user and a place.</li>
<li>Update the Place model in <code>api/v1/places.py</code> to include the collection of reviews for a place.</li>
</ol>

<h4>Instructions</h4>

<p>-&gt; <a href="/rltoken/sSsMY_14UyHfZ2CCI5Dwww" title="Find the detailed instructions for this task here" target="_blank">Find the detailed instructions for this task here</a> &lt;-</p>

<h4>Resources</h4>

<ol>
<li><strong>Flask-RESTx Documentation:</strong> <a href="/rltoken/T3KzG_F4pi8xOxm_hv4m3A" title="https://flask-restx.readthedocs.io/en/latest/" target="_blank">https://flask-restx.readthedocs.io/en/latest/</a></li>
<li><strong>Testing REST APIs with cURL:</strong> <a href="/rltoken/tA6ap3q1tdnDL67caQc-qg" title="https://everything.curl.dev/" target="_blank">https://everything.curl.dev/</a></li>
<li><strong>Designing RESTful APIs:</strong> <a href="/rltoken/qSLFMktKT5s6HUNZuitwnw" title="https://restfulapi.net/" target="_blank">https://restfulapi.net/</a></li>
</ol>

<h4>Expected Outcome</h4>

<p>By the end of this task, you should have implemented the core review management endpoints, including the ability to create, read, update, and delete reviews. Additionally, you will have implemented the ability to retrieve all reviews associated with a specific place. The <code>DELETE</code> operation is introduced here to allow students to practice implementing this functionality for the first time. The functionality should be documented and tested, ensuring that all review-related operations are handled smoothly within the HBnB application.</p>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-hbnb</code></li>
            <li>Directory: <code>part2</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="31655" data-batch-id="843" data-toggle="modal" data-target="#task-31655-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-31655-users-done-modal" data-task-id="31655" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "5. Implement the Review Endpoints"</h4>
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
              <span id="task-31655-score-info-score">0</span>/
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

      </div>
      <div data-role="task31656" data-position="7" id="task-num-6">
        <div class="panel panel-default task-card " id="task-31656">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      6. Implement Testing and Validation of the Endpoints
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

<p>This task involves creating and running tests for the endpoints you have developed so far. You will implement validation logic, perform thorough testing using <code>cURL</code>, and document the results of those tests. The focus is on ensuring that each endpoint works as expected and adheres to the input/output formats, status codes, and validation rules you have defined in previous tasks.</p>

<p>In this task, you will:</p>

<ol>
<li>Implement basic validation checks for each of the attributes in your endpoints.</li>
<li>Perform black-box testing using <code>cURL</code> and the Swagger documentation generated by Flask-RESTx.</li>
<li>Create a detailed testing report, highlighting both successful and failed cases.</li>
</ol>

<h4>Instructions</h4>

<p>-&gt; <a href="/rltoken/7Ct5bf7Xxf6hsLBysyF53w" title="Find the detailed instructions for this task here" target="_blank">Find the detailed instructions for this task here</a> &lt;-</p>

<h4>Expected Outcome</h4>

<p>By the end of this task, you should have:
- Implemented basic validation for all entity models.
- Performed thorough testing using cURL and other tools.
- Generated Swagger documentation to confirm that your API is correctly described.
- Created and executed unit tests using <code>unittest</code> or <code>pytest</code>.
- Documented the testing process, highlighting both successful cases and edge cases that were handled correctly.</p>

<hr>

<p>This task combines both manual and automated testing while guiding students to validate and thoroughly test their implementation. Let me know if any additional information is needed!</p>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-hbnb</code></li>
            <li>Directory: <code>part2</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="31656" data-batch-id="843" data-toggle="modal" data-target="#task-31656-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-31656-users-done-modal" data-task-id="31656" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "6. Implement Testing and Validation of the Endpoints"</h4>
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
              <span id="task-31656-score-info-score">0</span>/
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

      </div>


      <div class="panel panel-default">
        <div class="panel-body">
          <div class="d-flex justify-content-around">
              <div>
                <a data-toggle="tooltip" title="HBnB - UML" class="btn btn-primary" role="button" href="/projects/3210">
                  <span class="glyphicon glyphicon-arrow-left" aria-hidden="true"></span> Previous project
</a>              </div>
              <form action=/corrections/1021852/skip method="post">
                <input
                  name="authenticity_token"
                  type="hidden"
                  value=Ki0BiF-Rf9J-z0sIahoFAQGBDS_XXGbMqtUYOecPThDsoZzWGPHvrTrg64Zt8iplKnudDU8117o-YPzTCWjoTA
                />
                <button class="btn btn-warning" type="submit">
                  Next project <span class="glyphicon glyphicon-arrow-right" aria-hidden="true"></span>
                </button>
              </form>
          </div>
        </div>
      </div>
  </div>

    <div class="col-sm-12 col-md-12 hidden-lg">
        <div data-react-class="projects/ProjectReview" data-react-props="{&quot;style&quot;:&quot;line&quot;,&quot;correction&quot;:{&quot;statusURI&quot;:&quot;/corrections/1021852/status_self_paced.json&quot;,&quot;startReviewURI&quot;:&quot;/corrections/1021852/start_auto_review_self_paced.json&quot;},&quot;csrfToken&quot;:&quot;Hv-dz1Wxc75npLZXA7w7itupZvmLUSuIyuzWz4NMVuLYcwCREtHjwSOLFtkEVBTu8FP22xM4mv5eWTIlbSvwvg&quot;,&quot;nextProject&quot;:{&quot;details&quot;:{&quot;curriculum_completed&quot;:false,&quot;message&quot;:&quot;Next project: HBnB - Auth \u0026 DB&quot;,&quot;uri&quot;:&quot;/projects/3212&quot;},&quot;fetchURI&quot;:&quot;/projects/3211/next&quot;},&quot;pollingInterval&quot;:10000,&quot;progress&quot;:{&quot;auto_review&quot;:{&quot;can_execute&quot;:true,&quot;completion&quot;:null,&quot;inability_to_execute_reason&quot;:null},&quot;tasks&quot;:[{&quot;id&quot;:31650,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:0,&quot;score&quot;:0}},{&quot;id&quot;:31651,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:null,&quot;score&quot;:0}},{&quot;id&quot;:31652,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:null,&quot;score&quot;:0}},{&quot;id&quot;:31653,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:null,&quot;score&quot;:0}},{&quot;id&quot;:31654,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:null,&quot;score&quot;:0}},{&quot;id&quot;:31655,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:null,&quot;score&quot;:0}},{&quot;id&quot;:31656,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:null,&quot;score&quot;:0}}],&quot;summary&quot;:{&quot;completion&quot;:0.0,&quot;score&quot;:{&quot;mandatory&quot;:null,&quot;optional&quot;:null}},&quot;can_skip&quot;:true,&quot;can_start_peer_review&quot;:false},&quot;peerReview&quot;:{&quot;availableReviewersURI&quot;:&quot;/corrections/1021852/available_reviewers.json&quot;,&quot;canReviewPeerDirectly&quot;:true,&quot;correctCorrectionURI&quot;:&quot;https://intranet.hbtn.io/corrections/1021852/correct&quot;,&quot;qaReviewsURI&quot;:&quot;/corrections/to_review&quot;,&quot;readyForReviewURI&quot;:&quot;/corrections/1021852/toggle_ready_for_review.json&quot;,&quot;reviewDeadline&quot;:null,&quot;synchronousManualReview&quot;:false},&quot;project&quot;:{&quot;completion&quot;:0.0,&quot;id&quot;:3211,&quot;index&quot;:0,&quot;isAccessible&quot;:true,&quot;isOptional&quot;:false,&quot;imagePath&quot;:&quot;/assets/pathway/001_color-bb105595db22648e67fe1bf13ccc170165764f9c481034cdfd49dbb416af34af.png&quot;,&quot;name&quot;:&quot;HBnB - BL and API&quot;,&quot;score&quot;:{&quot;mandatory&quot;:null,&quot;optional&quot;:null},&quot;tasksCount&quot;:0},&quot;skipURI&quot;:&quot;/corrections/1021852/skip&quot;,&quot;taskLevelReviewTypeHumanized&quot;:&quot;Your score will be updated as you progress.&quot;}" data-react-cache-id="projects/ProjectReview-0"></div>

    </div>

  <div class="col-xl-3 col-lg-4 hidden-xs hidden-sm hidden-md sticky-nav">
          <div data-react-class="projects/ProjectReview" data-react-props="{&quot;style&quot;:&quot;column&quot;,&quot;correction&quot;:{&quot;statusURI&quot;:&quot;/corrections/1021852/status_self_paced.json&quot;,&quot;startReviewURI&quot;:&quot;/corrections/1021852/start_auto_review_self_paced.json&quot;},&quot;csrfToken&quot;:&quot;tmESBNV-Bp7Gh1QBbiNsacBPxDFJIF5anGSC8sN6V05w7Y9akh6W4YKo9I9py0MN67VUE9FJ7ywI0WYYLR3xEg&quot;,&quot;nextProject&quot;:{&quot;details&quot;:{&quot;curriculum_completed&quot;:false,&quot;message&quot;:&quot;Next project: HBnB - Auth \u0026 DB&quot;,&quot;uri&quot;:&quot;/projects/3212&quot;},&quot;fetchURI&quot;:&quot;/projects/3211/next&quot;},&quot;pollingInterval&quot;:10000,&quot;progress&quot;:{&quot;auto_review&quot;:{&quot;can_execute&quot;:true,&quot;completion&quot;:null,&quot;inability_to_execute_reason&quot;:null},&quot;tasks&quot;:[{&quot;id&quot;:31650,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:0,&quot;score&quot;:0}},{&quot;id&quot;:31651,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:null,&quot;score&quot;:0}},{&quot;id&quot;:31652,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:null,&quot;score&quot;:0}},{&quot;id&quot;:31653,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:null,&quot;score&quot;:0}},{&quot;id&quot;:31654,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:null,&quot;score&quot;:0}},{&quot;id&quot;:31655,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:null,&quot;score&quot;:0}},{&quot;id&quot;:31656,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:null,&quot;score&quot;:0}}],&quot;summary&quot;:{&quot;completion&quot;:0.0,&quot;score&quot;:{&quot;mandatory&quot;:null,&quot;optional&quot;:null}},&quot;can_skip&quot;:true,&quot;can_start_peer_review&quot;:false},&quot;peerReview&quot;:{&quot;availableReviewersURI&quot;:&quot;/corrections/1021852/available_reviewers.json&quot;,&quot;canReviewPeerDirectly&quot;:true,&quot;correctCorrectionURI&quot;:&quot;https://intranet.hbtn.io/corrections/1021852/correct&quot;,&quot;qaReviewsURI&quot;:&quot;/corrections/to_review&quot;,&quot;readyForReviewURI&quot;:&quot;/corrections/1021852/toggle_ready_for_review.json&quot;,&quot;reviewDeadline&quot;:null,&quot;synchronousManualReview&quot;:false},&quot;project&quot;:{&quot;completion&quot;:0.0,&quot;id&quot;:3211,&quot;index&quot;:0,&quot;isAccessible&quot;:true,&quot;isOptional&quot;:false,&quot;imagePath&quot;:&quot;/assets/pathway/001_color-bb105595db22648e67fe1bf13ccc170165764f9c481034cdfd49dbb416af34af.png&quot;,&quot;name&quot;:&quot;HBnB - BL and API&quot;,&quot;score&quot;:{&quot;mandatory&quot;:null,&quot;optional&quot;:null},&quot;tasksCount&quot;:0},&quot;skipURI&quot;:&quot;/corrections/1021852/skip&quot;,&quot;taskLevelReviewTypeHumanized&quot;:&quot;Your score will be updated as you progress.&quot;}" data-react-cache-id="projects/ProjectReview-0"></div>


    <div class="panel panel-default task-card " id="task-18584">
      <span id="user_id" data-id="2303"></span>
      <div class="panel-heading panel-heading-actions">
        <h3 class="panel-title">
          Tasks list
        </h3>
      </div>
      <div class="panel-body task-list">
          <ul class="nav nav-pills nav-justified" role="tablist">
              <li class="active"><a href="#mandatory" role="tab" data-toggle="tab">Mandatory</a></li>
              <li><a href="#advanced" role="tab" data-toggle="tab">Advanced</a></li>
          </ul>
          <div class="tab-content mt-4">
            <div role="tabpanel" class="tab-pane active" id="mandatory">
                  <div class="task-button d-flex align-center justify-content-between" role="button" data-task-index="0" id="heading-0">
                    <div class="task-title-list">0. <code>Project Setup and Package Initialization</code></div>
                    <strong class='task_progress_score text-primary ml-2' data-task-id='31650'></strong>
                  </div>
                  <div class="task-button d-flex align-center justify-content-between" role="button" data-task-index="1" id="heading-1">
                    <div class="task-title-list">1. <code>Implement Core Business Logic Classes</code></div>
                    <strong class='task_progress_score text-primary ml-2' data-task-id='31651'></strong>
                  </div>
                  <div class="task-button d-flex align-center justify-content-between" role="button" data-task-index="2" id="heading-2">
                    <div class="task-title-list">2. <code>Implement the User Endpoints</code></div>
                    <strong class='task_progress_score text-primary ml-2' data-task-id='31652'></strong>
                  </div>
                  <div class="task-button d-flex align-center justify-content-between" role="button" data-task-index="3" id="heading-3">
                    <div class="task-title-list">3. <code>Implement the Amenity Endpoints</code></div>
                    <strong class='task_progress_score text-primary ml-2' data-task-id='31653'></strong>
                  </div>
                  <div class="task-button d-flex align-center justify-content-between" role="button" data-task-index="4" id="heading-4">
                    <div class="task-title-list">4. <code>Implement the Place Endpoints</code></div>
                    <strong class='task_progress_score text-primary ml-2' data-task-id='31654'></strong>
                  </div>
                  <div class="task-button d-flex align-center justify-content-between" role="button" data-task-index="5" id="heading-5">
                    <div class="task-title-list">5. <code>Implement the Review Endpoints</code></div>
                    <strong class='task_progress_score text-primary ml-2' data-task-id='31655'></strong>
                  </div>
                  <div class="task-button d-flex align-center justify-content-between" role="button" data-task-index="6" id="heading-6">
                    <div class="task-title-list">6. <code>Implement Testing and Validation of the Endpoints</code></div>
                    <strong class='task_progress_score text-primary ml-2' data-task-id='31656'></strong>
                  </div>
            </div>
            <div role="tabpanel" class="tab-pane" id="advanced">
            </div>
          </div>
      </div>
    </div>
  </div>


<script src="/assets/javascripts/application/custom/project_tasks.js"></script>



        <div class="modal fade" id="sandboxes-modal"><div class="modal-dialog modal-lg"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button><h4 class="modal-title">Recommended Sandboxes</h4></div><div class="modal-body"><div data-react-class="user_sandboxes/Sandboxes" data-react-props="{&quot;images&quot;:[{&quot;id&quot;:50,&quot;name&quot;:&quot;Ubuntu 18.04&quot;,&quot;aws_region&quot;:&quot;US East (N. Virginia)\t&quot;},{&quot;id&quot;:16,&quot;name&quot;:&quot;Ubuntu 22.04&quot;,&quot;aws_region&quot;:&quot;US East (N. Virginia)\t&quot;},{&quot;id&quot;:51,&quot;name&quot;:&quot;Ubuntu 18.04&quot;,&quot;aws_region&quot;:&quot;South America (São Paulo)&quot;},{&quot;id&quot;:17,&quot;name&quot;:&quot;Ubuntu 22.04&quot;,&quot;aws_region&quot;:&quot;South America (São Paulo)&quot;},{&quot;id&quot;:52,&quot;name&quot;:&quot;Ubuntu 18.04&quot;,&quot;aws_region&quot;:&quot;Europe (Paris)&quot;},{&quot;id&quot;:14,&quot;name&quot;:&quot;Ubuntu 22.04&quot;,&quot;aws_region&quot;:&quot;Europe (Paris)&quot;},{&quot;id&quot;:53,&quot;name&quot;:&quot;Ubuntu 18.04&quot;,&quot;aws_region&quot;:&quot;Asia Pacific (Sydney)&quot;},{&quot;id&quot;:18,&quot;name&quot;:&quot;Ubuntu 22.04&quot;,&quot;aws_region&quot;:&quot;Asia Pacific (Sydney)&quot;}],&quot;sandboxesUri&quot;:&quot;/user_sandboxes&quot;,&quot;csrfToken&quot;:&quot;r5-dCdmtc-8V_72sUF-m8WZAVL1OFiQ256AR-ZbCafBpEwBXns3jkFHQHSJXt4mVTbrEn9Z_lUBzFfUTeKXPrA&quot;,&quot;maxNumberOfContainers&quot;:2}" data-react-cache-id="user_sandboxes/Sandboxes-0"></div></div></div></div></div>

    <button id="scrollToTopButton" class="floating-button btn-primary">
        <i class="fa fa-arrow-up"></i>
    </button>
</div>

<script src="/assets/javascripts/applications/custom/project.js"></script>
      </article>
    </main>
      <div class="modal fade" id="search-modal" tabindex="-1" role="dialog" aria-labelledby="search-modal-label">
    <div class="modal-dialog modal-md">
        <div class="modal-content">
            <div class="modal-header">
                <div id="search-bar-container">
    <input id="search-bar"
            type="text"
            name="hbtn-search-bar"
            placeholder="✨Start search by typing in this field✨">
</div>

            </div>
            <div class="modal-body">
                <div id="modal-spinner" class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div id="search-results-container">
</div>

            </div>
        </div>
    </div>
</div>

      <div class="modal fade" id="markdownGuideModal" tabindex="-1" role="dialog" aria-labelledby="markdownGuideModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-md">
    <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title">Markdown Guide</h4>
        </div>
        <div class="modal-body">
            <h4>Emphasis</h4>
<pre>**<strong>bold</strong>**
*<em>italics</em>*
~~<strike>strikethrough</strike>~~</pre>
<h4>Headers</h4>
<pre># Big header
## Medium header
### Small header
#### Tiny header</pre>
<h4>Lists</h4>
<pre>* Generic list item
* Generic list item
* Generic list item

1. Numbered list item
2. Numbered list item
3. Numbered list item</pre>
<h4>Links</h4>
<pre>[Text to display](http://www.example.com)</pre>
<h4>Quotes</h4>
<pre>> This is a quote.
> It can span multiple lines!</pre>
<h4>Images</h4>
<p>CSS style available: <code>width, height, opacity</code></p>
<pre>![](http://www.example.com/image.jpg)
![](http://www.example.com/image.jpg | width: 200px)
![](http://www.example.com/image.jpg | height: 124px | width: 80px | opacity: 0.6)
</pre>
<h4>Tables</h4>
<pre>| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John     | Doe      | Male     |
| Mary     | Smith    | Female   |

<em>Or without aligning the columns...</em>

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John | Doe | Male |
| Mary | Smith | Female |
</pre>
<h4>Displaying code</h4>
<pre>`var example = "hello!";`

<em>Or spanning multiple lines...</em>

```
var example = "hello!";
alert(example);
```</pre>
        </div>
    </div>
  </div>
</div>

      <script>
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

          ga('create',
            'UA-67152800-6',
            'auto', {
              userId: '9546'
            }
          );

        ga('send', 'pageview');

        $(document).ready(function() {
          ga(function(tracker) {
            var clientId = tracker.get('clientId');
            $('.ga-client-id').val(clientId);
          });
        });
      </script>

</body>
</html>
