#!/bin/bash
python3 /code/dissen/manage.py migrate
python3 /code/dissen/manage.py runserver 0.0.0.0:8000
