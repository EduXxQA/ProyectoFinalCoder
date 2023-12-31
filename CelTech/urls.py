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
    # path('administrador', administrador, name="Administrador"),  
    path('celulares', celulares, name="Celulares"),  
    path('fundas', fundas, name="Fundas"),  
    path('accesorios', accesorios, name="Accesorios"),  
    path('login', loginUsuario, name="Login"),
    path('registrar/', register, name="Registrar"),
    path('logout/', LogoutView.as_view(template_name= "inicio.html"), name="Logout"),
    #path('consulta/', consulta, name="Consulta"),
    path('buscarCF/', busquedaCelular , name="buscarCF"),
    path('resultadoCF/', resultadoCelular , name="resultado"),
    path('buscarAC/', busquedaAccesorios , name="buscarAC"),
    path('resultadoAC/', resultadoAC , name="resultadoAC"),
   
    # //////formulario contacto/////
    
    path('contacto/', contacto , name="contacto"),
    path('gracias/', gracias , name="gracias"),


   
    path('carrito/', carrito , name="carrito"),
    path('aboutus/', aboutus , name="AboutUs"),

    path('fundas-lista/', FundasList.as_view(), name="FundasLista"),
    path('fundas-detalle/<pk>', FundasDetail.as_view(), name="FundasDetalle"),
    path('fundas-crear/', FundasCreate.as_view(), name="FundasCrear"),
    path('fundas-actualizar/<pk>', FundasUpdate.as_view(), name="FundasActualizar"),
    path('fundas-eliminar/<pk>', FundasDelete.as_view(), name="FundasEliminar"),
    

      
]
