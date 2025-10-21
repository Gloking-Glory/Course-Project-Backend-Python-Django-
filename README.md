# Jece Project Backend

This is the backend service for the Jece Project, a RESTful API built with Django and Django REST Framework. It provides endpoints to manage university course information.

## Table of Contents

- [Features](#features)
- [System Architecture](#system-architecture)
- [Prerequisites](#prerequisites)
- [Local Setup](#local-setup)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Create a Virtual Environment](#2-create-a-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Set Up Environment Variables](#4-set-up-environment-variables)
  - [5. Run Database Migrations](#5-run-database-migrations)
  - [6. Run the Development Server](#6-run-the-development-server)
- [API Endpoints](#api-endpoints)
  - [Course Management](#course-management)
    - [Create a Course](#create-a-course)
    - [List Courses](#list-courses)
    - [Retrieve a Course](#retrieve-a-course)
    - [Update a Course](#update-a-course)
    - [Delete a Course](#delete-a-course)
- [Deployment](#deployment)

---

## Features

- **CRUD Operations**: Full Create, Read, Update, and Delete functionality for courses.
- **Filtering**: List courses with filters for `course_title` and `university`.
- **Pagination**: API responses for lists are paginated for efficient data handling.
- **CORS Enabled**: Cross-Origin Resource Sharing (CORS) is configured to allow requests from specified frontend origins.
- **API Throttling**: Rate limiting is in place to prevent abuse (`200 requests/day` for anonymous users, `1000 requests/day` for authenticated users).
- **Production Ready**: Includes security middleware, separate settings for production, and is configured for deployment.

## System Architecture

The backend is built using the **Django REST Framework** on top of the Django web framework.

- **Database**: The application can run with either SQLite (for development) or PostgreSQL (for production). The choice is determined by the `USE_POSTGRES` environment variable.
- **CORS**: `django-cors-headers` is used to handle cross-origin requests, making it possible for a separate frontend application (e.g., a React app running on `localhost:3000`) to communicate with the API.
- **Environment Configuration**: All sensitive data and environment-specific settings (like database credentials, secret key, and allowed hosts) are managed through a `.env` file using `python-dotenv`.

## Prerequisites

- Python 3.8+
- Pip (Python package installer)
- Git
- (Optional) PostgreSQL server for production-like setup.

## Local Setup

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd jeceProject
```

### 2. Create a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

A `requirements.txt` file is created with the necessary packages and install them.

**`requirements.txt`:**
```
Django
djangorestframework
django-cors-headers
django-filter
python-dotenv
dj-database-url
psycopg2-binary # Required for PostgreSQL
gunicorn # For production deployment
whitenoise # For production deployment
```

Install the packages:
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a file named `.env` in the project root (`jeceProject/`) and populate it with the following variables.

**`.env` file:**
```env
# Django Settings
SECRET_KEY=django-insecure-3f!o(3@8_2z-7u7l!t9p8*6l4+z3l&s@a$3p5x*e#k#z6(5b1
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost,domain.com,www.domain.com

# CORS Settings for Development
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

# Database Settings
# Set USE_POSTGRES to False to use SQLite for simple development
USE_POSTGRES=False

# --- PostgreSQL Credentials (only needed if USE_POSTGRES=True) ---
# DATABASE_NAME=your_db_name
# DATABASE_USER=your_db_user
# DATABASE_PASSWORD=your_db_password
# DATABASE_HOST=localhost
# DATABASE_PORT=5432
```

### 5. Run Database Migrations

This command creates the necessary database tables based on your models.

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

The API will now be available at `http://127.0.0.1:8000/`.

## API Endpoints

The API is versioned using URL path versioning. The base URL for the current version is `/api`.

### Course Management

#### Create a Course

- **Endpoint**: `POST /api/courses/add/-course`
- **Description**: Adds a new course to the database.
- **Request Body**:
  ```json
  {
      "course_title": "Introduction to Computer Science",
      "university": "Tech University",
      "duration": "4 years",
      "location": "Online",
      "fees": "20000.00"
  }
  ```
- **Success Response** (`201 CREATED`):
  ```json
  {
      "message": "Course created successfully",
      "data": { ... course object ... }
  }
  ```

#### List Courses

- **Endpoint**: `GET /api/courses/`
- **Description**: Retrieves a paginated list of all courses.
- **Query Parameters**:
  - `course_title` (string): Filter courses by title (case-insensitive, contains).
  - `university` (string): Filter courses by university (case-insensitive, contains).
  - `page` (integer): The page number for pagination.
- **Example**: `GET /api/courses/?university=Tech&page=2`

#### Retrieve a Course

- **Endpoint**: `GET /api/courses/<id>/`
- **Description**: Retrieves the details of a specific course by its ID.

#### Update a Course

- **Endpoint**: `PUT /api/courses/<id>/update/` or `PATCH /api/courses/<id>/update/`
- **Description**: Updates an existing course. `PUT` requires all fields, while `PATCH` allows partial updates.

#### Delete a Course

- **Endpoint**: `DELETE /api/courses/<id>/delete/`
- **Description**: Deletes a course from the database.

## Deployment

This project is configured for deployment to **AWS Elastic Beanstalk**. The `.elasticbeanstalk/config.yml` file contains the basic configuration for the EB CLI.

For a production deployment, ensure the following:
1.  Set `DEBUG=False` in your environment variables on the server.
2.  Configure `ALLOWED_HOSTS` to include your domain and the Elastic Beanstalk URL.
3.  Set up a PostgreSQL database (like AWS RDS) and configure the database environment variables accordingly.
4.  Set `USE_POSTGRES=True`.
5.  Configure `CORS_ALLOWED_ORIGINS` to your frontend's production URL.