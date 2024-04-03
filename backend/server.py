import socket
import json
from rich.console import Console
from rich.traceback import install
from funcs.utils import ReadCSV, ParseCommand
from funcs.Employees import *

install()  # ensures any errors are printed in a pretty format on the terminal
main_data = ReadCSV('Employee_data.csv')
console = Console()
SERVER_SOCKET_ADDR = ('127.0.0.1', 8080)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(SERVER_SOCKET_ADDR)
console.print("[bold green]UDP Server Is live on 127.0.0.1:8080")

try:
    while True:
        data, client_addr = serverSocket.recvfrom(4096)
        client_command = data.decode('ascii')

        '''
        The code is designed to work in two modes. normal mode from the terminal menu, 
        or command mode by launching the client with -c.
        
        A command follows a format [GET <Argument> <name or title>]
        
        for example, if i wanted the full employee details of Tanner Kendrick, then the
        command from the client would be:
        
            "GET full-employee-Details Tanner Kendrick"
        
        If command mode is used, the client will explicitly send the command to the server
        and the server will in turn send the reply directly. However, menu mode would be much 
        more user firendly.
        
        Keep in mind that the client will always execute commands regardless of the mode, 
        but in a controlled manner. 
        '''

        if client_command == "TEST test-connection":  # NOTE - this is here to test the connections
            serverSocket.sendto(
                "CONNECTION-RECIEVED".encode('ascii'), client_addr)

        elif client_command.startswith("GET full-employee-Details"):  # NOTE - Q1
            response_data = json.dumps(GetAllEmpDetails(
                main_data, ParseCommand(client_command)))
            serverSocket.sendto(response_data.encode('ascii'), client_addr)

        elif client_command.startswith("GET gender-experience"):  # NOTE - Q2
            response_data = json.dumps(GenderExperienceDetails(
                main_data, ParseCommand(client_command)))
            serverSocket.sendto(response_data.encode('ascii'), client_addr)

        elif client_command.startswith("GET title-#"):  # NOTE - Q3
            response_data = json.dumps(PositionDetails(
                main_data, ParseCommand(client_command)))
            serverSocket.sendto(response_data.encode('ascii'), client_addr)

        elif client_command.startswith("GET list-title"):  # NOTE - Q4
            response_data = json.dumps(GetDetailsByPositionTitle(
                main_data, ParseCommand(client_command)))
            serverSocket.sendto(response_data.encode('ascii'), client_addr)

        else:  # NOTE - Handling invalid commands
            serverSocket.sendto(
                "400 - INVALID COMMAND".encode('ascii'), client_addr)

except KeyboardInterrupt:
    console.print("[bold blue] GOODBYE!")
finally:
    exit(0)
