from utils.fs import GetFS, EncodeFile
from rich.traceback import install
from rich.console import Console
from threading import Thread
import socket
import json
import sys

install()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8080))
server_socket.listen()


Console().print("TCP server is live on 127.0.0.1:8080", style="bold cyan")


def HandleConn(socket: socket.socket):
    """
      HandleConn handles individual connections
      with their requests
    """
    try:
        raw_data = socket.recv(2048)
        client_command = raw_data.decode("ascii")

        if client_command == "GET fs-list":
            socket.send(json.dumps(GetFS()).encode('ascii'))

        elif client_command.startswith("GET file"):
            socket.send(EncodeFile(
                int(client_command.split(" ")[2])).encode('ascii'))

        elif client_command == "SIGTERM":
            raise KeyboardInterrupt
    except KeyboardInterrupt:
        server_socket.close()
        socket.close()
        sys.exit(0)


def server_loop():
    try:
        while True:
            conn, _ = server_socket.accept()
            conn_thread = Thread(target=HandleConn, args=(conn, server_socket))
            conn_thread.start()
            conn_thread.join()  # wait for thread to finish
            conn.close()
    except KeyboardInterrupt:
        server_socket.close()
        sys.exit(0)


if __name__ == "__main__":
    server_loop()
