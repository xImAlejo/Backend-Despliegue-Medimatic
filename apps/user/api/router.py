from rest_framework.routers import DefaultRouter
from apps.user.api.viewsets import UserViewSets
from apps.user.api.viewsets import SetPassword

router = DefaultRouter()

router.register(r'UserViewSets',UserViewSets,basename='UserViewSets')
router.register(r'SetPassword',SetPassword,basename='SetPassword')
urlpatterns = router.urls