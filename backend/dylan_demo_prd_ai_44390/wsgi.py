"""
WSGI config for dylan_demo_prd_ai_44390 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "dylan_demo_prd_ai_44390.settings"
)

application = get_wsgi_application()
