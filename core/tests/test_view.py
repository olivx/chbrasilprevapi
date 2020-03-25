import pytest
from django.urls import reverse
from model_mommy import mommy

from ..models import Categoria, Pedido, PedidoItem, Produto


@pytest.mark.django_db
def test_list_categorias(api_client, token):
    mommy.make(Categoria, _quantity=10)
    resp = api_client.get(
        reverse("categoria-list"), HTTP_AUTHORIZATION=f"Token {token}"
    )

    assert resp.status_code == 200
    assert len(resp.json()) == 10


# view Categoria
@pytest.mark.django_db
def test_get_categoria_by_id(api_client, django_request, token):
    categoria = mommy.make(Categoria)
    resp = api_client.get(
        reverse("categoria-detail", args=([categoria.id])),
        HTTP_AUTHORIZATION=f"Token {token}",
    )

    assert resp.status_code == 200
    assert (
        django_request.build_absolute_uri(
            reverse("categoria-detail", args=([categoria.id]))
        )
        == resp.json()["url"]
    )


@pytest.mark.django_db
def test_create_categoria(api_client, token):
    categoria = mommy.prepare(Categoria)
    data = dict(categoria=categoria.categoria)
    resp = api_client.post(
        reverse("categoria-list"),
        HTTP_AUTHORIZATION=f"Token {token}",
        data=data,
        format="json",
    )

    assert resp.status_code == 201
    assert Categoria.objects.get(categoria=data["categoria"])


# view Produto
@pytest.mark.django_db
def test_list_produto(api_client, token):
    mommy.make(Produto, _quantity=10)
    resp = api_client.get(reverse("produto-list"), HTTP_AUTHORIZATION=f"Token {token}")

    assert resp.status_code == 200
    assert len(resp.json()) == 10


@pytest.mark.django_db
def test_get_produto_by_id(api_client, django_request, token):
    produto = mommy.make(Produto)
    resp = api_client.get(
        reverse("produto-detail", args=([produto.id])),
        HTTP_AUTHORIZATION=f"Token {token}",
    )

    assert resp.status_code == 200
    assert (
        django_request.build_absolute_uri(
            reverse("produto-detail", args=([produto.id]))
        )
        == resp.json()["url"]
    )


@pytest.mark.django_db
def test_create_produto(api_client, token):
    categoria = Categoria.objects.create(**{"categoria": "categoria"})
    produto = mommy.prepare(Produto, _save_related=True)
    data = dict()
    for field in produto._meta.fields:
        data[field.name] = getattr(produto, field.name)
    data.pop("foto")

    data["categoria"] = reverse("categoria-detail", args=([categoria.id]))
    resp = api_client.post(
        reverse("produto-list"),
        HTTP_AUTHORIZATION=f"Token {token}",
        data=data,
        format="json",
    )

    assert resp.status_code == 201
    assert Produto.objects.get(produto=data["produto"])


# view pedidodo
@pytest.mark.django_db
def test_list_pedido(api_client, token):
    mommy.make(Pedido, _quantity=10)
    resp = api_client.get(reverse("pedido-list"), HTTP_AUTHORIZATION=f"Token {token}")

    assert resp.status_code == 200
    assert len(resp.json()) == 10


@pytest.mark.django_db
def test_get_pedido_by_id(api_client, django_request, token):
    pedido = mommy.make(Pedido)
    resp = api_client.get(
        reverse("pedido-detail", args=([pedido.id])),
        HTTP_AUTHORIZATION=f"Token {token}",
    )

    assert resp.status_code == 200
    assert (
        django_request.build_absolute_uri(reverse("pedido-detail", args=([pedido.id])))
        == resp.json()["url"]
    )


@pytest.mark.django_db
def test_create_pedido(api_client, token):
    pedido = mommy.prepare(Pedido, _save_related=True)
    data = dict()
    for field in pedido._meta.fields:
        data[field.name] = getattr(pedido, field.name)

    data["client"] = reverse("user-me", args=([pedido.client.id]))
    resp = api_client.post(
        reverse("pedido-list"),
        HTTP_AUTHORIZATION=f"Token {token}",
        data=data,
        format="json",
    )

    assert resp.status_code == 201
    assert Pedido.objects.get(sessao=data["sessao"])


@pytest.mark.django_db
def test_patch_pedido(api_client, token):
    data = dict()
    pedido = mommy.make(Pedido)
    for field in pedido._meta.fields:
        data[field.name] = getattr(pedido, field.name)

    data["client"] = reverse("user-me", args=([pedido.client.id]))
    resp = api_client.patch(
        reverse("pedido-detail", args=([pedido.id])),
        HTTP_AUTHORIZATION=f"Token {token}",
        data=data,
    )

    assert resp.status_code == 400
    assert resp.json() == {"detail": "Cannot patch [client] field"}


# view Pedido Item
@pytest.mark.django_db
def test_list_pedido_item(api_client, token):
    mommy.make(PedidoItem, _quantity=10)
    resp = api_client.get(
        reverse("pedidoitem-list"), HTTP_AUTHORIZATION=f"Token {token}"
    )

    assert resp.status_code == 200
    assert len(resp.json()) == 10


@pytest.mark.django_db
def test_get_pedido_item_by_id(api_client, django_request, token):
    pedidoitem = mommy.make(PedidoItem)
    resp = api_client.get(
        reverse("pedidoitem-detail", args=([pedidoitem.id])),
        HTTP_AUTHORIZATION=f"Token {token}",
    )

    assert resp.status_code == 200
    assert (
        django_request.build_absolute_uri(
            reverse("pedidoitem-detail", args=([pedidoitem.id]))
        )
        == resp.json()["url"]
    )


@pytest.mark.django_db
def test_create_pedido_item(api_client, token):
    pedidoitem = mommy.prepare(PedidoItem, _save_related=True)
    data = dict()
    for field in pedidoitem._meta.fields:
        data[field.name] = getattr(pedidoitem, field.name)

    data["produto"] = reverse("produto-detail", args=([pedidoitem.produto.pk]))
    data["pedido"] = reverse("pedido-detail", args=([pedidoitem.pedido.pk]))
    resp = api_client.post(
        reverse("pedidoitem-list"),
        HTTP_AUTHORIZATION=f"Token {token}",
        data=data,
        format="json",
    )

    assert resp.status_code == 201
    assert PedidoItem.objects.get(produto=pedidoitem.produto)


@pytest.mark.django_db
def test_patch_pedido_item(api_client, token):
    data = dict()
    pedidoitem = mommy.make(PedidoItem)
    for field in pedidoitem._meta.fields:
        data[field.name] = getattr(pedidoitem, field.name)

    data["produto"] = reverse("produto-detail", args=([pedidoitem.produto.pk]))
    data["pedido"] = reverse("pedido-detail", args=([pedidoitem.pedido.id]))
    resp = api_client.patch(
        reverse("pedidoitem-detail", args=([pedidoitem.id])),
        HTTP_AUTHORIZATION=f"Token {token}",
        data=data,
    )

    assert resp.status_code == 400
    assert resp.json() == {"detail": "Cannot patch [pedido] field"}
