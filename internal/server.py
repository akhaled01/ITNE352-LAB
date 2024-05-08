import socket
from rich import console
from threading import Thread
from utils.handler import HandleConn

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8080))
server_socket.listen()

console.Console().print("TCP server is live on 127.0.0.1:8080", style="bold cyan")

while True:
    conn, addr = server_socket.accept()
    Thread(target=HandleConn, args=(conn, addr)).start()
