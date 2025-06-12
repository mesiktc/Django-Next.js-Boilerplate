# Django + Next.js Boilerplate

A fullstack boilerplate with Django (DRF) backend and Next.js frontend, ready for Docker deployment.

## Features
- Django 4.x + DRF + JWT Auth
- Next.js 14+ (App Router, TypeScript, Tailwind CSS)
- PostgreSQL database
- Dockerized for local dev and production
- User registration, login, profile (JWT)
- Swagger/Redoc API docs

## Quick Start

### 1. Clone and configure
```bash
git clone <repo-url>
cd django+nextjs-biolerplate
cp backend/.env.example backend/.env  # Edit as needed
cp frontend/.env.example frontend/.env  # Edit as needed
```

### 2. Build and run with Docker Compose
```bash
docker-compose up --build
```
- Backend: http://localhost:8000
- Frontend: http://localhost:3000
- Swagger: http://localhost:8000/swagger/

### 3. Create a superuser (optional)
```bash
docker-compose exec backend python manage.py createsuperuser
```

## Directory Structure
```
django+nextjs-biolerplate/
├── backend/      # Django project
├── frontend/     # Next.js app
├── docker-compose.yml
└── README.md
```

## Environment Variables

### Backend (`backend/.env`)
See `backend/.env.example` for all available variables. Key variables:
- `DEBUG`
- `SECRET_KEY`
- `ALLOWED_HOSTS`
- `DB_ENGINE`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
- `JWT_SECRET_KEY`, `JWT_ACCESS_TOKEN_LIFETIME`, `JWT_REFRESH_TOKEN_LIFETIME`
- `EMAIL_BACKEND`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USE_TLS`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`
- `CORS_ALLOWED_ORIGINS`, `CSRF_TRUSTED_ORIGINS`

### Frontend (`frontend/.env`)
See `frontend/.env.example` for all available variables. Key variables:
- `NEXT_PUBLIC_API_URL`
- `NEXT_PUBLIC_APP_URL`
- `NEXT_PUBLIC_JWT_EXPIRY`, `NEXT_PUBLIC_JWT_REFRESH_EXPIRY`
- `NEXT_PUBLIC_ENABLE_REGISTRATION`, `NEXT_PUBLIC_ENABLE_EMAIL_VERIFICATION`

## Deployment
- Both backend and frontend build as Docker images
- Cloud-agnostic: deploy anywhere Docker is supported

---
MIT License 