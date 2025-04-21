from rest_framework.routers import DefaultRouter
from apps.coordination.api.viewsets import CoordinationViewSets

router = DefaultRouter()

router.register(r'CoordinationViewSets',CoordinationViewSets,basename='CoordinationViewSets')
urlpatterns = router.urls