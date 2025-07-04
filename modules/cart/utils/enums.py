from django.db import models
from django.utils.translation import gettext_lazy as _


class CartStatus(models.TextChoices):
    CREATED = "CREATED", _("Created")
    ORDERED = "ORDERED", _("Ordered")
