from django.urls import include, path

app_name = "portfolio"

urlpatterns = [
    path("api/v1/", include("apps.portfolio.api.v1.urls", namespace="api_v1")),
]
