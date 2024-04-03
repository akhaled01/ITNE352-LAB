#!/bin/bash

cd Lab2_env
source bin/activate
cd ..

if [[ $1 == "server" ]]; then
  python backend/server.py
elif [[$1 == "client"]]; then
  python backend/client.py
else
  echo "INVALID OPTION"
fi


deactivate
