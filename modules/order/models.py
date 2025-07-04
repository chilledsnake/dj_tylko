from django.db import models

from modules.cart.models import Cart
from modules.order.utils.enums import RegionsChoices


class Order(models.Model):
    carts = models.ForeignKey(Cart, related_name="orders", on_delete=models.CASCADE)
    region = models.CharField(choices=RegionsChoices, max_length=2)
    order_date = models.DateTimeField(auto_now_add=True)
