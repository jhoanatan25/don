"""
WSGI config for Cadrs4drivers project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
if 'OPENSHIFT_REPO_DIR' in os.environ:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cars4driver.settings")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cars4driver.development")

application = get_wsgi_application()
