from rest_framework.routers import DefaultRouter
from apps.entry.api.viewsets import EntryViewSets

router = DefaultRouter()

router.register(r'EntryViewSets',EntryViewSets,basename='EntryViewSets')
urlpatterns = router.urls