from utils.client.interactions import GetFsFromServer, GetFileByOption
from utils.client.ui import UI, FileChooseUI
from rich.console import Console
from rich.traceback import install
from rich.prompt import Prompt
import socket
import sys
import time

install()  # pretty print all tracebacks


while True:
    '''
      client_socket always ends up getting closed when the thread ends.
      Hence, reconnection is required
    '''
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 8080))

    try:
        choice = UI()

        if choice == 1:
            Console().clear()
            for i, filename in enumerate(GetFsFromServer(client_socket)):
                Console().print(i, filename)
            while True:
                Prompt.ask("[bold blue] Press Enter to continue")
                break

        elif choice == 2:
            GetFileByOption(FileChooseUI(GetFsFromServer(client_socket)))

        elif choice == 3:
            raise KeyboardInterrupt

        elif choice == 4:
            client_socket.send("SIGTERM".encode(
                "ascii"))  # quit and end server
            raise KeyboardInterrupt

    except KeyboardInterrupt:
        client_socket.close()
        Console().print("GOODBYE!", style="bold blue")
        time.sleep(1)
        Console().clear()
        sys.exit(0)
