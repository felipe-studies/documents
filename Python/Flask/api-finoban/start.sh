#!/bin/bash

deactivate
source ./env/bin/activate
export FLASK_APP=api.py
python3 -m flask run
deactivate
