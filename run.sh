#!/bin/bash

#* Script to run the project quickly

virtualenv test_env 
cd test_env
source bin/activate
cd ..
clear
echo "Installing Required Dependencies"
pip install -r requirements.txt
python main.py
deactivate
rm -rf test_env