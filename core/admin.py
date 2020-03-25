from django.contrib import admin

from .models import Pedido

# Register your models here.


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("client", "sessao", "get_status")
    list_filter = ("status",)

    def get_status(self, obj):
        return obj.get_status_display()

    get_status.short_description = "Status"
