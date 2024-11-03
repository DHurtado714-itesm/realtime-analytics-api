import requests
import time

# API URL for retrieving stats
url = "http://localhost:80/stats"


def get_stats():
    """Send a single GET request to retrieve stats and track response time."""
    try:
        # Record the start time
        start_time = time.time()

        # Send the GET request
        response = requests.get(url)

        # Record the end time and calculate the duration
        end_time = time.time()
        response_time = end_time - start_time

        # Print the result with response time
        if response.status_code == 200:
            print(
                f"Retrieved stats successfully | Response Time: {response_time:.4f} seconds"
            )
        else:
            print(
                f"Failed to retrieve stats: {response.status_code}, {response.text} | Response Time: {response_time:.4f} seconds"
            )

        return response_time

    except Exception as e:
        print(f"Error: {e}")
        return None


# Track response times for analysis
response_times = []

# Number of continuous reads
num_requests = 50000 # You can adjust this to control how long the script runs

for _ in range(num_requests):
    # Send the request and store the response time
    response_time = get_stats()
    if response_time is not None:
        response_times.append(response_time)

    # Optional delay to control the request rate

# Calculate and print average response time
if response_times:
    avg_response_time = sum(response_times) / len(response_times)
    print(f"\nAverage Response Time: {avg_response_time:.4f} seconds")
else:
    print("No successful requests to calculate response time.")
