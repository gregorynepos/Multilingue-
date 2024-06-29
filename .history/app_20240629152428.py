# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'Welcome to my Flask App!'

# # Ajoutez cette vérification pour s'assurer que le serveur Gunicorn est correctement configuré
# if __name__ == '__main__':
#     # Utilisation de Gunicorn comme serveur WSGI
#     import os
#     host = '0.0.0.0'
#     port = int(os.environ.get('PORT', 8000))
#     workers = int(os.environ.get('WEB_CONCURRENCY', 1))
#     bind = f"{host}:{port}"
#     command = f"gunicorn -w {workers} -b {bind} app:app"
#     os.system(command)