from django.db import models

from modules.cart.models import Cart


class Order(models.Model):
    UK = "UK"
    DE = "DE"
    FR = "FR"
    PL = "PL"
    NL = "NL"

    REGIONS = (
        (UK, "United Kingdom"),
        (DE, "Germany"),
        (FR, "France"),
        (PL, "Poland"),
        (NL, "Netherlands"),
    )

    carts = models.ForeignKey(Cart, related_name="orders", on_delete=models.CASCADE)
    region = models.CharField(choices=REGIONS, max_length=2)
    order_date = models.DateTimeField(auto_now_add=True)
