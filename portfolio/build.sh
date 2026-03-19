#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# --clear removes stale files (e.g. old back-bg.jpg) so backgrounds/CSS stay in sync
python manage.py collectstatic --no-input --clear
python manage.py migrate
