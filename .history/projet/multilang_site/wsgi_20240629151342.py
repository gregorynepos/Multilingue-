"""
WSGI config for multilang_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'multilang_site.settings')

application = get_wsgi_application()

from django.conf import settings
from django.core.management import call_command

if settings.DEBUG:
    application = get_wsgi_application()
else:
    from django.core.wsgi import get_wsgi_application
    from whitenoise.django import DjangoWhiteNoise
    application = get_wsgi_application()
    application = DjangoWhiteNoise(application)

# Ajout de cette vérification pour s'assurer que le serveur Gunicorn est correctement configuré
if __name__ == '__main__':
    # Utilisation de Gunicorn comme serveur WSGI
    import os
    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 8000))
    workers = int(os.environ.get('WEB_CONCURRENCY', 1))
    bind = f"{host}:{port}"
    command = f"gunicorn -w {workers} -b {bind} votre_projet.wsgi"
    os.system(command)
