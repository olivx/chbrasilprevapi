from os.path import splitext
from uuid import uuid4

from django.conf import settings
from django.db import models

# Create your models here.


def image_upload_to(instance, filename):
    _, filename_ext = splitext(filename)
    return f"produto/foto/{uuid4()}.{filename_ext}"


class Produto(models.Model):
    quantidade = models.PositiveIntegerField("Quantidade")
    produto = models.CharField("produto", max_length=255)
    descricao = models.TextField("Descrição", null=True, blank=True)
    foto = models.ImageField("Foto", null=True, blank=True, upload_to=image_upload_to)
    preco = models.DecimalField("Preço", decimal_places=2, default=0.00, max_digits=8)

    categoria = models.ForeignKey(
        "core.Categoria", on_delete=models.CASCADE, related_name="categorias"
    )

    def __str__(self):
        return self.produto

    class Meta:
        ordering = ("-id",)
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"


class Pedido(models.Model):
    class StatusChoices(models.IntegerChoices):
        STATUSS_NOVO = 0, "Novo"
        STATUS_PROCESSANDO = 1, "Processando"
        STATUS_APROVADO = 2, "Aprovado"

    data = models.DateTimeField(auto_now=True)
    sessao = models.CharField("Sessão", max_length=30)
    status = models.PositiveIntegerField(
        "Status", choices=StatusChoices.choices, default=StatusChoices.STATUSS_NOVO
    )

    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        pedido = f"id: {self.id} | cliente: {self.client} | status: {self.get_status_display()}"
        return pedido

    class Meta:
        ordering = ("-data",)
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"


class PedidoItem(models.Model):
    quantidade = models.PositiveIntegerField("Quantidade")
    nome = models.CharField("Produto", max_length=255)
    valor = models.DecimalField("Preço", decimal_places=2, default=0.00, max_digits=8)
    subtotal = models.DecimalField(
        "Sub total", decimal_places=2, default=0.00, max_digits=8
    )

    pedido = models.ForeignKey(
        "core.Pedido", on_delete=models.CASCADE, related_name="pedidos"
    )
    produto = models.ForeignKey(
        "core.Produto", on_delete=models.CASCADE, related_name="produtos"
    )

    def __str__(self):
        return f"produto: {self.produto.produto} qdt: {self.quantidade}"

    class Meta:
        ordering = ("-id",)
        verbose_name = "ProdutoItem"
        verbose_name_plural = "ProdutoItem"


class Categoria(models.Model):
    categoria = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.categoria

    class Meta:
        ordering = ("-id",)
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
