#!/bin/bash

source /var/app/venv/staging-LQM1lest/bin/activate
python manage.py compilescss
python manage.py collectstatic --ignore=*.scss
