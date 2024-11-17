import pytest
from core.order.models import Order
from core.fixtures.user import user
# Create your tests here.

@pytest.mark.django_db
def test_create_order(user):
    order = Order.objects.create(customer=user,item='phone', amount=1000000) 
    assert order.customer == user
    assert order.item == 'phone'
    assert order.amount == 1000000
