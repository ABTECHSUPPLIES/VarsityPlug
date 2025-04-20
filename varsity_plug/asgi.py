"""
ASGI config for varsity_plug project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Set the default settings module for the 'varsity_plug' project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'varsity_plug.settings')

# Create the ASGI application for use by the web server
application = get_asgi_application()
