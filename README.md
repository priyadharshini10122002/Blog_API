# Key Features
  - **JWT Authentication:** Secure user registration and login with token-based authentication, allowing for protected access to endpoints.
  - **User Management:** Enables new users to sign up and existing users to authenticate, receiving JWT tokens for further interactions.
  - **Token-Based Access Control:** Protects routes and resources, ensuring that only authenticated users can access certain API endpoints.
  -  **Blog Management**: Full CRUD functionalities to create, read, update, and delete blog posts.

# API Endpoints
  -  POST /api/register/ - Register a new user and get a JWT token.
  -  POST /api/login/ - Authenticate a user and receive a JWT token.
  -  POST /api/blog/ - Create Blog Post
  -  GET /api/blog/ - Retrieve Blog Posts
  -  PATCH /api/blog/<id>/ - Update Blog Post
  -  DELETE /api/blog/<id>/ - Delete Blog Post


# Technology Stack
  -  **Backend:** Python, Django, Django REST Framework
  -  **Authentication:** JWT Authentication via Django REST Framework

## API Endpoints

You can find the Postman collection for the API [here]
(https://api.postman.com/collections/35061861-ff481b36-513d-4855-a9a9-be9be7b81d02?access_key=PMAT-01JAAF3PR91CJ8Q76JCJ4JD68V).
