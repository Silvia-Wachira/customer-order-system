from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from core.abstract.viewsets import AbstractViewSet
from core.order.models import Order
from core.order.serializers import OrderSerializer
# import africastalking

# Create your views here.

import africastalking

# TODO: Initialize Africa's Talking


username = 'sandbox'
api_key = 'atsk_bc46b6b18d2da6a2942684d9938187305a066d14ca1d634aa52407f5937a14d771c56732'
africastalking.initialize(username, api_key)

sms = africastalking.SMS

class send_sms():
        
        #TODO: Send message
        
    def sending(self):
            # Set the numbers in international format
            recipients = ["+254705361989"]
            # Set your message
            message = "Hey Client!";
            # Set your shortCode or senderId
            sender = "45788"
            try:
                response = sms.send(message, recipients, sender)
                print (response)
            except Exception as e:
                print (f'Houston, we have a problem: {e}')



class OrderViewSet(AbstractViewSet):
    http_method_names = ('post', 'get')
    permission_classes = (IsAuthenticated,)
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
        send_sms().sending()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
