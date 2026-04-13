# User Management API (Django + DRF)

📌 Project Overview

This is a backend API system built using Django and Django REST Framework.
It provides user authentication, role-based access control, and secure API handling using JWT.

## 🚀 Features
- User Registration
- JWT Authentication (Login)
- Role-Based Access Control (Admin/User)
- CRUD APIs for Users
- Current Logged-in User API
- Secure Password Hashing
- Input Validation
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
GET /api/users/(Admin only)
GET /api/users/{id}/
PUT /api/users/{id}/
DELETE /api/users/{id}/(Admin only)
GET /api/users/me/

## 🔒 Permissions
- Admin users can view and delete all users
- Normal users can only access their own data

## 📈 Future Improvements

Deploy on cloud (AWS / Render)


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

🔐 Authentication Usage

Include JWT token in headers:

Authorization: Bearer <access_token>

## ⚙️ Setup
```bash
git clone <repo-url>
cd project
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver



