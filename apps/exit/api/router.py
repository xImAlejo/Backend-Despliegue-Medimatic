from rest_framework.routers import DefaultRouter
from apps.exit.api.viewsets import ExitViewSets

router = DefaultRouter()

router.register(r'ExitViewSets',ExitViewSets,basename='ExitViewSets')
urlpatterns = router.urls