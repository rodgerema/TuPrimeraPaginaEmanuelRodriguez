from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic import DetailView, CreateView

from . import models, forms
from .models import Stock, Ubicacion
from .forms import *

# Create your views here.
def index(request):
    stock = Stock.objects.all()

    return render(request, "stock/index.html", {"stock": stock})

# def crear(request):
#     if request.method == "POST":
#         form = StockForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("stock:index")
#     else:
#         form = StockForm()
#     return render(request, "stock/crear.html", {"form": form})


class StockCreate(CreateView):
    model = models.Stock
    form_class = StockForm
    success_url = reverse_lazy("stock:index")

def buscar(request):
    resultados = []

    if request.method == 'POST':
        form = BuscarPorUbicacion(request.POST)
        if form.is_valid():
            ubicacion = form.cleaned_data['ubicacion']
            try:
                ubicacion = Ubicacion.objects.get(ubicacion=ubicacion)
                resultados = Stock.objects.filter(ubicacion_id=ubicacion)
            except Stock.DoesNotExist:
                resultados = []
    
    else:
        form = BuscarPorUbicacion()

    return render(request, 'stock/buscar.html', {'form': form, 'resultados': resultados})

class StockUpdate(UpdateView):
    model = models.Stock
    form_class = StockForm
    success_url = reverse_lazy("stock:index")


class StockDelete(DeleteView):
    model = models.Stock
    success_url = reverse_lazy("stock:index")

class StockDetail(DetailView):
    model = models.Stock