from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .serializers import ProjectSerializer
from ...models import Project


class ProjectViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
