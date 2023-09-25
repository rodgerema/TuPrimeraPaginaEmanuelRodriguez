from django import forms

from . import models

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = ["nombre", "apellido", "nacimiento", "pais_origen_id"]

class PaisForm(forms.ModelForm):
    class Meta:
        model = models.Pais
        fields = ["nombre"]

class BuscarPorPais(forms.Form):
    nombre_pais = forms.CharField(label='Nombre del país', max_length=100)


class EliminarCliente(forms.Form):
    cliente_id = forms.IntegerField(label='ID Cliente')