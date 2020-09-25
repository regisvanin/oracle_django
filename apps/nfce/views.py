from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Nfce

class NfceList(ListView):
    model = Nfce
    paginate_by = 10

    def get_queryset(self):
        queryset = Nfce.objects.all().order_by('data_cadastro')
        return queryset

class NfceCreate(CreateView):
    model = Nfce
    fields = ['data_cadastro', 'empresa', 'pdv', 'data_ocorrencia', 'num_sat', 'fabricante', 'num_extrato', 'num_ticket', 'atendente']

    def form_valid(self, form):
        obj = form.save()
        return super(NfceCreate, self).form_valid(form)

class NfceEdit(UpdateView):
    model = Nfce
    fields = ['id', 'data_cadastro', 'empresa', 'pdv', 'data_ocorrencia', 'num_sat', 'fabricante', 'num_extrato', 'num_ticket', 'atendente']

class NfceDelete(DeleteView):
    model = Nfce
    success_url = reverse_lazy('list_nfce')
