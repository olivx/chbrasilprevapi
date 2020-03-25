import pytest
from django.contrib.auth import get_user_model
from model_mommy import mommy

from ..models import Categoria, Pedido, PedidoItem, Produto


@pytest.mark.django_db
def test_pytest_categoria():
    model = mommy.make(Categoria, categoria="categoria")
    assert str(model) == "categoria"


@pytest.mark.django_db
def test_pytest_produto():
    model = mommy.make(Produto, produto="produto")
    assert str(model) == "produto"


@pytest.mark.django_db
def test_pytest_pedido():
    client = mommy.make(get_user_model(), nome="thiago")
    model = mommy.make(Pedido, sessao="sessao", client=client, status=0)
    assert str(model) == "id: 1 | cliente: thiago | status: Novo"


@pytest.mark.django_db
def test_pytest_pedido_item():
    produto = mommy.make(Produto, produto="produto")
    model = mommy.make(PedidoItem, produto=produto, quantidade=10)
    assert str(model) == "produto: produto qdt: 10"
