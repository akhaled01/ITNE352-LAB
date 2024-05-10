from utils.ui import UI
from rich.console import Console
from rich.prompt import Prompt
import socket
import sys
import json
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8080))

while True:
    try:
        match UI():
            case 1:
                client_socket.send("GET fs-list".encode("ascii"))
                raw_data, _ = client_socket.recvfrom(2048)
                data = json.loads(raw_data.decode("ascii"))
                for f in data:
                    Console().print(f)
                Prompt("").ask()
            case 3:
                raise KeyboardInterrupt
            case 4:
                client_socket.send("SIGTERM".encode("ascii"))
                raise KeyboardInterrupt
    except KeyboardInterrupt:
        client_socket.close()
        Console().print("GOODBYE!", style="bold blue")
        time.sleep(1)
        Console().clear()
        sys.exit(0)
