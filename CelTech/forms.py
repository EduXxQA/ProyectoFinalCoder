from django import forms
from .models import *

class AdministradorCelulares(forms.Form):
    marca = forms.CharField(required=True)
    modelo = forms.CharField(required=True)
    precio = forms.IntegerField(required=True)
    
    
class AdministradorAccesorios(forms.Form):
    marca = forms.CharField(required=True)
    tipo = forms.CharField(required=True)
    precio = forms.IntegerField(required=True)
    
    
class AdministradorFundas(forms.Form):
    modelo = forms.CharField(required=True)
    tipo = forms.CharField(required=True)
    precio = forms.IntegerField(required=True)
    
    
# class consultaFormulario(forms.ModelForm):
#     class Meta:
#         model = Consulta
#         fields = ("__all__")
    
    