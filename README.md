### README.md

# Real-Time Analytics API with FastAPI, MongoDB, and Redis

This project is a real-time analytics API built using **FastAPI** for handling requests, **MongoDB** for storing page view data, and **Redis** for caching data to improve performance. The API allows tracking of page views (`POST /track`) and retrieval of aggregated statistics (`GET /stats`).

## Features

- **Track Page Views**: Records each page view along with a unique user ID.
- **Retrieve Analytics**: Provides real-time analytics data such as the total number of views and unique visitors.
- **High Performance**: Uses Redis caching to reduce response times for high-frequency data retrieval.

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
   - `docker-compose.yml` (Docker setup for FastAPI, MongoDB, and Redis)

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

   This command starts the FastAPI application, MongoDB, and Redis.

2. **Access the API**:

   - FastAPI documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs).
   - Endpoints:
     - `POST /track` - Track page views
     - `GET /stats` - Retrieve real-time analytics

## Usage

### Endpoints

1. **Track Page View**: Sends a `POST` request to log a page view for a specific page and user.

   ```http
   POST http://localhost:8000/track
   Content-Type: application/json

   {
     "page_id": "home",
     "user_id": "user123"
   }
   ```

2. **Retrieve Stats**: Sends a `GET` request to fetch real-time analytics data.

   ```http
   GET http://localhost:8000/stats
   Content-Type: application/json
   ```

### Example Scripts

#### `send_multiple_tracks.py`

Simulates multiple `POST /track` requests to track page views from different users on various pages.

```python
python send_multiple_tracks.py
```

#### `read_multiple_tracks.py`

Simulates multiple `GET /stats` requests to repeatedly retrieve real-time analytics data.

```python
python read_multiple_tracks.py
```

Both scripts log response times for each request and provide an average response time at the end.

## Project Structure

```plaintext
real-time-analytics/
├── main.py            # Main FastAPI application
├── config.py          # Redis client configuration
├── database.py        # MongoDB connection setup
├── models.py          # Data models for MongoDB
├── views.py           # API endpoints
├── Dockerfile         # Dockerfile for FastAPI app
├── docker-compose.yml # Docker Compose setup
├── send_multiple_tracks.py  # Script for multiple write requests
└── read_multiple_tracks.py  # Script for multiple read requests
```

## Performance Testing

- Run the `send_multiple_tracks.py` script to test the average response time for tracking page views.
- Run the `read_multiple_tracks.py` script to test the average response time for retrieving analytics data.

The average response times for reading and writing operations are approximately:

- **Read Average Response Time**: ~0.0048 seconds
- **Write Average Response Time**: ~0.0050 seconds
