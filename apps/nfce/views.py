from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from .models import Nfce

class NfceList(ListView):
    model = Nfce
    paginate_by = 5

    def get_queryset(self):
        queryset = Nfce.objects.all()
        return queryset

class NfceCreate(CreateView):
    model = Nfce
    fields = ['data_cadastro', 'empresa', 'pdv', 'data_ocorrencia', 'num_sat', 'fabricante', 'num_extrato', 'num_ticket', 'atendente']

    def form_valid(self, form):
        obj = form.save()
        return super(NfceCreate, self).form_valid(form)