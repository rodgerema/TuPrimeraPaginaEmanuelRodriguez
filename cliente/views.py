from django.shortcuts import render, redirect
from django.http import HttpResponse

#from . import models, forms
from .models import Cliente, Pais
from .forms import *


def index(request):
    clientes = Cliente.objects.all()

    return render(request, "cliente/index.html", {"clientes": clientes})

def crear(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:index")
    else:
        form = ClienteForm()
    return render(request, "cliente/crear.html", {"form": form})


def agregar_pais(request):
    if request.method == "POST":
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:index")
    else:
        form = PaisForm()
    return render(request, "cliente/agregar_pais.html", {"form": form})


def buscar(request):
    resultados = []

    if request.method == 'POST':
        form = BuscarPorPais(request.POST)
        if form.is_valid():
            nombre_pais = form.cleaned_data['nombre_pais']
            try:
                pais = Pais.objects.get(nombre=nombre_pais)
                resultados = Cliente.objects.filter(pais_origen_id=pais)
            except Pais.DoesNotExist:
                resultados = []
    
    else:
        form = BuscarPorPais()

    return render(request, 'cliente/buscar.html', {'form': form, 'resultados': resultados})



def eliminar_cliente(request):
    if request.method == "POST":
        form = EliminarCliente(request.POST)
        if form.is_valid():
            cliente_id = form.cleaned_data['cliente_id']
            try:
                cliente = Cliente.objects.get(pk=cliente_id)
                cliente.delete()
                return redirect("cliente:index")
            except Cliente.DoesNotExist:
                #return HttpResponse("ID de cliente invalido")
                form.add_error('cliente_id', 'ID de cliente inválido. Vuelve a intentarlo.')
    else:
        form = EliminarCliente()
    return render(request, "cliente/eliminar_cliente.html", {"form": form}) 
        


