import pytest
from apps.core.models import URL
from django.test import Client
from django.urls import reverse
from rest_framework import status


def test_redirection(client: Client):
    path = reverse("por")
    response = client.get(path)

    assert response.status_code == status.HTTP_301_MOVED_PERMANENTLY
