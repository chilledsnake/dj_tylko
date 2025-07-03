from django.contrib.auth.models import User
from django.db import models

from modules.shelf.models import Shelf


class Cart(models.Model):
    CREATED = "CREATED"
    ORDERED = "ORDERED"
    STATUS = (
        (CREATED, "CREATED"),
        (ORDERED, "ORDERED"),
    )
    products = models.ManyToManyField(Shelf, related_name="carts")
    owner = models.ForeignKey(User, related_name="carts", on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, default=CREATED, max_length=7)
