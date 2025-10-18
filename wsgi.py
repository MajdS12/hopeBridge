import os
from django.core.wsgi import get_wsgi_application
from decouple import config

# Use production settings if in production environment
settings_module = config('DJANGO_SETTINGS_MODULE', default='settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()