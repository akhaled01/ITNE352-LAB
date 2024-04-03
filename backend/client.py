import socket

SOCKET_ADDR = ('127.0.0.1', 9000)
SERVER_SOCKET_ADDR = ('127.0.0.1', 8080)

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsocket.bind(SOCKET_ADDR)

