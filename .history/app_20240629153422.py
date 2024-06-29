import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'votre_projet.settings')
application = get_wsgi_application()

if __name__ == '__main__':
    # Utilisation de Gunicorn comme serveur WSGI
    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 8000))
    workers = int(os.environ.get('WEB_CONCURRENCY', 1))
    bind = f"{host}:{port}"
    command = f"gunicorn -w {workers} -b {bind} votre_projet.wsgi"
    os.system(command)