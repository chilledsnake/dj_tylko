from django.db import models
from django.utils.translation import gettext_lazy as _


class RegionsChoices(models.TextChoices):
    UK = "UK", _("United Kingdom")
    DE = "DE", _("Germany")
    FR = "FR", _("France")
    PL = "PL", _("Poland")
    NL = "NL", _("Netherlands")
