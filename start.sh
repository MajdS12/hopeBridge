#!/bin/bash
# Startup script for Railway deployment

# Activate virtual environment
source /opt/venv/bin/activate

# Run database migrations
python manage.py migrate --settings=settings_production

# Collect static files
python manage.py collectstatic --noinput --settings=settings_production

# Start the application
exec gunicorn --bind 0.0.0.0:$PORT --workers 3 --timeout 120 settings_production.wsgi:application
