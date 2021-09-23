import socket

from .base import *

INTERNAL_IPS = [
    "127.0.0.1",
    socket.gethostbyname(socket.gethostname())[:-1] + "1",
]

# django-extensions:
# A collection of custom extensions for the Django Framework.
INSTALLED_APPS += [
    "django_extensions",
]
