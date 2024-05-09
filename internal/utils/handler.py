from os import listdir
from rich.console import Console
from rich.traceback import install
import socket
import json

install()

def HandleConn(socket: socket.socket, addr: list):
    """
    This function handles individual connections
    with their requests
    """
    raw_data, _ = socket.recvfrom(4096)
    data = raw_data.decode("ascii")
    match data:
        case "GET fs-list":
            Console().print("RECIEVED GET fs-list REQUEST", style="bold yellow")
            Console().print_json(json=json.dumps(GetFS()))
            socket.sendto(json.loads(GetFS()), addr)


def GetFS() -> list[str]:
    return listdir("files")
