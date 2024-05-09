# Lab 3 ITNE352

This project is a multithreaded TCP file server.

> It is preferable to use Linux OS or Git Bash for running this project

## Steps For running the project

1. First, initialize a new virtualenv by running `python -m venv lab_env`
2. in the terminal, run `activate` if on windows
   1. If on linux, `cd lab_env` then run `source bin/activate`
3. run `pip install -r requirements.txt`
4. give the run script proper permissions by running `chmod 777 run.py`
5. To run the TCP server, type `python run.py server`
6. To run the TCP client, type `python run.py client`

## Libraries Used

2. `socket` for UDP socket Manipulation
3. `json` for data serialization across sockets
4. `rich` for good terminal UI

### Done by Abdulrahman Idrees - 202200729
