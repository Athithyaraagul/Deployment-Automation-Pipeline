# Deployment Automation Pipeline

This project demonstrates a simple Python application with a complete CI/CD pipeline using GitHub Actions and Docker.

## Features

1.  **Simple Python App**: A Flask application with a greeting and health check endpoint.
2.  **Containerization**: `Dockerfile` included to build a lightweight image.
3.  **CI/CD**: GitHub Actions workflow (`.github/workflows/ci.yml`) that:
    *   Runs tests.
    *   Builds the Docker image.
    *   Simulates a deployment.
4.  **Health Check & Auto-Rollback**: A deployment script (`scripts/deploy.py`) that:
    *   Starts the container.
    *   Polls the `/health` endpoint.
    *   If healthy, marks deployment as successful.
    *   If unhealthy, stops the container (simulating a rollback).

## Getting Started

### Prerequisites

*   Python 3.9+
*   Docker (for local building/running)

### Running Locally

1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2.  Run the app:
    ```bash
    python app.py
    ```

3.  Visit `http://localhost:5000` or `http://localhost:5000/health`.

### Running Tests

```bash
pytest tests/
```

### Docker

Build the image:
```bash
docker build -t my-app .
```

Run the container:
```bash
docker run -p 5000:5000 my-app
```

## CI/CD Pipeline

Push changes to the `main` branch to trigger the pipeline.
The pipeline simulation runs on GitHub Actions runners, which have Docker installed.
