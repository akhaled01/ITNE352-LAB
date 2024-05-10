# Lab 3 ITNE352

![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white) ![json](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white) ![apache](https://img.shields.io/badge/Apache-D22128?style=for-the-badge&logo=Apache&logoColor=white)

This project is a multithreaded TCP file server. A file server is any type of server that recives requests and serves files. Multithreading has been used to ensure multiple clients can connect at the same time. Good coding practices have been adhered to.

This Project tries to mimic some of `nginx`/`apache` functionality, but it is too "simple" for it to do so. It also tries to use HTTP-like syntax to communicate between server and client

## Steps For running the project

> It is preferable to use Linux OS for running this project

1. First, initialize a new virtualenv by running `python -m venv lab_env`
2. in the terminal, run `activate` if you are on `powershell`
   * If you are on `bash`/`zsh`, `cd lab_env`, then run `source bin/activate`
3. run `pip install -r requirements.txt`
4. if you are on linux, give the run script proper permissions by running `chmod 777 run.py`
   * If you are on windows, execute the script in an with admin privileges and allow firewall bypass
5. To run the TCP server, execute `python run.py server`
6. To run the TCP client, execute `python run.py client`

> It should be noted that `internal/files` houses the files served by the server, while `internal/client_files` houses the files requested by the client

## Libraries Used

1. `socket` for TCP socket utilities
2. `subprocess` for executing processes
3. `os` for file and dir manipulation
4. `sys` for handling system events gracefully
5. `json` for data serialization across sockets
6. `rich` for good terminal UI

### Done by Abdulrahman Idrees - 202200729
