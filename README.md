# Django REST Framework Task Manager API

A simple Task Manager API built with **Django** and **Django REST Framework (DRF)** featuring **JWT authentication**.\
Users can register, log in, and perform CRUD operations on tasks.

---

## **Features**

- User registration & login (JWT auth)
- Create, read, update, and delete tasks
- Each task belongs to a specific user
- Swagger API documentation
- Unit tests for core functionality

---

## **Requirements**

- Python 3.10+
- Django 4.x
- Django REST Framework
- djangorestframework-simplejwt
- drf-yasg (Swagger)

---

## **Installation**

1. **Clone the repository**

```bash
git clone https://github.com/ayush2034/task-manager.git
cd task-manager
```

2. **Create and activate virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py migrate
```

5. **Create superuser (optional)**

```bash
python manage.py createsuperuser
```

---

## **Running the Project**

Start the development server:

```bash
python manage.py runserver
```

The API will be available at:

```
http://127.0.0.1:8000/api/
```

---

## **API Documentation**

Swagger UI:

```
http://127.0.0.1:8000/api/docs/
```

ReDoc:

```
http://127.0.0.1:8000/api/redoc/
```

---

## **Authentication**

### **Register**

`POST /api/auth/register/`

Request body:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

### **Login**

`POST /api/auth/login/`

Request body:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

Response:

```json
{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}
```

**Use the **``** token in all protected API requests**:

```
Authorization: Bearer <access_token>
```

---

## **Tasks API**

| Method | Endpoint         | Description                 |
| ------ | ---------------- | --------------------------- |
| GET    | /api/tasks/      | List all tasks for the user |
| POST   | /api/tasks/      | Create a new task           |
| GET    | /api/tasks/{id}/ | Retrieve task details       |
| PUT    | /api/tasks/{id}/ | Update a task               |
| DELETE | /api/tasks/{id}/ | Delete a task               |

### **Example: Create Task**

```json
POST /api/tasks/
Headers: Authorization: Bearer <access_token>
Body:
{
  "title": "My First Task",
  "description": "Learning Django REST Framework",
  "completed": false
}
```

Response:

```json
{
  "id": 1,
  "title": "My First Task",
  "description": "Learning Django REST Framework",
  "completed": false,
  "created_at": "2025-08-13T11:15:41.843573Z",
  "updated_at": "2025-08-13T11:15:41.843573Z"
}
```

---

## **Running Tests**

The project includes unit tests for authentication and task CRUD.\
Run tests with:

```bash
python manage.py test
```

You should see output like:

```
Found 3 test(s).
...
OK
```
---