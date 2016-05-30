#!/bin/sh

python3 manage.py makemigrations
python3 manage.py migrate

uwsgi --ini ./docker/uwsgi.ini &
nginx -g 'daemon off;'
