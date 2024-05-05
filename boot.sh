#!/bin/bash
# This script is used to boot the container with the web application.

while true; do
    FLASK_APP=src flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Deploy command failed, retrying in 5 secs...
    sleep 5
done

PYTHONPATH=. python src/scripts/script_2024_05_01_10_03_populate_db.py

exec gunicorn \
    -b :5000 \
    --access-logfile - \
    --error-logfile - \
    src:app
