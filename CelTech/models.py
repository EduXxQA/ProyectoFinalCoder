from django.db import models

# Create your models here.


class Clientes(models.Model):
   
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    numero = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.numero} - {self.email}'
    
    


class Celulares(models.Model):
   
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    precio = models.IntegerField()
    
    def __str__(self):
        return f'{self.marca} - {self.modelo} - ${self.precio}'

class Accesorios(models.Model):
    
    marca = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    precio = models.IntegerField()
    
    def __str__(self):
        return f'{self.marca} - {self.tipo} - ${self.precio}'
    
    
class Fundas(models.Model):
    
    modelo = models.CharField(max_length=20)
    tipo =  models.CharField(max_length=20)
    precio = models.IntegerField()
    
    def __str__(self):
        return f'{self.modelo} - {self.tipo} - ${self.precio}'
    
    
# class Consulta(models.Model):
#     nombre = models.CharField(max_length=100)
#     correo = models.EmailField()
#     mensaje = models.TextField()
    
        
    

    

    
    
    