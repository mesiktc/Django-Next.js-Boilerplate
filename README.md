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
- See `backend/.env.example` for backend config
- Frontend uses `NEXT_PUBLIC_API_URL` (set in docker-compose)

## Deployment
- Both backend and frontend build as Docker images
- Cloud-agnostic: deploy anywhere Docker is supported

---
MIT License 