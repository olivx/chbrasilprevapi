import django_filters
from django_filters import rest_framework as filters

from .models import Pedido, PedidoItem, Produto


class ProdutofilterSet(filters.FilterSet):
    produto = django_filters.CharFilter(field_name="produto", lookup_expr="icontains")
    categoria = django_filters.CharFilter(
        field_name="categoria", lookup_expr="categoria__iexact"
    )
    quantidade__gte = django_filters.NumberFilter(
        field_name="quantidade", lookup_expr="gte"
    )
    quantidade__lte = django_filters.NumberFilter(
        field_name="quantidade", lookup_expr="lte"
    )
    preco__gte = django_filters.NumberFilter(field_name="preco", lookup_expr="gte")
    preco__lte = django_filters.NumberFilter(field_name="preco", lookup_expr="lte")

    class Meta:
        model = Produto
        fields = [
            "produto",
            "categoria",
            "preco__gte",
            "preco__lte",
            "quantidade__gte",
            "quantidade__gte",
        ]


class PedidofilterSet(filters.FilterSet):
    sessao = django_filters.CharFilter(field_name="sessao", lookup_expr="contains")
    client_nome = django_filters.CharFilter(
        field_name="client", lookup_expr="nome__icontains"
    )
    client_pk = django_filters.NumberFilter(
        field_name="client__pk", lookup_expr="exact"
    )

    class Meta:
        model = Pedido
        fields = ["sessao", "client_nome", "client_pk"]


class PedidoItemfilterSet(filters.FilterSet):
    pedido = django_filters.CharFilter(field_name="pedido_pk", lookup_expr="exact")
    quantidade__gte = django_filters.NumberFilter(
        field_name="quantidade", lookup_expr="gte"
    )
    quantidade__lte = django_filters.NumberFilter(
        field_name="quantidade", lookup_expr="lte"
    )
    produto = django_filters.CharFilter(field_name="nome", lookup_expr="icontains")
    categoria = django_filters.CharFilter(
        field_name="produto", lookup_expr="categoria__categoria__icontains"
    )

    class Meta:
        model = PedidoItem
        fields = [
            "pedido",
            "produto",
            "categoria",
            "quantidade__gte",
            "quantidade__lte",
        ]
