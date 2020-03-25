from rest_framework import serializers

from .models import Categoria, Pedido, PedidoItem, Produto


class CategoriaSerialzier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class ProdutoSerialzier(serializers.HyperlinkedModelSerializer):
    categorias = CategoriaSerialzier(read_only=True)

    class Meta:
        model = Produto
        fields = "__all__"


class PedidoSerialzier(serializers.HyperlinkedModelSerializer):

    client = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Pedido
        fields = "__all__"


class PedidoItemSerialzier(serializers.HyperlinkedModelSerializer):

    produtos = ProdutoSerialzier(read_only=True)
    pedidos = PedidoSerialzier(read_only=True)

    class Meta:
        model = PedidoItem
        fields = "__all__"

    def validate(self, data):
        quantidade = data.get("quantidade")
        valor = data.get("valor")
        if valor is None or quantidade is None:
            raise serializers.ValidationError(
                f"não é possivel fazer as operação de sub valor, quatidade: {quantidade} valor {valor}"
            )
        data["subtotal"] = quantidade * valor
        return data
