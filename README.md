# Multilingual Django Application

## Description

Ce projet est une application Django multilingue simple qui affiche une liste d'articles de blog et permet aux utilisateurs de changer la langue de l'interface. De plus, il inclut une fonctionnalité optionnelle pour intégrer un chatbot utilisant un modèle de langage et une recherche augmentée par intelligence artificielle (RAG).

## Installation

### Prérequis

- Python 3.x
- pip (Python package installer)

### Étapes d'installation

1. **Clonez le dépôt :**
   ```bash
   git clone <repository_url>
   cd multilang_site
   ```
2. Créez et activez un environnement virtuel :

bash
Copier le code
python -m venv env
source env/bin/activate  
3. Installez les dépendances :

bash
Copier le code
pip install -r requirements.txt -U // -U pour mettre à jours les dépendances

4. Appliquez les migrations :

bash
Copier le code
python manage.py makemigrations
python manage.py migrate

5. Compilez les fichiers de traduction (si nécessaire) :

bash
Copier le code
python manage.py compilemessages

6. Démarrez le serveur de développement :

bash
Copier le code
python manage.py runserver

## Utilisation

Accédez à l'application dans votre navigateur :

arduino
Copier le code
http://127.0.0.1:8000/
Changer la langue :
Utilisez les liens en bas de la page pour changer la langue de l'interface (par exemple, Français,Portuguais,Italiens et English).

Interagir avec le chatbot (si intégré) :
Envoyez une requête POST à l'endpoint /chatbot/ avec un paramètre message pour obtenir une réponse du chatbot.

## Fonctionnalités

Affichage multilingue des articles de blog :

Les articles de blog sont affichés dans la langue sélectionnée par l'utilisateur.
Les éléments statiques de l'interface sont traduits en plusieurs langues.
Changement de langue :

Les utilisateurs peuvent changer la langue de l'interface en cliquant sur les liens de langue.

Chatbot intégré :

Un chatbot permet d'interagir avec un modèle de langage pour générer des réponses automatiques pour les reponses sont aléatoire.

## Déploiement

Connectez votre dépôt GitHub contenant le projet.
Configurez les paramètres du service (par exemple, choisissez le runtime Python, configurez les variables d'environnement).
Déployez l'application.
Documentation du Code

## Structure du Projet

multilang_site/ : Répertoire principal du projet.

settings.py : Configuration du projet.
urls.py : Configuration des routes principales.
wsgi.py : Configuration WSGI pour le déploiement.
main/ : Application principale.

models.py : Définition du modèle Article.
views.py : Définition des vues pour afficher les articles et gérer le chatbot.
urls.py : Configuration des routes spécifiques à l'application.
templates/ : Dossier contenant les templates HTML.
locale/ : Dossier contenant les fichiers de traduction.
Modèle Article
Le modèle Article contient les champs suivants :

title : Titre de l'article (CharField).
content : Contenu de l'article (TextField).
publication_date : Date de publication de l'article (DateTimeField).
Vue article_list
Affiche la liste des articles. Les articles sont récupérés de la base de données et passés au template article_list.html.

Vue chatbot (optionnelle)
Gère les requêtes POST pour interagir avec le modèle de langage. Utilise l'API d'OpenAI pour générer des réponses basées sur le message de l'utilisateur.

Utilisation de ChatGPT
J'ai utilisé ChatGPT pour les points suivants :

Recherche et clarification de concepts spécifiques à Django.
Génération de parties de code spécifiques.
Assistance pour l'intégration des modèles de langage.
Résolution de problèmes et débogage.
Temps total passé pour la réalisation du projet : 15 jours

Auteurs
Nepos - neposgregory@gmail.com
Merci pour cette opportunité et pour votre considération. Si vous avez des questions, n'hésitez pas à me contacter.

rust
Copier le code

N'hésitez pas à ajuster ce README en fonction de vos besoins spécifiques et des détails de votre implémentation.
