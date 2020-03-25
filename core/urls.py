from rest_framework.routers import DefaultRouter

from .views import CategoraiViewSet, PedidoItemViewSet, PedidoViewSet, ProdutoiViewSet

router = DefaultRouter(trailing_slash=False)

router.register(r"pedido", PedidoViewSet, basename=PedidoViewSet.name)
router.register(r"produto", ProdutoiViewSet, basename=ProdutoiViewSet.name)
router.register(r"categoria", CategoraiViewSet, basename=CategoraiViewSet.name)
router.register(r"pedidoitem", PedidoItemViewSet, basename=PedidoItemViewSet.name)

urlpatterns = router.urls
