from django.shortcuts import render
from .models import * 
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.db.models import   Q
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.list import ListView
# from django.shortcuts import render, redirect
from django.core.mail import send_mail
from ProyectoFinal import settings
from django.template.loader import render_to_string



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

def agrega_funda(req, modelo, tipo, precio):
    
    funda = Fundas(modelo=modelo, tipo=tipo, precio=precio)
    funda.save()
    
    return HttpResponse(f"""
        <p>Funda: {funda.modelo} - {funda.tipo} - ${funda.precio} AGREGADA</p>        
    """)
    
def agrega_celular(req, marca, modelo, precio):
    
    celular = Celulares(marca=marca, modelo=modelo, precio=precio)
    celular.save()
    
    return HttpResponse(f"""
        <p>Celular: {celular.marca} - {celular.modelo} - ${celular.precio} AGREGADO</p>        
    """)    


def administrador_celulares(req: HttpRequest):
    
    print('method', req.method)
    print('post', req.POST) 
    
    
       
    if req.method == 'POST':
        lista_celular = Celulares.objects.all()        
        agregarCelular = AdministradorCelulares(req.POST)
        
        if agregarCelular.is_valid():
            
            print(agregarCelular.cleaned_data)
            data = agregarCelular.cleaned_data
        
            celular = Celulares(marca=data["marca"], modelo=data["modelo"], precio=data["precio"])
            celular.save()
            return render(req, "lista_celulares.html", {"lista_celulares": lista_celular, "mensaje_celular": "Celular agregado correctamente"})    
        else:
            return render(req, "lista_celulares.html", {"lista_celulares": lista_celular, "mensaje_celular": "El celular no pudo ser agrgado"})    
    else:
        agregarCelular = AdministradorCelulares()       
        return render(req, "administrador_celulares.html", {"agregarCelular": agregarCelular}) 

def administrador_accesorios(req: HttpRequest):
    
    print('method', req.method)
    print('post', req.POST)
    
    if req.method == 'POST':
        lista_accesorio = Accesorios.objects.all()
        agregarAccesorio = AdministradorAccesorios(req.POST)
        
        if agregarAccesorio.is_valid():
            print(agregarAccesorio.cleaned_data)
            data = agregarAccesorio.cleaned_data
            
            accesorio = Accesorios(marca=data["marca"], tipo=data["tipo"], precio=data["precio"])
            accesorio.save()
            return render(req, "lista_accesorios.html", {"lista_accesorios": lista_accesorio, "mensaje_accesorio": "Accesorio agregado correctamente"})        
        else:
            return render(req, "lista_accesorios.html", {"lista_accesorios": lista_accesorio, "mensaje_accesorio": "El accesorio no pudo ser agrgado"})    
    else:
        agregarAccesorio = AdministradorAccesorios()    
        return render(req, "administrador_accesorios.html", {"agregarAccesorio": agregarAccesorio}) 

def administrador_fundas(req: HttpRequest):
    
    print('method', req.method)
    print('post', req.POST)
    
    if req.method == 'POST':
        lista_funda = Fundas.objects.all()
        agregarFunda = AdministradorFundas(req.POST)
        
        if agregarFunda.is_valid():
            print(agregarFunda.cleaned_data)
            data = agregarFunda.cleaned_data
            
            funda = Fundas(modelo=data["modelo"], tipo=data["tipo"], precio=data["precio"])
            funda.save()
            return render(req, "lista_fundas.html", {"lista_fundas": lista_funda, "mensaje_funda": "Funda agregada correctamente"})
        else:
            return render(req, "lista_fundas.html", {"lista_fundas": lista_funda, "mensaje_funda": "La funda no pudo ser agregada"})
    else:
        agregarFunda = AdministradorFundas()
        return render(req, "administrador_fundas.html", {"agregarFunda": agregarFunda}) 


def lista_celulares(req):
    
    lista_celular = Celulares.objects.all()
    
    return render(req, "lista_celulares.html", {"lista_celulares": lista_celular})



def lista_accesorios(req):
    
    lista_accesorio = Accesorios.objects.all()
    
    return render(req, "lista_accesorios.html", {"lista_accesorios": lista_accesorio})

def lista_fundas(req):
    
    lista_funda = Fundas.objects.all()
    
    return render(req, "lista_fundas.html", {"lista_fundas": lista_funda})

def eliminarCelular(req, id):
    
    if req.method == 'POST': 
        
        celular = Celulares.objects.get(id=id)
        celular.delete()
       
        lista_celulares = Celulares.objects.all()
        
        return render(req, "lista_celulares.html", {"lista_celulares": lista_celulares})
    
def eliminarAccesorio(req, id):
    
    if req.method == 'POST': 
        
        accesorio = Accesorios.objects.get(id=id)
        accesorio.delete()
       
        lista_accesorios = Accesorios.objects.all()
        
        return render(req, "lista_accesorios.html", {"lista_accesorios": lista_accesorios})
    
def eliminarFunda(req, id):
    
    if req.method == 'POST': 
        
        funda = Fundas.objects.get(id=id)
        funda.delete()
       
        lista_fundas = Fundas.objects.all()
        
        return render(req, "lista_fundas.html", {"lista_fundas": lista_fundas})
    

def editarCelular(req, id):
    lista_celular = Celulares.objects.all() 
    celular = Celulares.objects.get(id=id)
    
    if req.method == 'POST':
        
        agregarCelular = AdministradorCelulares(req.POST)
        
        if agregarCelular.is_valid():
            
            print(agregarCelular.cleaned_data)
            data = agregarCelular.cleaned_data
        
            celular.marca = data["marca"]
            celular.modelo = data["modelo"]
            celular.precio = data["precio"]
            
            celular.save()
            return render(req, "lista_celulares.html", {"lista_celulares": lista_celular, "mensaje_celular": "Celular actualizado correctamente"})    
        else:
            return render(req, "lista_celulares.html", {"lista_celulares": lista_celular, "mensaje_celular": "El celular no pudo ser actualizado"})    
    else:
        agregarCelular = AdministradorCelulares(initial={
            "marca": celular.marca,
            "modelo": celular.modelo,
            "precio": celular.precio,
                
        })       
        return render(req, "editar_celular.html", {"agregarCelular": agregarCelular, "id": celular.id}) 
    
    

def editarAccesorio(req, id):
    lista_accesorio = Accesorios.objects.all() 
    accesorio = Accesorios.objects.get(id=id)
    
    if req.method == 'POST':
        
        agregarAccesorio = AdministradorAccesorios(req.POST)
        
        if agregarAccesorio.is_valid():
            
            print(agregarAccesorio.cleaned_data)
            data = agregarAccesorio.cleaned_data
        
            accesorio.marca = data["marca"]
            accesorio.tipo = data["tipo"]
            accesorio.precio = data["precio"]
            
            accesorio.save()
            return render(req, "lista_accesorios.html", {"lista_accesorios": lista_accesorio, "mensaje_accesorio": "Accesorio actualizado correctamente"})    
        else:
            return render(req, "lista_accesorios.html", {"lista_accesorios": lista_accesorio, "mensaje_accesorio": "El accesorio no pudo ser actualizado"})    
    else:
        agregarAccesorio = AdministradorAccesorios(initial={
            "marca": accesorio.marca,
            "tipo": accesorio.tipo,
            "precio": accesorio.precio,
                
        })       
        return render(req, "editar_accesorio.html", {"agregarAccesorio": agregarAccesorio, "id": accesorio.id}) 
    

def editarFunda(req, id):
    lista_funda = Fundas.objects.all() 
    funda = Fundas.objects.get(id=id)
    
    if req.method == 'POST':
        
        agregarFunda = AdministradorFundas(req.POST)
        
        if agregarFunda.is_valid():
            
            print(agregarFunda.cleaned_data)
            data = agregarFunda.cleaned_data
        
            funda.modelo = data["modelo"]
            funda.tipo = data["tipo"]
            funda.precio = data["precio"]
            
            funda.save()
            return render(req, "lista_fundas.html", {"lista_fundas": lista_funda, "mensaje_funda": "Funda actualizada correctamente"})    
        else:
            return render(req, "lista_fundas.html", {"lista_fundas": lista_funda, "mensaje_funda": "La funda no pudo ser actualizada"})    
    else:
        agregarFunda = AdministradorFundas(initial={
            "modelo": funda.modelo,
            "tipo": funda.tipo,
            "precio": funda.precio,
                
        })       
        return render(req, "editar_funda.html", {"agregarFunda": agregarFunda, "id": funda.id})     
    
# def administrador (req):
    
#     return render (req, "administrador.html")
    
    
    
def celulares(req):
    
    celulares = Celulares.objects.all()
    
    return render(req, "celulares.html", {"celulares": celulares})


def fundas(req):
    
    fundas = Fundas.objects.all()
    
    return render(req, "fundas.html", {"fundas": fundas})

def accesorios(req):
    
    accesorio = Accesorios.objects.all()
    
    return render(req, "accesorios.html", {"accesorios": accesorio})


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
    
   
    
    

def busquedaCelular(req):
  busqueda= req.GET.get("buscar")  
  
  celulares=Celulares.objects.all()
  fundas =Fundas.objects.all()  
  
  
  if busqueda :
        celulares =Celulares.objects.filter(
        Q(modelo__icontains = busqueda)
        
        )
        fundas = Fundas.objects.filter(
            Q(modelo__icontains = busqueda)

        )

   

        
        if celulares and fundas:
            return render(req,"resultado_CF.html", {"celulares":celulares , "fundas": fundas})
        
        elif celulares:

            return render (req,"resultado_CF.html",{"celulares": celulares})
        
        elif fundas:
            return render (req,"resultado_CF.html",{"fundas": fundas})
        
    

        else: 
            return render (req,"resultado_CF.html", {"mc": "Modelo no encontrado"})
  else:
      return render(req,"buscar_CF.html")
  
  


      
      


# //////////// BUSQUEDA ACCESORIOS//////////
def busquedaAccesorios(req):
  busqueda= req.GET.get("buscar2")
  accesorios=Accesorios.objects.all()
  
  if busqueda:
        accesorios =Accesorios.objects.filter(
        Q(tipo__icontains = busqueda)
       
        )
        
        
        if accesorios :
            return render(req,"resultado_AC.html", {"accesorios":accesorios})
        
        

        else: 
            return render (req,"resultado_AC.html", {"mc": "Accesorio no encontrado"})
  else:
      return render(req,"buscar_AC.html")
  


# //////// RESULTADO DE LA BUSQUEDA///////
def resultadoCelular(req):
    return render (req, "resultado_CF.html")


def  resultadoAC(req):
    return render (req,'resultado_AC.html')




def carrito(req): 
    return render (req,"carrito.html")


def aboutus (req):
    
    return render (req, "aboutus.html")





class FundasList(ListView):
    model = Fundas
    template_name = "fundas_list.html"
    context_object_name = "fundaslist"
    


class FundasDetail(DetailView):
    model = Fundas
    template_name = "fundas_detail.html"
    context_object_name = "fundadetail"



    



class FundasCreate(CreateView):
    model = Fundas
    template_name = "fundas_create.html"
    fields = ("__all__")
    success_url = "/CelTech/fundas-lista/"
    
    

class FundasUpdate(UpdateView):
    model = Fundas
    template_name = "fundas_update.html"
    fields = ("__all__")
    success_url = "/CelTech/fundas-lista/"
    


class FundasDelete(DeleteView):
    model = Fundas
    template_name = "fundas_delete.html"
    success_url = "/CelTech/fundas-lista"

    
   

def contacto (req):
    if req.method == "POST":
        form = ConsultaFormulario(req.POST)
        if form.is_valid():
            asunto = "Consulta CelTech"
            mensaje = form.cleaned_data["mensaje"]
            correo = form.cleaned_data ["correo"]
            html = render_to_string("email.html" ,{"mensaje" : mensaje , "correo" : correo})
            from_email= "correo"
           
            send_mail(asunto, mensaje ,from_email , ["celtech.coderhouse@gmail.com"], html_message=html)
           
            return render ( req, "gracias.html")
    else: 
        form = ConsultaFormulario()

        return render (req,"contacto.html", {"form":form})


def gracias(req):
    return render(req,'gracias.html')

