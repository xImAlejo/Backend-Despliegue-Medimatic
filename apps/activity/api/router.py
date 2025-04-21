from rest_framework.routers import DefaultRouter
from apps.activity.api.viewsets import ActivityViewSets

router = DefaultRouter()

router.register(r'ActivityViewSets',ActivityViewSets,basename='ActivityViewSets')
urlpatterns = router.urls