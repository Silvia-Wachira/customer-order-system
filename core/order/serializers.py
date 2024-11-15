from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from core.abstract.serializers import AbstractSerializer
from core.order.models import Order
from core.user.models import User

class OrderSerializer(AbstractSerializer):
    customer = serializers.SlugRelatedField(
    queryset=User.objects.all(), slug_field='public_id')

    def validate_customer(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You can't create a order for another user.")
        return value
    
    class Meta:
        model = Order
        fields = ['id', 'customer', 'item', 'amount','created', 'updated']
        read_only_fields = ["edited"]