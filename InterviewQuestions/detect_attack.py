from collections import defaultdict
from datetime import datetime, timedelta


def check_attack(requests):
    # Dictionary to store timestamps for each unique (ip, port) combination
    timestamp_dict = defaultdict(list)

    # Threshold for the number of requests allowed in one minute
    threshold = 3

    # Time window duration (1 minute)
    window_duration = timedelta(minutes=1)

    # List to store detected attacks
    detected_attacks = []

    # Iterate through the list of requests
    for request in requests:
        ip = request['ip']
        port = request['port']
        timestamp = datetime.strptime(request['timestamp'], '%Y-%m-%d %H:%M:%S')

        # Get the list of timestamps for the current (ip, port) combination
        timestamps = timestamp_dict[ip, port]

        # Remove timestamps older than one minute
        while timestamps and timestamp - timestamps[0] > window_duration:
            timestamps.pop(0)

        # Add the current timestamp
        timestamps.append(timestamp)

        # Check if the count of timestamps exceeds the threshold
        if len(timestamps) >= threshold and (ip, port) not in detected_attacks:
            # Attack detected
            detected_attacks.append((ip, port))

    # Format the detected attacks for output
    if detected_attacks:
        return [f"Potential attack detected from {ip}:{port}." for ip, port in detected_attacks]
    else:
        return ["No potential attacks detected."]


requests_list = [
    {'ip': '192.168.1.1', 'port': 80, 'timestamp': '2024-03-12 12:00:00'},
    {'ip': '192.168.1.1', 'port': 80, 'timestamp': '2024-03-12 12:00:20'},
    {'ip': '192.168.1.1', 'port': 8080, 'timestamp': '2024-03-12 12:00:45'},
    {'ip': '192.168.1.1', 'port': 80, 'timestamp': '2024-03-12 12:01:50'},
    {'ip': '192.168.1.1', 'port': 80, 'timestamp': '2024-03-12 12:01:30'},
    {'ip': '192.168.1.1', 'port': 8080, 'timestamp': '2024-03-12 12:01:30'},
    {'ip': '192.168.1.1', 'port': 80, 'timestamp': '2024-03-12 12:01:31'},  # Attack
    {'ip': '192.168.1.1', 'port': 8080, 'timestamp': '2024-03-12 12:01:32'},  # Attack
]

results = check_attack(requests_list)
for result in results:
    print(result)
