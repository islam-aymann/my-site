from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from solo.admin import SingletonModelAdmin

from .models import SiteConfiguration

admin.site.site_header = _("Islam Ayman Site Administration")
admin.site.site_title = _("Islam Ayman Site Administration")


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(SingletonModelAdmin):
    pass
