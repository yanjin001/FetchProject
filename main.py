import yaml
import requests
import time
from collections import defaultdict

# Constants
CONFIG_FILE_PATH = 'sample_input.yaml'
REQUEST_INTERVAL = 15  # Time in seconds between each health check
TIMEOUT = 0.5  # Timeout for each HTTP request in seconds


# Function to load the YAML configuration file
def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


# Function to send HTTP request and determine the health of an endpoint
def check_endpoint_health(endpoint):
    headers = endpoint.get('headers', {})
    body = endpoint.get('body', None)
    method = endpoint.get('method', 'GET')  # Default method is GET
    url = endpoint['url']

    try:
        response = requests.request(method, url, headers=headers, json=body, timeout=TIMEOUT)

        # Calculate the response latency in seconds.
        # `response.elapsed` returns a `timedelta` object representing the amount of time elapsed
        # between sending the request and the arrival of the response.
        # `total_seconds()` converts this to a floating point number representing the total number of seconds.
        # Note: The response latency can vary due to several factors such as network conditions, server response time,
        # and the physical distance between the client and the server. As it's dynamic and not fixed,
        # the actual output might differ from the expected results shown in the exercise.
        response_latency = response.elapsed.total_seconds()

        # Check if the status code is 2xx and latency is less than 500 ms
        is_up = response.status_code // 100 == 2 and response_latency < TIMEOUT

    except requests.RequestException:
        is_up = False

    return is_up


# Main function to run the health check program
def run_health_checks(config_file_path, request_interval):
    config = load_config(config_file_path)
    total_checks = defaultdict(int)
    up_checks = defaultdict(int)

    try:
        while True:

            for endpoint in config:
                # Extract the complete domain name, including 'www.' if present
                domain = endpoint['url'].split('/')[2]

                if check_endpoint_health(endpoint):
                    up_checks[domain] += 1
                total_checks[domain] += 1

            # Calculate and print the availability percentage for each domain
            for domain in total_checks:
                availability_percentage = (up_checks[domain] / total_checks[domain]) * 100
                print(f"{domain} has {round(availability_percentage)}% availability percentage")

            # Sleep before the next health check cycle
            time.sleep(request_interval)

    except KeyboardInterrupt:
        print("Health check program terminated.")


run_health_checks(CONFIG_FILE_PATH, REQUEST_INTERVAL)
