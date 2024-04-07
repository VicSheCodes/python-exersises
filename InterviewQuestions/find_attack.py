'''
CATO
'''

from datetime import datetime, timedelta

requests = [
    {"ip": "192.168.1.1", "port": 8080, "timestamp": "2024-03-20 12:00:00"},
    {"ip": "192.168.1.2", "port": 8081, "timestamp": "2024-03-20 12:00:15"},
    {"ip": "192.168.1.1", "port": 8080, "timestamp": "2024-03-20 12:01:00"},
    {"ip": "192.168.1.3", "port": 8082, "timestamp": "2024-03-20 12:02:00"},
    {"ip": "192.168.1.4", "port": 8083, "timestamp": "2024-03-20 12:02:30"},
    {"ip": "192.168.1.1", "port": 8080, "timestamp": "2024-03-20 12:03:00"},
    {"ip": "192.168.1.5", "port": 8084, "timestamp": "2024-03-20 12:04:00"}
]


def detect_attack(requests):
    request_count = 0
    detected_attacks = []
    for req in requests:
        ip = requests['Ip']
        port = requests['Port']
        time = datetime.strptime(requests['Timestamp'], '%Y-%m-%d %H:%M:%S')

        key = f"{ip}:{port}"


def test_detected_attack():
    detected_attacks = detect_attack(requests)
    print("Detected Attacks:")
    for attack in detected_attacks:
        print(f"IP: {attack[1]}, Port: {attack[2]}, Timestamp: {attack[0]}")
