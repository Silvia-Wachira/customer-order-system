from rest_framework import routers
from core.user.viewsets import UserViewSet
from core.order.viewsets import OrderViewSet

router = routers.SimpleRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'order', OrderViewSet, basename='order')


urlpatterns = [
    *router.urls,
]