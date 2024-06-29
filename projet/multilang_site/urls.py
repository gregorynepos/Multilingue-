"""
URL configuration for multilang_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
     path('', views.home, name='home'),
    path('articles/', views.article_list, name='article_list'),
    path('admin/', admin.site.urls),
    path('chatbot/', views.chatbot_response, name='chatbot_response'),
    path('chatbot_view/', views.chatbot_view, name='chatbot_view'),  # Add a view for the chatbot form
]

urlpatterns += i18n_patterns(
    path('', include('django.conf.urls.i18n')),
)
