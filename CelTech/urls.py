from django.contrib import admin
from django.urls import path
from CelTech.views import *

urlpatterns = [
   
    path('agrega-cliente/<nombre>/<apellido>/<numero>', cliente),
    path('lista-clientes', lista_clientes),
    path('', inicio, name = "Inicio"),
    path('administrar-celulares', administar_celulares, name="AddministrarCelulares"),
    
]
