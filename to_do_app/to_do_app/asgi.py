"""
ASGI config for to_do_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Set the DJANGO_SETTINGS_MODULE environment variable to 'to_do_app.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'to_do_app.settings')

# Get the ASGI application for the Django project
application = get_asgi_application()

