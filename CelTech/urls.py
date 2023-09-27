from django.contrib import admin
from django.urls import path
from CelTech.views import *

urlpatterns = [
   
    path('agrega-cliente/<nombre>/<apellido>/<numero>', cliente),
    path('lista-clientes', lista_clientes),
    path('', inicio, name = "Inicio"),
    
    path('login', loginUsuario, name="Login"),
    path('registrar/', register, name="Registrar"),
   
   

]
