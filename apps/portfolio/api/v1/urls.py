from rest_framework.routers import DefaultRouter

from .viewsets import ProjectViewSet

app_name = "v1"

router = DefaultRouter()

router.register("projects", ProjectViewSet, basename="project")
urlpatterns = router.urls
