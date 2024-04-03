from funcs.UI import UI
import socket
import json

SOCKET_ADDR = ('127.0.0.1', 9000)
SERVER_SOCKET_ADDR = ('127.0.0.1', 8080)

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsocket.bind(SOCKET_ADDR)


op = input("[1] Command Mode, [2] Menu Mode: ")

if op == "1":
    command = input("Please enter command:")
    clientsocket.sendto(command.encode('ascii'), SERVER_SOCKET_ADDR)
    data, addr = clientsocket.recvfrom(4096)
    print(json.loads(data.decode('ascii')))
elif op == "2":
    UI(clientsocket)
