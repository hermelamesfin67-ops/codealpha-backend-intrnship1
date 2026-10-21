# codealpha-backend-intrnship1
# Event Registration System API

A RESTful Event Registration System built with **Python, Django, Django REST Framework, and JWT authentication**. The API allows users to browse events, register for events, manage their registrations, and enforce event capacity and access permissions.

## Features

- User registration and secure password hashing
- JWT authentication and token-based login
- Event listing and event details
- Superuser-only event creation, updating, and deletion
- Authenticated event registration
- Prevention of duplicate registrations
- Event capacity validation
- Registration cancellation
- Users can view and manage their own registrations
- Superusers can view all registrations
- Validation of nonexistent event IDs

## Tech Stack

- Python
- Django
- Django REST Framework (DRF)
- Django REST Framework Simple JWT
- PostgreSQL
- Postman for API testing

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/hermelamesfin67-ops/codealpha-backend-intrnship1.git
cd event registration system
```

### 2. Create and activate a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```


### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file if your project uses environment variables. Configure your secret key, database credentials, and other required settings. Never commit real secrets or passwords to GitHub.

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

## Authentication

Obtain a JWT token using your configured token endpoint. For example:

```http
POST /token/
```

Use the returned access token in protected requests:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/users/` | Register a user |
| POST | `/token/` | Obtain JWT tokens |
| POST | `/token/refresh/` | Refresh an access token |
| GET | `/events/` | List events |
| POST | `/events/` | Create an event (superuser only) |
| GET | `/events/<id>/` | Retrieve an event |
| PUT/PATCH | `/events/<id>/` | Update an event (superuser only) |
| DELETE | `/events/<id>/` | Delete an event (superuser only) |
| GET | `/registrations/` | List registrations according to user permissions |
| POST | `/registrations/` | Register for an event |
| GET | `/registrations/<id>/` | Retrieve an authorized registration |
| DELETE | `/registrations/<id>/` | Cancel an authorized registration |

*Confirm these paths against your actual `urls.py` before publishing.*

## Validation and Permissions

- Users must authenticate before registering for events.
- Users cannot register for the same event twice.
- Registration is rejected when event capacity is reached.
- Invalid event IDs are rejected.
- Ordinary users can access only their own registrations.
- Superusers can view all registrations.
- Event creation and modifications are restricted to superusers.

## Testing

The API was tested using Postman, including authentication, event creation, event registration, cancellation, duplicate-registration prevention, invalid event IDs, capacity validation, and permission checks.

## Future Improvements

- Automated tests with Django's test framework
- API documentation using Swagger/OpenAPI
- Event search and filtering
- Deployment to a production hosting platform

## Author

**Hermela Mesfin**

Aspiring Backend Developer | Python & Django REST Framework

GitHub:[[https://github.com/hermelamesfin67-ops/](codealpha-backend-intrnship1.git)]

