# Microservice SDPX

A lightweight FastAPI microservice that provides mathematical operations and utility endpoints.

## Overview

This is a containerized Python microservice built with FastAPI, designed to demonstrate modern software development practices including:
- REST API development
- Unit testing
- Docker containerization
- Kubernetes deployment
- CI/CD with Jenkins

## Features

- **Multiply by 10 Endpoint**: Performs simple mathematical operation (multiply input by 10)
- **Greeting Endpoint**: Returns a greeting message
- **Production Ready**: Configured for deployment in Kubernetes
- **Fully Tested**: Includes unit tests for core functionality

## API Endpoints

### GET `/mul10/{num}`
Multiplies the provided number by 10.

**Parameters:**
- `num` (float): The number to multiply

**Response:**
```json
{
  "result": 50
}
```

**Example:**
```
GET /mul10/5
```

### GET `/getcode`
Returns a greeting message.

**Response:**
```json
{
  "code": "Helloooo, CEEEEEEE!"
}
```

## Project Structure

```
.
├── app/
│   ├── __init__.py         # Package initialization
│   └── main.py             # FastAPI application and endpoints
├── k8s/
│   ├── deployment.yaml     # Kubernetes deployment configuration
│   └── service.yaml        # Kubernetes service configuration
├── tests/
│   └── test_mul10.py       # Unit tests for mul10 endpoint
├── Dockerfile              # Docker image configuration
├── Jenkinsfile             # CI/CD pipeline configuration
└── requirements.txt        # Python dependencies
```

## Requirements

- Python 3.11+
- pip or conda package manager
- Docker (for containerization)
- Kubernetes (for deployment)
- Jenkins (for CI/CD)

## Installation

### Local Setup

1. **Clone the repository** (if applicable):
```bash
git clone <repository-url>
cd microservice_SDPX
```

2. **Create a virtual environment**:
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
# or
source venv/bin/activate      # On Linux/macOS
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

## Running the Application

### Local Development

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### Interactive API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Testing

Run the unit tests:

```bash
pytest tests/
```

Or with coverage:

```bash
pytest tests/ --cov=app
```

## Docker

### Build the Image

```bash
docker build -t microservice-sdpx:latest .
```

### Run the Container

```bash
docker run -p 8000:8000 microservice-sdpx:latest
```

The service will be accessible at `http://localhost:8000`

## Kubernetes Deployment

### Prerequisites
- Kubernetes cluster running
- kubectl configured to access your cluster

### Deploy to Kubernetes

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### Verify Deployment

```bash
kubectl get deployments
kubectl get services
kubectl get pods
```

### Access the Service

```bash
kubectl port-forward svc/microservice-sdpx 8000:8000
```

Then access the API at `http://localhost:8000`

## CI/CD Pipeline

This project includes a [Jenkinsfile](Jenkinsfile) for automated continuous integration and deployment. The pipeline typically includes:
- Code checkout
- Dependency installation
- Unit testing
- Docker image build
- Image registry push
- Kubernetes deployment

Refer to the [Jenkinsfile](Jenkinsfile) for detailed pipeline stages.

## Dependencies

Key dependencies included:
- **FastAPI** (0.131.0): Modern web framework for building APIs
- **Uvicorn**: ASGI web server
- **Pydantic**: Data validation
- **Pytest**: Testing framework

See [requirements.txt](requirements.txt) for the complete list.

## Development

### Adding New Endpoints

Edit [app/main.py](app/main.py) and add new route decorators:

```python
@app.get("/new-endpoint/{param}")
def new_endpoint(param: str):
    return {"result": param}
```

### Adding Tests

Add test functions to [tests/test_mul10.py](tests/test_mul10.py):

```python
def test_new_feature():
    response = client.get("/new-endpoint/test")
    assert response.status_code == 200
```

## Environment Variables

Currently, the application uses default configuration. For production deployments, consider adding environment variables for:
- API host and port
- Logging level
- Database connections (if applicable)

## Troubleshooting

### Port Already in Use
If port 8000 is already in use, specify a different port:
```bash
uvicorn app.main:app --port 8001
```

### Import Errors
Ensure you're in the virtual environment with dependencies installed:
```bash
pip install -r requirements.txt
```

### Kubernetes Connection Issues
Verify cluster connectivity:
```bash
kubectl cluster-info
```

## Contributing

1. Create a feature branch
2. Make your changes
3. Run tests to ensure nothing breaks
4. Submit pull request

## License

[Add your license here]

## Contact

For questions or issues, please open an issue in the repository.
