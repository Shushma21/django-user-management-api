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

## ⚙️ Setup

```bash
git clone <repo-url>
cd project
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
