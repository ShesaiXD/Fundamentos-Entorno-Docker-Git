#!/bin/bash
# espera simple (puedes usar wait-for-it o similar si quieres)
# Aplicar migraciones y crear superuser si hace falta
python manage.py migrate --noinput
# python manage.py collectstatic --noinput  # si usas staticfiles
exec gunicorn auth_service.wsgi:application --bind 0.0.0.0:8000