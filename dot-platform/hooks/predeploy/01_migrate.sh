#!/bin/bash

source /var/app/venv/staging-LQM1lest/bin/activate
python manage.py migrate --fake sessions zero
python manage.py showmigrations
python manage.py migrate --noinput
python manage.py migrate --fake-initial
python manage.py migrate
