# Real-Time Analytics API with FastAPI, MongoDB, Redis, and NGINX

This project is a real-time analytics API built using **FastAPI** for handling requests, **MongoDB** for storing page view data, and **Redis** for caching data to improve performance. NGINX is used as a load balancer to distribute requests across multiple FastAPI instances, enabling horizontal scaling and improved handling of high request volumes.

## Features

- **Track Page Views**: Records each page view along with a unique user ID.
- **Retrieve Analytics**: Provides real-time analytics data, such as the total number of views and unique visitors.
- **High Performance and Scalability**: Uses Redis caching to reduce response times for frequent data retrieval and NGINX for load balancing across multiple FastAPI instances.

## Performance Metrics

- **Read Average Response Time**: ~0.0048 seconds
- **Write Average Response Time**: ~0.0050 seconds

These metrics are based on simulated multiple requests using the included scripts.

## Prerequisites

- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/)
- Python 3.7+

## Setup

1. Clone the repository and navigate to the project directory:

   ```bash
   git clone https://github.com/yourusername/real-time-analytics-api.git
   cd real-time-analytics-api
   ```

2. Ensure you have the following files:

   - `main.py` (FastAPI app)
   - `config.py` (configuration for Redis client)
   - `database.py` (MongoDB connection)
   - `models.py` (data models)
   - `views.py` (API endpoints)
   - `Dockerfile` (FastAPI Docker setup)
   - `docker-compose.yml` (Docker setup for FastAPI, MongoDB, Redis, and NGINX)
   - `nginx.conf` (NGINX configuration for load balancing)

3. Create a `requirements.txt` with the following dependencies:

   ```plaintext
   fastapi
   uvicorn
   motor
   redis
   pydantic
   ```

## Running the Application

1. **Build and Start the Containers**:

   ```bash
   docker-compose up --build
   ```

   This command starts the FastAPI application with multiple replicas, MongoDB, Redis, and NGINX for load balancing.

2. **Access the API**:

   - FastAPI documentation is available at [http://localhost/docs](http://localhost/docs) (proxied by NGINX).
   - Endpoints:
     - `POST /track` - Track page views
     - `GET /stats` - Retrieve real-time analytics

## Usage

### Endpoints

1. **Track Page View**: Sends a `POST` request to log a page view for a specific page and user.

   ```http
   POST http://localhost/track
   Content-Type: application/json

   {
     "page_id": "home",
     "user_id": "user123"
   }
   ```

2. **Retrieve Stats**: Sends a `GET` request to fetch real-time analytics data.

   ```http
   GET http://localhost/stats
   Content-Type: application/json
   ```

### Example Scripts

#### `send_multiple_tracks.py`

Simulates multiple `POST /track` requests to track page views from different users on various pages.

```bash
python send_multiple_tracks.py
```

#### `read_multiple_tracks.py`

Simulates multiple `GET /stats` requests to repeatedly retrieve real-time analytics data.

```bash
python read_multiple_tracks.py
```

Both scripts log response times for each request and provide an average response time at the end.

## Project Structure

```plaintext
real-time-analytics/
├── main.py               # Main FastAPI application
├── config.py             # Redis client configuration
├── database.py           # MongoDB connection setup
├── models.py             # Data models for MongoDB
├── views.py              # API endpoints
├── Dockerfile            # Dockerfile for FastAPI app
├── docker-compose.yml    # Docker Compose setup
├── nginx.conf            # NGINX configuration for load balancing
├── send_multiple_tracks.py  # Script for multiple write requests
└── read_multiple_tracks.py  # Script for multiple read requests
```

## Performance Testing

- Run the `send_multiple_tracks.py` script to test the average response time for tracking page views.
- Run the `read_multiple_tracks.py` script to test the average response time for retrieving analytics data.

The average response times for reading and writing operations are approximately:

- **Read Average Response Time**: ~0.0080 seconds
- **Write Average Response Time**: ~0.0079 seconds

## NGINX Load Balancing

This setup includes NGINX as a load balancer, configured in `nginx.conf`. The load balancer distributes incoming requests across multiple FastAPI instances, which improves scalability and enables the system to handle higher traffic.

NGINX configuration file (`nginx.conf`):

```nginx
events { }

http {
    upstream fastapi_app {
        # Load-balancing setup for FastAPI instances
        server app:8000;
        server app:8000;
        server app:8000;
    }

    server {
        listen 80;

        location / {
            proxy_pass http://fastapi_app;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
```
