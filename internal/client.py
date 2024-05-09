from utils.ui import UI
from rich.console import Console
import socket
import sys
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8080))

while True:
    try:
        match UI():
            case 1:
                client_socket.send("GET fs-list".encode("ascii"))
            case 3:
                raise KeyboardInterrupt
    except KeyboardInterrupt:
        client_socket.close()
        Console().print("GOODBYE!", style="bold blue")
        time.sleep(1)
        Console().clear()
        sys.exit(0)
