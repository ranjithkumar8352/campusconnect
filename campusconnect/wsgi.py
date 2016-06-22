"""
WSGI config for campusconnect project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/Library/Python/2.7/site-packages/django')

sys.path.append('/Users/sarthak') # this line solved it
sys.executable = '/usr/bin/python'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "campusconnect.settings")

application = get_wsgi_application()
