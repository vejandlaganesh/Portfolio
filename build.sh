#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
# Create the admin user from DJANGO_SUPERUSER_USERNAME / _EMAIL / _PASSWORD.
# Re-running is harmless: it just reports that the user already exists.
python manage.py createsuperuser --noinput || echo "NOTE: superuser not created (already exists, or DJANGO_SUPERUSER_* variables are not set)."
