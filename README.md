# Django API Authentication Project

This project demonstrates how to set up a Django project with API authentication using Django REST framework.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- virtualenv (optional but recommended)

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/ankurjaiswalofficial/django-api-auth.git
    cd django-api-auth
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (optional but recommended for accessing the admin site):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the application:**

    - Admin site: `http://127.0.0.1:8000/admin/`
    - API endpoints: `http://127.0.0.1:8000/api/`
    - API authentication: `http://127.0.0.1:8000/api-auth/`

8. **Create an API key:**

    To create an API key, send a POST request to the `http://127.0.0.1:8000/api-key/` endpoint. Include any required data in the request body as specified by the API documentation.

9. **Access endpoints using the API key:**

    Include the following header in your HTTP requests to access protected endpoints:

    ```
    X-API-KEY: <your-api-key>
    ```

## Frontend Integration

This project includes a frontend application that interacts with the Django API. The frontend is built using modern JavaScript frameworks and communicates with the backend via RESTful API endpoints.

### Setting Up the Frontend

1. **Navigate to the frontend directory:**

    ```bash
    cd frontend
    ```

2. **Install dependencies:**

    ```bash
    npm install
    ```

3. **Run the development server:**

    ```bash
    npm start
    ```

4. **Access the frontend application:**

    Open your browser and navigate to `http://localhost:3000`.

### Frontend Features

- User authentication using API keys and Hawk authentication.
- Interactive UI for testing API endpoints.
- Error handling and user-friendly messages for failed requests.

## CORS Configuration

To enable cross-origin requests between the frontend and backend, CORS (Cross-Origin Resource Sharing) has been configured in the Django project.

### CORS Setup

1. **Install the `django-cors-headers` package:**

    ```bash
    pip install django-cors-headers
    ```

2. **Add `corsheaders` to `INSTALLED_APPS` in `settings.py`:**

    ```python
    INSTALLED_APPS = [
        ...existing code...
        'corsheaders',
    ]
    ```

3. **Add the `CorsMiddleware` to the middleware stack in `settings.py`:**

    ```python
    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        ...existing code...
    ]
    ```

4. **Configure allowed origins in `settings.py`:**

    ```python
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:3000",  # Frontend URL
    ]
    ```

This setup ensures that the frontend can communicate with the backend without encountering CORS errors.

## Custom Middleware

A custom middleware has been implemented to log API requests and responses for debugging and monitoring purposes.

### Middleware Implementation

1. **Create the middleware file:**

    The middleware is located in `myapp/middleware.py`.

2. **Add the middleware to the stack in `settings.py`:**

    ```python
    MIDDLEWARE = [
        ...existing code...
        'myapp.middleware.RequestResponseLoggingMiddleware',
    ]
    ```

3. **Middleware Functionality:**

    - Logs incoming requests, including headers and body.
    - Logs outgoing responses, including status codes and response data.

This middleware is useful for debugging and ensuring the API behaves as expected during development.

## Hawk Authentication

### Generate Hawk Credentials

To generate Hawk credentials (ID and key), send a `GET` request to the `/auth/hawk-auth/` endpoint. Ensure the user is authenticated.

**Request:**
```http
GET /auth/hawk-auth/ HTTP/1.1
Host: example.com
Authorization: Bearer <your-access-token>
```

**Response:**
```json
{
    "id": "generated-hawk-id",
    "key": "generated-hawk-key"
}
```

### Authenticate Using Hawk

To authenticate a request using Hawk, include the `Authorization` header in your request. The header must be generated using the Hawk protocol.

**Request:**
```http
POST /auth/hawk-auth/ HTTP/1.1
Host: example.com
Authorization: Hawk id="<hawk-id>", mac="<generated-mac>", ts="<timestamp>", nonce="<nonce>"
Content-Type: application/json
```

**Response (Success):**
```json
{
    "message": "Hawk authentication successful"
}
```

**Response (Failure):**
```json
{
    "error": "Invalid Hawk credentials"
}
```

## Project Structure

- `api_auth_proj/`: Main project directory.
- `myapp/`: Application directory containing views, models, serializers, etc.
- `requirements.txt`: List of dependencies.
- `manage.py`: Django's command-line utility for administrative tasks.

## License

This project is licensed under the MIT License.
