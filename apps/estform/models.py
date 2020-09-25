from django.db import models

class EstoqueFormiguinha(models.Model):
    sku = models.CharField(max_length=16, primary_key=True)
    desc_produto = models.TextField(max_length=260)
    ean = models.TextField(max_length=300)
    estoque_atual = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False

    def __str__(self):
        return str(self.sku)
