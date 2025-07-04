from django.db import models

from modules.cart.utils.enums import CartStatus
from modules.shelf.models import Shelf
from modules.user.models import User


class Cart(models.Model):
    products = models.ManyToManyField(Shelf, related_name="carts")
    owner = models.ForeignKey(User, related_name="carts", on_delete=models.CASCADE)
    status = models.CharField(
        choices=CartStatus, default=CartStatus.CREATED, max_length=7
    )
