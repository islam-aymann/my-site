from .base import *  # noqa

DEBUG = False

# django-storages:
# django-storages is a collection of custom storage backends for Django.
INSTALLED_APPS += [
    "storages",
]

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

AWS_DEFAULT_ACL = None
AWS_S3_FILE_OVERWRITE = False

AWS_ACCESS_KEY_ID = os.environ.get(
    "AWS_ACCESS_KEY_ID",
    "AWS_ACCESS_KEY_ID",
)
AWS_SECRET_ACCESS_KEY = os.environ.get(
    "AWS_SECRET_ACCESS_KEY",
    "AWS_SECRET_ACCESS_KEY",
)

AWS_STORAGE_BUCKET_NAME = os.environ.get(
    "AWS_STORAGE_BUCKET_NAME",
    "AWS_STORAGE_BUCKET_NAME",
)
