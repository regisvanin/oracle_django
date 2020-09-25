import django_filters
from .models import EstoqueFormiguinha


class EstoqueFormiguinhaFilter(django_filters.FilterSet):
    desc_produto = django_filters.CharFilter(lookup_expr='icontains')
    sku = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = EstoqueFormiguinha
        fields = ['estoque_atual']