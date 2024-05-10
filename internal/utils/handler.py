from threading import current_thread
from os import listdir
from rich.console import Console
from rich.traceback import install
import socket
import json
import sys

install()


def HandleConn(socket: socket.socket, addr: list):
    """
    This function handles individual connections
    with their requests
    """
    try:
        raw_data, _ = socket.recvfrom(4096)
        data = raw_data.decode("ascii")
        match data:
            case "GET fs-list":
                Console().print("RECIEVED GET fs-list REQUEST", style="bold yellow")
                Console().print_json(json=json.dumps(GetFS()))
                socket.sendto(json.dumps(GetFS()).encode('ascii'), addr)
            case "SIGTERM":
                raise KeyboardInterrupt
    except KeyboardInterrupt:
        sys.exit(0)


def GetFS() -> list[str]:
    return listdir("internal/files")
