# miaplicacion/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.inicio, name='inicio'),
    path('login/',auth_views.LoginView.as_view(), name='login'),
    path('registro/', views.registro, name ='registro'),
    path('menuprincipal/', views.menuprincipal, name='menuprincipal'),
    path('recuperar/', views.recuperar, name='recuperar'),
    path('contacto/', views.contacto, name='contacto'),
    path('agenda/', views.agenda, name='agenda'),
    path('informacion/', views.informacion, name='informacion'),
]
