from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from . import forms, models

class ClienteList(ListView):
    model = models.Cliente

    def get_queryset(self):
        if self.request.GET.get("buscar"):
            consulta = self.request.GET.get("buscar")
            object_list = models.Cliente.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Cliente.objects.all()
        return object_list


class ClienteCreate(CreateView):
    model = models.Cliente
    form_class = forms.ClienteForm
    success_url = reverse_lazy("cliente:index")


class ClienteDetail(DetailView):
    model = models.Cliente


class ClienteUpdate(UpdateView):
    model = models.Cliente
    form_class = forms.ClienteForm
    success_url = reverse_lazy("cliente:index")


class ClienteDelete(DeleteView):
    model = models.Cliente
    success_url = reverse_lazy("cliente:index")


