from django.db import models
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel

from apps.common.mixins import model_directory


class SiteConfiguration(SingletonModel):
    header_image = models.ImageField(
        upload_to=model_directory,
        verbose_name=_("header image"),
    )

    class Meta:
        verbose_name = _("Site Configuration")

    def __str__(self):
        return str(_("Site Configuration"))
