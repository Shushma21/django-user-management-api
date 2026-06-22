# User Management API (Django + DRF)

A backend REST API built with Django and Django REST Framework for user authentication, role-based access control, and secure user management.

## Features

- User Registration with validation
- JWT Authentication (Login & Token Refresh)
- Role-Based Access Control (Admin / User)
- Full CRUD API for Users
- Current Logged-in User endpoint
- Secure Password Hashing
- Pagination, Filtering & Search
- Swagger API Documentation
- Automated Tests

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (development) / PostgreSQL (production)
- JWT Authentication (SimpleJWT)
- drf-spectacular (Swagger)

## Setup

```bash
git clone https://github.com/Shushma21/django-user-management-api
cd django-user-management-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## API Endpoints

### Auth
| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| POST | `/api/users/register/` | Register a new user | Anyone |
| POST | `/api/token/` | Login and get JWT token | Anyone |
| POST | `/api/token/refresh/` | Refresh JWT token | Anyone |

### Users
| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| GET | `/api/users/` | List all users | Admin only |
| POST | `/api/users/` | Create a user | Authenticated |
| GET | `/api/users/{id}/` | Get a user | Authenticated |
| PUT | `/api/users/{id}/` | Update a user | Admin only |
| PATCH | `/api/users/{id}/` | Partial update | Admin only |
| DELETE | `/api/users/{id}/` | Delete a user | Admin only |
| GET | `/api/users/me/` | Get current user | Authenticated |

## Swagger Docs

Visit `http://127.0.0.1:8000/api/docs/` to explore and test the API interactively.

## Authentication

Include the JWT token in all protected requests:

```
Authorization: Bearer <access_token>
```

## Permissions

- **Admin** — can list, update and delete all users
- **Regular user** — can only view and update their own data

## Running Tests

```bash
python manage.py test apps.users.tests
```

## Sample Request

### Register
```json
POST /api/users/register/

{
    "username": "john",
    "email": "john@gmail.com",
    "password": "Test@1234",
    "role": "user"
}
```

### Response
```json
{
    "status": "success",
    "data": {
        "id": 1,
        "username": "john",
        "email": "john@gmail.com",
        "role": "user"
    }
}
```
