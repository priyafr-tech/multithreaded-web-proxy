"""
proxy_server.py
Main proxy server implementation

Team: Titans
Project: Multithreaded Web Proxy with Content Filtering and LRU Caching
"""

import socket
import threading

HOST = "127.0.0.1"
PORT = 8888

def handle_client(client_socket):
    print("Client connected")
    request = client_socket.recv(1024)
    print("Request received:", request.decode(errors="ignore"))

    # TODO:
    # 1. Parse HTTP request
    # 2. Check access control
    # 3. Check cache
    # 4. Fetch from server if needed

    client_socket.close()

def start_proxy():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"Proxy running on {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        thread = threading.Thread(
            target=handle_client,
            args=(client_socket,)
        )
        thread.start()

if __name__ == "__main__":
    start_proxy()
