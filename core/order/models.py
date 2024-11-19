from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from core.abstract.models import AbstractModel,AbstractManager
from django.http import Http404

# Create your models here.

#   Represents an order placed by a customer,
class OrderManager(AbstractManager):
    pass

class Order(models.Model):

    customer = models.ForeignKey(to="core_user.User",on_delete=models.CASCADE)
    item = models.CharField(max_length=255,help_text='Name/Description of the ordered item')
    amount = models.IntegerField(validators=[MinValueValidator(1)],help_text='Order amount')
    created = models.DateTimeField(auto_now_add=True,help_text='Timestamp when the order was created')
    updated = models.DateTimeField(auto_now=True,help_text='Timestamp when the order was last updated')

    objects = OrderManager()
    def __str__(self):
        return f"{self.customer.name}"
    class Meta:
        db_table = "core.order"