from rich import console
from rich.traceback import install
from threading import Thread
from utils.server.handler import HandleConn
import socket
import sys

install()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8080))
server_socket.listen()


console.Console().print("TCP server is live on 127.0.0.1:8080", style="bold cyan")

try:
    while True:
        conn, addr = server_socket.accept()
        conn_thread = Thread(target=HandleConn, args=(conn, server_socket))
        conn_thread.start()
        conn_thread.join() # wait for thread to finish
        conn.close()
except KeyboardInterrupt:
    server_socket.close()
    sys.exit(0)
