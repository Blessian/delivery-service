from rest_framework import routers
from .views import DeliveryLogViewSet

router = routers.SimpleRouter()
router.register(r'logs', DeliveryLogViewSet, basename='logs')

urlpatterns = router.urls
