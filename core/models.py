from os.path import splitext
from uuid import uuid4

from django.conf import settings
from django.db import models

# Create your models here.


def image_upload_to(instance, filename):
    _, filename_ext = splitext(filename)
    return f"produto/foto/{instance.pk}/{uuid4()}.{filename_ext}"


class Produto(models.Model):
    quantidade = models.IntegerField("Quantidade")
    produto = models.CharField("produto", max_length=255)
    desricao = models.TextField("Descrição", null=True, blank=True)
    foto = models.ImageField("Foto", null=True, blank=True, upload_to=image_upload_to)
    preco = models.DecimalField("Preço", decimal_places=2, default=0.00, max_digits=8)

    categoria = models.ForeignKey("core.Categoria", on_delete=models.CASCADE)

    def __str__(self):
        return self.produto

    class Meta:
        ordering = ("-id",)
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"


class Pedido(models.Model):
    STATUSS_NOVO = 0
    STATUS_PROCESSANDO = 1
    STATUS_APROVADO = 2

    STATUS_CHOICES = (
        (STATUSS_NOVO, "Novo"),
        (STATUS_PROCESSANDO, "Processando"),
        (STATUS_APROVADO, "Aprovado"),
    )

    data = models.DateTimeField(auto_now=True)
    status = models.IntegerField("Status", default=STATUSS_NOVO)
    sessao = models.CharField("Sessão", max_length=30)

    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.categoria

    class Meta:
        ordering = ("-data",)
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"


class PedidoItem(models.Model):
    quantidade = models.IntegerField("Quantidade")
    produto = models.CharField("Status", max_length=255)
    valor = models.DecimalField("Preço", decimal_places=2, default=0.00, max_digits=8)
    subtotal = models.DecimalField("Preço", decimal_places=2, default=0.00, max_digits=8)

    pedido = models.ForeignKey("core.Pedido", on_delete=models.CASCADE)
    produto = models.ForeignKey("core.Produto", on_delete=models.CASCADE)

    def __str__(self):
        return self.produto

    class Meta:
        ordering = ("-id",)
        verbose_name = "ProdutoItem"
        verbose_name_plural = "ProdutoItem"


class Categoria(models.Model):
    categoria = models.CharField(max_length=200)

    def __str__(self):
        return self.categoria

    class Meta:
        ordering = ("-id",)
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
