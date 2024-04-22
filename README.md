# Lab 2 ITNE352

This project is a UDP server that allows multiple UDP clients to query data from the `Employee_data.csv` file.

> It is preferable to use Linux OS for running this project

## Steps For running the project

1. First, give the script proper permissions by running `chmod 777 run.sh`
2. To run the UDP server, type `./run.sh server`
3. To run the UDP client, type `./run.sh client`

> You can also use netcat to run this project by running `nc locahost 8080 -u`, You will have to use the command mode to run this project. To know more about the command mode, please read the documentation provided in `backend/server.py`

## Libraries Used

1. `csv` for csv file operations
2. `socket` for UDP socket Manipulation
3. `json` for data serialization across sockets
4. `rich` for good terminal UI

### Done by Abdulrahman Idrees - 202200729
