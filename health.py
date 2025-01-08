import requests
import yaml
import time
from collections import defaultdict
from threading import Event

# Track cumulative data
domain_stats = defaultdict(lambda: {"up": 0, "total": 0})
stop_event = Event()

def parse_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def check_endpoint(endpoint):
    url = endpoint['url']
    method = endpoint.get('method', 'GET')
    headers = endpoint.get('headers', {})
    body = endpoint.get('body', None)

    start_time = time.time()

    try:
        response = requests.request(method, url, headers=headers, data=body, timeout=2)
        latency = (time.time() - start_time) * 1000

        if 200 <= response.status_code < 300 and latency < 500:
            return 'UP', latency
        else:
            return 'DOWN', latency
    except requests.RequestException:
        return 'DOWN', None

def log_availability():
    for domain, stats in domain_stats.items():
        availability = 100 * stats['up'] / stats['total'] if stats['total'] > 0 else 0
        print(f"{domain} has {round(availability)}% availability percentage")

def perform_health_checks(config):
    global domain_stats
    for endpoint in config:
        name = endpoint['name']
        url = endpoint['url']
        domain = url.split('//')[-1].split('/')[0]  # Extract domain

        status, latency = check_endpoint(endpoint)

        domain_stats[domain]['total'] += 1
        if status == 'UP':
            domain_stats[domain]['up'] += 1

        print(f"Checked {name}: {status} (Latency: {latency} ms)")

    log_availability()

def main(file_path):
    config = parse_config(file_path)

    print("Starting health checks. Press Ctrl+C to stop.")
    try:
        while not stop_event.is_set():
            perform_health_checks(config)
            time.sleep(15)
    except KeyboardInterrupt:
        print("Stopping health checks.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="HTTP Endpoint Health Checker")
    parser.add_argument('file_path', type=str, help="Path to the YAML configuration file")

    args = parser.parse_args()
    main(args.file_path)
