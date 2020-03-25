from rest_framework import permissions, viewsets

from .exception import CannotPatchApiException
from .filters import PedidofilterSet, PedidoItemfilterSet, ProdutofilterSet
from .models import Categoria, Pedido, PedidoItem, Produto

# Create your views here.
from .serializers import (
    CategoriaSerialzier,
    PedidoItemSerialzier,
    PedidoSerialzier,
    ProdutoSerialzier,
)


class CategoraiViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerialzier
    queryset = Categoria.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get", "post", "head", "options", "patch", "delete"]
    name = "categoria"


class ProdutoiViewSet(viewsets.ModelViewSet):
    serializer_class = ProdutoSerialzier
    queryset = Produto.objects.select_related("categoria").all()
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = ProdutofilterSet
    http_method_names = ["get", "post", "head", "options", "patch", "delete"]
    name = "produto"


class PedidoViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoSerialzier
    queryset = Pedido.objects.select_related("client").all()
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = PedidofilterSet
    http_method_names = ["get", "post", "head", "options", "patch", "delete"]
    name = "pedido"

    def partial_update(self, request, pk=None):
        if request.data.get("client"):
            raise CannotPatchApiException("Cannot patch [client] field")
        return super().partial_update(request, pk)


class PedidoItemViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoItemSerialzier
    queryset = PedidoItem.objects.select_related("produto", "pedido").all()
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get", "post", "head", "options", "patch", "delete"]
    filterset_class = PedidoItemfilterSet
    name = "pedidoitem"

    def partial_update(self, request, pk=None):
        if request.data.get("pedido"):
            raise CannotPatchApiException("Cannot patch [pedido] field")
        return super().partial_update(request, pk)
