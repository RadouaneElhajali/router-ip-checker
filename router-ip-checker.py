import socket
import requests

def is_ip_reachable(ip):
    try:
        socket.create_connection((ip, 80), timeout=1)
        return True
    except (socket.timeout, socket.error):
        return False

def is_router_page(ip):
    url = f"http://{ip}/"
    try:
        response = requests.get(url, timeout=1)
        return "html" in response.headers.get('content-type', '').lower()
    except requests.ConnectionError:
        return False

def find_router():
    for i in range(1, 255):
        ip = f"192.168.1.{i}"
        if is_ip_reachable(ip) and is_router_page(ip):
            print(f"Router found at {ip}")
            break
        else:
            print(f"Checking {ip}...")

if __name__ == "__main__":
    find_router()
