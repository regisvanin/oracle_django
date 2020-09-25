from django.db import models
from django.urls import reverse
from django.utils import timezone


class Nfce(models.Model):
    id = models.AutoField(primary_key=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    data_alteracao = models.DateTimeField(null=True)
    empresa = models.IntegerField(blank=False, null=False)
    pdv = models.IntegerField(blank=False, null=False)
    data_ocorrencia = models.DateField(blank=False)
    num_sat = models.CharField(max_length=30, blank=False)
    fabricante = models.CharField(max_length=200, blank=False)
    num_extrato = models.IntegerField(blank=False, null=False)
    num_ticket = models.IntegerField(blank=False, null=False)
    atendente = models.CharField(max_length=60, blank=False)

    class Meta:
        db_table = 'usr_t_nfce_inutilizada'
        managed = False

    def get_absolute_url(self):
        return reverse('list_nfce')

    def __str__(self):
        return str(self.id)
