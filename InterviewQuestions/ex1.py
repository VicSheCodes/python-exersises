from datetime import datetime, timedelta


def detect_attack(requests):
    # Dictionary to store requests count for each IP+port combination
    request_count = {}

    # List to store detected attacks
    attacks = []

    for request in requests:
        ip = request['ip']
        port = request['port']
        timestamp = datetime.strptime(request['timestamp'], '%Y-%m-%d %H:%M:%S')

        # Generate a unique key for each IP+port combination
        key = f"{ip}:{port}"

        # If the key exists in request_count dictionary, update the count, else initialize it to 1
        request_count[key] = request_count.get(key, 0) + 1

        # Check if the count exceeds 3 within a minute window
        if request_count[key] > 3:
            # Check if the time difference between current request and the first request in the window is greater than 1 minute
            if timestamp - attacks[0][0] >= timedelta(minutes=1):
                # If the time difference is greater than 1 minute, remove the first element from attacks list
                attacks.pop(0)

            # Append the current request to the attacks list
            attacks.append((timestamp, ip, port))

        # If the length of attacks list exceeds 0 and the time difference between current request and the first request in the window is greater than 1 minute
        if len(attacks) > 0 and timestamp - attacks[0][0] >= timedelta(minutes=1):
            # Clear the attacks list
            attacks.clear()

    return attacks


# Example usage
requests_bank = [
    {"ip": "192.168.1.1", "port": 8080, "timestamp": "2024-03-20 12:00:00"},
    {"ip": "192.168.1.2", "port": 8080, "timestamp": "2024-03-20 12:00:15"},
    {"ip": "192.168.1.1", "port": 8080, "timestamp": "2024-03-20 12:01:00"},
    {"ip": "192.168.1.1", "port": 8080, "timestamp": "2024-03-20 12:02:00"},
    {"ip": "192.168.1.1", "port": 8080, "timestamp": "2024-03-20 12:02:30"},
    {"ip": "192.168.1.1", "port": 8080, "timestamp": "2024-03-20 12:03:00"},
    {"ip": "192.168.1.1", "port": 8080, "timestamp": "2024-03-20 12:04:00"}
]

detected_attacks = detect_attack(requests_bank)
print("Detected Attacks:")
for attack in detected_attacks:
    print(f"IP: {attack[1]}, Port: {attack[2]}, Timestamp: {attack[0]}")
