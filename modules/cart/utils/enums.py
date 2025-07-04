from django.db import models
from django.utils.translation import gettext_lazy as _


class CartStatus(models.TextChoices):
    CREATED = "CR", _("Created")
    ORDERED = "OR", _("Ordered")
