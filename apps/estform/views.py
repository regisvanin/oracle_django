from django.views.generic import ListView
from .models import EstoqueFormiguinha

class EstoqueList(ListView):
    model = EstoqueFormiguinha
    paginate_by = 15

    def get_queryset(self):
        depto = self.request.GET.get('depto', None)
        produto = self.request.GET.get('produto', None)
        descritivo = self.request.GET.get('descritivo', None)

        query = '''select p.id as sku,
                         p.descritivo as desc_produto,
                         0 as ean,
                         sum(pe.estoque_atual) as estoque_atual
                     from proreg.produtos p
                     left join proreg.produtos_ean e on p.id = e.produto and e.qtdee = 1
                     left join proreg.produtos_estoques pe on p.id = pe.produto
                     inner join proreg.estoques est on pe.estoque = est.id and est.troca = 'F'
                     inner join proreg.deptos d on p.depto = d.depto and p.secao = d.secao and p.grupo = d.grupo and p.subgrupo = d.subgrupo
                     where p.status in (0,1)
                     and p.depto = nvl(%s , p.depto)
                     and p.id = nvl(%s , p.id)
                     and p.descritivo like upper(%s)
                     group by p.id,
                                 p.descritivo
                        order by 4 desc
                     '''


        queryset = EstoqueFormiguinha.objects.raw(query, [depto, produto, descritivo])
        return queryset
