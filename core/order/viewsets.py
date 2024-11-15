from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from core.abstract.viewsets import AbstractViewSet
from core.order.models import Order
from core.order.serializers import OrderSerializer
# Create your views here.

class OrderViewSet(AbstractViewSet):
    http_method_names = ('post', 'get')
    permission_classes = (AllowAny,)
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()
    
    def get_object(self):
        obj = Order.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)