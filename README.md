# Django API Authentication Project

This project demonstrates how to set up a Django project with API authentication using Django REST framework.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- virtualenv (optional but recommended)

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/django-api-auth.git
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

## Project Structure

- `api_auth_proj/`: Main project directory.
- `myapp/`: Application directory containing views, models, serializers, etc.
- `requirements.txt`: List of dependencies.
- `manage.py`: Django's command-line utility for administrative tasks.

## License

This project is licensed under the MIT License.
