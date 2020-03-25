import pytest
from django.contrib.auth import get_user_model
from model_mommy import mommy

from ..models import Categoria, Pedido, PedidoItem, Produto
from ..serializers import (
    CategoriaSerialzier,
    PedidoItemSerialzier,
    PedidoSerialzier,
    ProdutoSerialzier,
)


@pytest.mark.django_db
def test_deserialize_categoria(django_request):
    _test_deserilazer(
        Categoria, CategoriaSerialzier, django_request, fields=["categoria"]
    )


@pytest.mark.django_db
def test_deserialize_produto(django_request):
    _test_deserilazer(
        Produto,
        ProdutoSerialzier,
        django_request,
        fields=["produto", "quantidade", "preco", "foto", "descricao"],
    )


@pytest.mark.django_db
def test_deserialize_pedido(django_request):
    _test_deserilazer(
        Pedido, PedidoSerialzier, django_request, fields=["data", "sessao", "status"]
    )


@pytest.mark.django_db
def test_deserialize_pedido_item(django_request):
    _test_deserilazer(
        PedidoItem,
        PedidoItemSerialzier,
        django_request,
        fields=["quantidade", "produto", "valor", "subtotal"],
    )


@pytest.mark.django_db
def test_pedido_item_validate_true(django_request,):
    get_user_model().objects.create(
        **{"email": "email@email.com", "password": "password"}
    )
    Categoria.objects.create(**{"categoria": "Pet shop"})

    Pedido.objects.create(
        **{
            "data": "2020-03-23T03:43:25.401539Z",
            "client_id": 1,
            "sessao": "adasdasd",
            "status": 0,
        }
    )

    Produto.objects.create(
        **{
            "categoria_id": 1,
            "quantidade": 10,
            "produto": "test de produto",
            "descricao": "teste de produto descrição",
            "preco": 10.00,
        }
    )

    data = {
        "quantidade": "10",
        "valor": "10.00",
        "pedido": "http://127.0.0.1:8000/api/v1/pedido/1",
        "produto": "http://127.0.0.1:8000/api/v1/produto/1",
    }

    serializer = PedidoItemSerialzier(data=data, context={"request": django_request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    assert serializer.data.get("subtotal") == "100.00"


@pytest.mark.django_db
def test_pedido_item_validate_false(django_request,):
    get_user_model().objects.create(
        **{"email": "email@email.com", "password": "password"}
    )
    Categoria.objects.create(**{"categoria": "Pet shop"})

    Pedido.objects.create(
        **{
            "data": "2020-03-23T03:43:25.401539Z",
            "client_id": 1,
            "sessao": "adasdasd",
            "status": 0,
        }
    )

    Produto.objects.create(
        **{
            "categoria_id": 1,
            "quantidade": 10,
            "produto": "test de produto",
            "descricao": "teste de produto descrição",
            "preco": 10.00,
        }
    )

    data = {
        "quantidade": "10",
        "pedido": "http://127.0.0.1:8000/api/v1/pedido/1",
        "produto": "http://127.0.0.1:8000/api/v1/produto/1",
    }

    serializer = PedidoItemSerialzier(data=data, context={"request": django_request})
    with pytest.raises(Exception) as execinfo:
        serializer.is_valid(raise_exception=True)
    error_message = "não é possivel fazer as operação"
    error_message + "de sub valor, quatidade: 10 valor None"
    assert error_message in str(execinfo.value.args[0])


def _test_deserilazer(model, klass_serialzier, django_request, fields=[]):
    model = mommy.make(model)
    serializer = klass_serialzier(model, context={"request": django_request})
    for field_name in fields:
        assert model._meta.get_field(field_name).name in serializer.data.keys()
