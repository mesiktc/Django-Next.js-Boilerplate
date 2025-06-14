# Django + Next.js Boilerplate

A modern web application boilerplate using Django for the backend and Next.js for the frontend.

## Features

- **Backend (Django)**
  - Django REST Framework for API endpoints
  - JWT Authentication
  - Google OAuth2 Authentication
  - PostgreSQL Database
  - CORS Configuration
  - Swagger/OpenAPI Documentation
  - Payment Integration (Stripe & LemonSqueezy)
  - Subscription Management

- **Frontend (Next.js)**
  - TypeScript Support
  - Tailwind CSS for Styling
  - React Bootstrap Components
  - Protected Routes
  - Authentication Flow
  - Payment Screen
  - Responsive Design

## Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL
- Stripe Account (for payments)
- LemonSqueezy Account (optional, alternative payment provider)

## Setup

### Backend Setup

1. Create and activate a virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
```
Edit `.env` with your configuration:
```
# Django Settings
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Settings
DATABASE_URL=postgres://user:password@localhost:5432/dbname

# Email Settings
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

# Google OAuth2 Settings
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GOOGLE_CALLBACK_URL=http://localhost:3000/auth/google/callback

# Payment Settings
PAYMENT_PROVIDER=stripe  # or lemonsqueezy

# Stripe Settings
STRIPE_PUBLIC_KEY=your_stripe_public_key
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_WEBHOOK_SECRET=your_stripe_webhook_secret

# LemonSqueezy Settings
LEMON_SQUEEZY_API_KEY=your_lemonsqueezy_api_key
LEMON_SQUEEZY_WEBHOOK_SECRET=your_lemonsqueezy_webhook_secret
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

### Frontend Setup

1. Install dependencies:
```bash
cd frontend
npm install
```

2. Set up environment variables:
```bash
cp .env.example .env.local
```
Edit `.env.local` with your configuration:
```
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
```

3. Start the development server:
```bash
npm run dev
```

## Payment System

The boilerplate includes a complete payment system with the following features:

### Backend

- Payment plan management
- Subscription handling
- Payment processing
- Support for multiple payment providers (Stripe & LemonSqueezy)

### Frontend

- Payment plan display
- Subscription management
- Protected routes based on subscription status
- Responsive payment UI

### Setting Up Payments

1. **Stripe Setup**
   - Create a Stripe account
   - Get your API keys from the Stripe dashboard
   - Create products and prices in Stripe
   - Update the `provider_price_id` in the payment plans with your Stripe price IDs

2. **LemonSqueezy Setup (Optional)**
   - Create a LemonSqueezy account
   - Get your API key from the dashboard
   - Create products in LemonSqueezy
   - Update the `provider_price_id` in the payment plans with your LemonSqueezy variant IDs

3. **Configure Payment Provider**
   - Set `PAYMENT_PROVIDER=stripe` or `PAYMENT_PROVIDER=lemonsqueezy` in your backend `.env` file
   - Add the corresponding API keys and secrets

## API Documentation

Once the backend server is running, you can access the API documentation at:
- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
