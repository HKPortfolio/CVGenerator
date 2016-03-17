#!/bin/bash
source ENV/bin/activate
pip freeze > requirements.txt
deactivate