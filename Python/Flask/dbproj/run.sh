#!/bin/bash

deactivate
source ./env/bin/activate
export FLASK_APP=hellodb.py
python3 -m flask run
deactivate
