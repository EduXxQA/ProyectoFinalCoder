from django.contrib import admin
from django.urls import path
from CelTech.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('agrega-cliente/<nombre>/<apellido>/<numero>', cliente),
    path('lista-clientes', lista_clientes),
    path('', inicio, name = "Inicio"),
    path('agrega-funda/<modelo>/<tipo>/<precio>', agrega_funda),
    path('agrega-celular/<marca>/<modelo>/<precio>', agrega_celular),
    path('administrador-celulares', administrador_celulares, name="AdministradorCelulares"),
    path('administrador-accesorios', administrador_accesorios, name="AdministradorAccesorios"),
    path('administrador-fundas', administrador_fundas, name="AdministradorFundas"),  
    path('lista-celulares', lista_celulares, name="ListaCelulares"),
    path('lista-accesorios', lista_accesorios, name="ListaAccesorios"),  
    path('lista-fundas', lista_fundas, name="ListaFundas"),  
    path('eliminar-celular/<int:id>', eliminarCelular, name="EliminarCelular"),  
    path('eliminar-accesorio/<int:id>', eliminarAccesorio, name="EliminarAccesorio"),  
    path('eliminar-funda/<int:id>', eliminarFunda, name="EliminarFunda"),  
    path('editar-celular/<int:id>', editarCelular, name="EditarCelular"),  
    path('editar-accesorio/<int:id>', editarAccesorio, name="EditarAccesorio"),  
    path('editar-funda/<int:id>', editarFunda, name="EditarFunda"),
    path('administrador', administrador, name="Administrador"),  
    path('celulares', celulares, name="Celulares"),  
    path('fundas', fundas, name="Fundas"),  
    path('accesorios', accesorios, name="Accesorios"),  
    path('login', loginUsuario, name="Login"),
    path('registrar/', register, name="Registrar"),
    path('logout/', LogoutView.as_view(template_name= "inicio.html"), name="Logout"),
    #path('consulta/', consulta, name="Consulta"),
    path('buscar/', busquedaCelular , name="buscar"),
    path('resultado/', resultadoCelular , name="resultado"),


      
]
