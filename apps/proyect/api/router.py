from rest_framework.routers import DefaultRouter
from apps.proyect.api.viewsets import ProyectViewSets

router = DefaultRouter()

router.register(r'ProyectViewSets',ProyectViewSets,basename='ProyectViewSets')
urlpatterns = router.urls