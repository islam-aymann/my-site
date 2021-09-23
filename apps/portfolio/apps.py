from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PortfolioConfig(AppConfig):
    default_auto_field = "django.db.models.AutoField"
    name = "apps.portfolio"
    verbose_name = _("portfolio app")
