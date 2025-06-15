# Django-Next.js Boilerplate 🚀

![Django-Next.js Boilerplate](https://img.shields.io/badge/Version-1.0.0-blue.svg) ![License](https://img.shields.io/badge/License-MIT-green.svg) ![Docker](https://img.shields.io/badge/Docker-Enabled-brightgreen.svg)

Welcome to the **Django-Next.js Boilerplate**! This repository provides a fullstack boilerplate that combines a Django backend with a Next.js frontend. It's designed for easy deployment using Docker, making it perfect for developers looking to kickstart their projects.

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Folder Structure](#folder-structure)
6. [API Documentation](#api-documentation)
7. [Frontend Development](#frontend-development)
8. [Docker Setup](#docker-setup)
9. [Contributing](#contributing)
10. [License](#license)
11. [Links](#links)

## Features

- **Fullstack Solution**: Combines Django REST Framework (DRF) and Next.js for a seamless development experience.
- **Docker Support**: Easy to deploy using Docker and Docker Compose.
- **Scalable Architecture**: Built with scalability in mind, allowing you to expand as needed.
- **RESTful API**: Ready-to-use RESTful API endpoints for your frontend to consume.
- **Responsive Design**: Next.js provides server-side rendering and static site generation for optimal performance.

## Technologies Used

- **Backend**: 
  - Django
  - Django REST Framework (DRF)

- **Frontend**: 
  - Next.js (Version 14)

- **Containerization**: 
  - Docker
  - Docker Compose

- **Database**: 
  - PostgreSQL (recommended)

## Installation

To get started with the **Django-Next.js Boilerplate**, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mesiktc/Django-Next.js-Boilerplate.git
   cd Django-Next.js-Boilerplate
   ```

2. **Build the Docker containers**:
   ```bash
   docker-compose up --build
   ```

3. **Access the application**:
   - Backend: `http://localhost:8000`
   - Frontend: `http://localhost:3000`

4. **Run migrations**:
   Open a new terminal and run:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. **Create a superuser** (optional):
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

6. **Download and execute the latest release** from [here](https://github.com/mesiktc/Django-Next.js-Boilerplate/releases).

## Usage

After setting up the project, you can start developing your application. The backend provides RESTful API endpoints, while the frontend can consume these endpoints for a dynamic user experience.

### Backend API Endpoints

You can access the API documentation via the Django admin interface after creating a superuser. The default admin URL is `http://localhost:8000/admin`.

### Frontend Development

The frontend is built with Next.js. You can modify the pages located in the `frontend/pages` directory. The API calls can be made using `fetch` or libraries like `axios`.

## Folder Structure

Here's a brief overview of the folder structure:

```
Django-Next.js-Boilerplate/
│
├── backend/                # Django backend
│   ├── manage.py           # Django management script
│   ├── requirements.txt    # Python dependencies
│   └── your_app/           # Your Django app
│
├── frontend/               # Next.js frontend
│   ├── pages/              # Next.js pages
│   ├── components/         # React components
│   └── styles/             # CSS styles
│
├── docker-compose.yml      # Docker Compose configuration
└── Dockerfile              # Dockerfile for the backend
```

## API Documentation

The backend exposes several API endpoints. Below are some examples:

- **GET /api/items/**: Retrieve a list of items.
- **POST /api/items/**: Create a new item.
- **GET /api/items/{id}/**: Retrieve a specific item.
- **PUT /api/items/{id}/**: Update a specific item.
- **DELETE /api/items/{id}/**: Delete a specific item.

You can find more detailed API documentation in the Django admin interface.

## Frontend Development

The frontend uses Next.js, which allows for server-side rendering and static site generation. To add new pages, simply create a new file in the `frontend/pages` directory.

### Example of a Next.js Page

Here’s a simple example of a Next.js page that fetches data from the backend:

```javascript
import { useEffect, useState } from 'react';

const ItemsPage = () => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch('/api/items/')
      .then((response) => response.json())
      .then((data) => setItems(data));
  }, []);

  return (
    <div>
      <h1>Items</h1>
      <ul>
        {items.map((item) => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default ItemsPage;
```

## Docker Setup

The project uses Docker for easy deployment. The `docker-compose.yml` file defines the services required for both the backend and frontend.

### Docker Commands

- **Start the application**:
  ```bash
  docker-compose up
  ```

- **Stop the application**:
  ```bash
  docker-compose down
  ```

- **Access the Docker container**:
  ```bash
  docker-compose exec web bash
  ```

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request. Ensure that your code follows the existing style and includes tests where applicable.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes.
4. Test your changes.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Links

For the latest releases, visit [here](https://github.com/mesiktc/Django-Next.js-Boilerplate/releases). Download and execute the latest release to get started.

Explore the "Releases" section for updates and new features.