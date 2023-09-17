from django.shortcuts import render
from .models import * 
from django.http import HttpResponse, HttpRequest

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

# def celular(req, marca, modelo, precio):
#     celular = Celulares(marca = marca, modelo = modelo, precio = precio)
#     celular.save()


def administrador(req):
    
    if req.method == 'POST':
       celular = Celulares(marca=req.POST['marca'], modelo=req.POST['modelo'], precio=req.POST['precio'])
       celular.save()
       return render(req, "administrador.html", {"mensaje": "Celular Agregado con éxito"})
        
    
    return render (req, "administrador.html")