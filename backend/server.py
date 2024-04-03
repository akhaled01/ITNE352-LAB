import socket
import json
from rich.console import Console
from rich.traceback import install
from funcs.CSVIO import ReadCSV
from funcs.Employees import GetAllEmpDetails
install()

main_data = ReadCSV('Employee_data.csv')

console = Console()

SERVER_SOCKET_ADDR = ('127.0.0.1', 8080)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(SERVER_SOCKET_ADDR)
console.print("[bold green]UDP Server Is live on localhost:8080")

while True:
    data, client_addr = serverSocket.recvfrom(4096)
    client_command = data.decode('ascii')

    match client_command:
        case "GET test-connection":
            serverSocket.sendto(
                "CONNECTION-RECIEVED".encode('ascii'), client_addr)
        case command if command.startswith("GET full-employee-Details"):
            command_array = command.split(' ')
            nameOfEmployee = command_array[-1]
            Employee_Details = GetAllEmpDetails(nameOfEmployee)
            response_data = json.dumps(Employee_Details)
            serverSocket.sendto(response_data.encode('ascii'), client_addr)
