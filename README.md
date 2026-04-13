# User Management API (Django + DRF)

## 🚀 Features
- User Registration
- JWT Authentication (Login)
- Role-Based Access Control (Admin/User)
- CRUD APIs for Users
- Pagination & Permissions

## 🛠 Tech Stack
- Python
- Django
- Django REST Framework
- SQLite
- JWT Authentication

## 🔗 API Endpoints

### Auth
POST /api/users/register/
POST /api/token/

### Users
GET /api/users/
GET /api/users/{id}/
PUT /api/users/{id}/
DELETE /api/users/{id}/

## 🔒 Permissions
- Admin users can view and delete all users
- Normal users can only access their own data
## ⚙️ Setup

## 📌 Sample API Request

### Register User

POST /api/users/register/

Request:
{
"username": "shushma",
"email": "[shushma@gmail.com](mailto:shushma@gmail.com)",
"password": "test123",
"role": "user"
}

Response:
{
"id": 1,
"username": "shushma",
"email": "[shushma@gmail.com](mailto:shushma@gmail.com)",
"role": "user"
}

```bash
git clone <repo-url>
cd project
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver



