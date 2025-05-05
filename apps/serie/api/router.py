from rest_framework.routers import DefaultRouter
from apps.serie.api.viewsets import SerieViewSets

router = DefaultRouter()

router.register(r'SerieViewSets',SerieViewSets,basename='SerieViewSets')
urlpatterns = router.urls