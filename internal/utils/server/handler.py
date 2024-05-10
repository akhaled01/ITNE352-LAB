from utils.server.fs import GetFS, EncodeFile
from rich.traceback import install
import socket
import json
import sys

install()


def HandleConn(socket: socket.socket, server_socket: socket.socket):
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
