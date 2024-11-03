import requests
import time
import random

# API URL
url = "http://localhost:80/track"

# Sample data for page views
page_ids = ["home", "about", "contact", "blog", "pricing"]
user_ids = [f"user{n}" for n in range(1, 100)]  # Generate 20 sample user IDs


def send_track_request(page_id, user_id):
    """Send a single track request to the API and track response time."""
    payload = {"page_id": page_id, "user_id": user_id}
    try:
        # Record the start time
        start_time = time.time()

        # Send the request
        response = requests.post(url, json=payload)

        # Record the end time and calculate the duration
        end_time = time.time()
        response_time = end_time - start_time

        # Print the result with response time
        if response.status_code == 200:
            print(
                f"Successfully tracked page view: {page_id} by {user_id} | Response Time: {response_time:.4f} seconds"
            )
        else:
            print(
                f"Failed to track page view: {response.status_code}, {response.text} | Response Time: {response_time:.4f} seconds"
            )

        return response_time

    except Exception as e:
        print(f"Error: {e}")
        return None


# Track response times for analysis
response_times = []

# Send multiple requests
for _ in range(50000):  # Send 50 requests as an example
    page_id = random.choice(page_ids)
    user_id = random.choice(user_ids)

    # Send the request and store the response time
    response_time = send_track_request(page_id, user_id)
    if response_time is not None:
        response_times.append(response_time)


# Calculate and print average response time
if response_times:
    avg_response_time = sum(response_times) / len(response_times)
    print(f"\nAverage Response Time: {avg_response_time:.4f} seconds")
else:
    print("No successful requests to calculate response time.")
