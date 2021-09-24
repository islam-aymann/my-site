from django.urls import include, path

from apps.portfolio.views import index, RedirectionView

app_name = "portfolio"

urlpatterns = [
    path("", index, name="index"),
    path("<str:destination>", RedirectionView.as_view(), name="redirection"),
    path("api/v1/", include("apps.portfolio.api.v1.urls", namespace="api_v1")),
]
