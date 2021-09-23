import django_heroku

from .base import *  # noqa

django_heroku.settings(locals())
