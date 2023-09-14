from django.db import models

# Create your models here.


class Clientes(models.Model):
   
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    numero = models.IntegerField()
    email = models.EmailField()


class Celulares(models.Model):
   
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    precio = models.IntegerField()
    

class Accesorios(models.Model):
    
    marca = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    precio = models.IntegerField()
    
    
class Fundas(models.Model):
    
    modelo = models.CharField(max_length=20)
    tipo =  models.CharField(max_length=20)
    precio = models. IntegerField()
    

    

    
    
    