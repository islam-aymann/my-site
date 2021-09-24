from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .open_api import urlpatterns as openapi_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls", namespace="core")),
    path("", include("apps.portfolio.urls", namespace="portfolio")),
]

urlpatterns += openapi_urlpatterns

if settings.DEBUG and settings.DEBUG_TOOLBAR:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    try:
        import debug_toolbar

        urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
    except ImportError:
        pass
