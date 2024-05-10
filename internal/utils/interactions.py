import socket
import json
import os


def GetFsFromServer(cs: socket.socket):
    '''
      Sends a `GET fs-list` request to server and returns 
      results
    '''
    cs.send("GET fs-list".encode("ascii"))
    raw_data = cs.recv(2048)
    return json.loads(raw_data.decode("ascii"))


def GetFileByOption(option: int):
    '''
      Kickstarts a new socket and recives file encoding.

      When recieved, it saves the file
    '''
    file_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_socket.connect(("127.0.0.1", 8080))
    file_socket.send(f"GET file {option}".encode("ascii"))

    os.makedirs("internal/client_files", mode=0o777, exist_ok=True)

    file_json_obj = json.loads(file_socket.recv(2048).decode("ascii"))
    with open("internal/client_files/"+file_json_obj["filename"], "w") as new_file:
        new_file.write(file_json_obj["content"])
