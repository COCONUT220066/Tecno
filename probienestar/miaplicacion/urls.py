# miaplicacion/urls.py

from django.urls import path
from . import views

urlpatterns = [

    path('', views.inicio, name='inicio'),
    path('ingreso/', views.ingreso, name='ingreso'),
    path('registro/', views.registro, name='registro'),
    path('menuprincipal/', views.menuprincipal, name='menuprincipal'),
    path('recuperar/', views.recuperar, name='recuperar'),
    path('contacto/', views.contacto, name='contacto'),
    path('agenda/', views.agenda, name='agenda'),
    path('informacion/', views.informacion, name='informacion'),
    path('sintomas/', views.sintomas, name='sintomas')
]
