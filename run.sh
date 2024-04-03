#!/bin/bash

#NOTE - Done by Abdulrahman Idrees - ID: 202200729

source Lab2_env/bin/activate

if [[ $1 == "server" ]]; then
  python backend/server.py
elif [[ $1 == "client" ]]; then
  python backend/client.py
else
  echo "INVALID OPTION"
fi
  deactivate
