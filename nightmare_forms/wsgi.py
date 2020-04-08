"""
WSGI config for nightmare_forms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# This will set production as default, but we must still set it with an
# ENV on heroku to ensure that the migrate command runs agains the correct DB
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nightmare_forms.settings.prod')

application = get_wsgi_application()
