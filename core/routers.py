from rest_framework import routers
from core.user.viewsets import UserViewSet
from core.order.viewsets import OrderViewSet
from core.auth.viewsets.register import RegisterViewSet
from core.auth.viewsets.login import LoginViewSet
from core.auth.viewsets.refresh import RefreshViewSet

router = routers.SimpleRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'order', OrderViewSet, basename='order')
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')


urlpatterns = [
    *router.urls,
]