# Lab 2 ITNE352

This project is consists of both a UDP server that allows multiple UDP clients to query data from the `Employee_data.csv` file.

> It is preferable to use Linux OS for running this project
>
> To run the project, execute the `run.sh` script in either server or client mode in a proper environment

1. First, give the script proper permissions by running `chmod 777 run.sh`
2. To run the UDP server, type `./run.sh server`
3. To run the UDP client, type `./run.sh client`

## Libraries Used

1. `csv` for csv file operations
2. `socket` for UDP socket Manipulation
3. `json` for data serialization across sockets

### Done by Abdulrahman Idrees - 202200729
