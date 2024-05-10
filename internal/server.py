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
        server_socket.shutdown(0) # graceful shutdown of server
        server_socket.close()
        socket.close()
        sys.exit(0)


def server_loop():
    '''
    `server_loop` accepts connections from clients and 
    creates a `HandleConn` thread. It is assumed that an
    `OSError` is a Errno 9 (aka `server_socket` is offline), so it 
    will exit gracefully and end all threads (same with `KeyboardInterrupt`). 
    '''
    try:
        while True:
            conn, _ = server_socket.accept()
            conn_thread = Thread(target=HandleConn, args=(conn,))
            conn_thread.start()
            conn_thread.join()  # wait for thread to finish
            conn.close()
    except (OSError, KeyboardInterrupt):
        sys.exit(0)


if __name__ == "__main__":
    server_loop()
