from django import forms
from stock.models import Stock
from . import models

class ComprasForm(forms.ModelForm):
    
    articulo = forms.ModelChoiceField(queryset=Stock.objects.all(), label="Articulo",  widget=forms.Select(attrs={'class': 'form'}))

    widgets = {
        "articulo": forms.Select(attrs={'class': 'form-control'}),
        "precio": forms.NumberInput(attrs={'class': 'form-control'}),
        "cantidad": forms.NumberInput(attrs={'class': 'form-control'}),
        "categoria_id": forms.Select(attrs={'class': 'form-control'}),
    }

    class Meta:
        model = models.Compras
        fields = "__all__"


class BuscarPorCategoria(forms.Form):
    categoria = forms.ModelChoiceField(queryset=models.Categoria.objects.all(),label='Buscar por categoria', widget=forms.Select(attrs={'class': 'form'}))

