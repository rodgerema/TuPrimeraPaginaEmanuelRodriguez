from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Categoria, Compras
from django.views.generic import CreateView
from .forms import *
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your views here.
def index(request):
    compras = Compras.objects.all()

    return render(request, "compras/index.html", {"compras": compras})

class ComprasCreate(CreateView):
    model = models.Compras
    form_class = ComprasForm
    success_url = reverse_lazy("compras:index")

def buscar(request):
    resultados = []

    if request.method == 'POST':
        form = BuscarPorCategoria(request.POST)
        if form.is_valid():
            categoria = form.cleaned_data['categoria']
            try:
                categoria = Categoria.objects.get(categoria=categoria)
                resultados = Compras.objects.filter(categoria_id=categoria)
            except Compras.DoesNotExist:
                resultados = []
    
    else:
        form = BuscarPorCategoria()

    return render(request, 'compras/buscar.html', {'form': form, 'resultados': resultados})
