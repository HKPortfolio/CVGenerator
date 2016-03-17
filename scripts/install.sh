#!/bin/bash
sudo pip install virtualenv
virtualenv ENV -p python3
source ENV/bin/activate
pip install -r requirements.txt
deactivate