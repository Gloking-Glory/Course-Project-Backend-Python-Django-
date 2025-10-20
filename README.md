# jeceBackend

A robust backend system for the **Jece Project**, built with Django. This service powers the `courses` application and includes features for course analysis, details, update and delete.

---

## Table of Contents

- Features
- Technologies Used
  - Development Server
  - Running Tests
- API Overview
  - Authentication API
  - Courses API
- Code Quality

---

## Features

*   **REST API**: Exposes a clean RESTful API using Django REST Framework.

*   **Backend Framework**: Django
*   **API Frameworks**:
    *   Django REST Framework
*   **Databases**:
    *   SQLite
    *   PostgreSQL (via `psycopg2-binary`)
    *   MySQL (via `PyMySQL`)

## API Overview

The REST API is built with Django REST Framework. The main entry points are typically prefixed with `/api/`.

### Authentication API

*   **Obtain Token**: `POST /api/token/`
    *   Request Body: `{ "username": "your_username", "password": "your_password" }`
    *   Response: `{ "refresh": "...", "access": "..." }`
*   **Refresh Token**: `POST /api/token/refresh/`
    *   Request Body: `{ "refresh": "your_refresh_token" }`
    *   Response: `{ "access": "..." }`

### Courses API

These are the primary endpoints for managing courses.

*   `GET /api/courses/`: Retrieve a list of all available courses.
*   `POST /api/courses/`: Create a new course.
*   `GET /api/courses/{id}/`: Retrieve the details of a specific course.
*   `PUT /api/courses/{id}/`: Update a specific course.
*   `DELETE /api/courses/{id}/`: Delete a specific course.

## Code Quality
