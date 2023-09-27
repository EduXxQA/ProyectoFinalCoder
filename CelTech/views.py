from django.shortcuts import render
from .models import * 
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import *
# Create your views here.

def cliente(req, nombre, apellido, numero):
    
    cliente = Clientes(nombre=nombre, apellido=apellido, numero=numero)
    cliente.save()
    
    return HttpResponse(f"""
        <p>Cliente: {cliente.nombre} {cliente.apellido} AGREGADO!</p>                 
    """) 
    

def lista_clientes(req):
    
    lista = Clientes.objects.all()
    
    return render(req, "lista_clientes.html", {"lista_clientes": lista})

def inicio (req):
    
    return render (req, "inicio.html")



    
    



def loginUsuario (req): 
    
    if req.method == "POST":
        
        miFormulario = AuthenticationForm(req, data= req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]

            user= authenticate(username=usuario, password=psw)

            if user is not None:
                login(req,user)
                return render(req,"inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render (req, "inicio.html", {"mensaje": "Datos Incorrectos"})
        else : 
            return render (req, "inicio.html", {"mensaje": "Formulario Invalido"})
        
        
    else: 
            miFormulario = AuthenticationForm()
            return render (req, "login.html", {"miFormulario" : miFormulario})    
    
def register(req):

    if req.method == 'POST':

        miFormulario = UserCreationForm(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario = data["username"]

            miFormulario.save()

            return render(req, "inicio.html", {"mensaje": f"Usuario {usuario} creado con éxito!"})

        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})

    else:
        miFormulario = UserCreationForm()
        return render(req, "registro.html", {"miFomulario": miFormulario})
    

