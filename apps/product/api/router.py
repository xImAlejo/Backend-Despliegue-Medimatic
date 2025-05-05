from rest_framework.routers import DefaultRouter
from apps.product.api.viewsets import ProductViewSets

router = DefaultRouter()

router.register(r'ProductViewSets',ProductViewSets,basename='ProductViewSets')
urlpatterns = router.urls