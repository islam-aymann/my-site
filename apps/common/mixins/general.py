from ckeditor.fields import RichTextField
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


def model_directory(instance, filename):
    now = timezone.now()
    return (
        f"my-site/{instance.__class__.__name__.lower()}/"
        f"{now.year}/{now.month}/{filename}"
    )


class TitleSlugModelMixin(models.Model):
    title = models.CharField(
        max_length=512,
        verbose_name=_("title"),
    )

    slug = models.SlugField(
        allow_unicode=True,
        unique=True,
        auto_created=True,
        editable=False,
        verbose_name=_("slug"),
        max_length=1024,
    )

    class Meta:
        abstract = True


class TitleSlugDescriptionModelMixin(TitleSlugModelMixin):
    description = models.TextField(_("description"), blank=True, null=True)

    class Meta:
        abstract = True


class TitleSlugRichDescriptionModelMixin(TitleSlugModelMixin):
    description = RichTextField(blank=True, null=True, verbose_name=_("description"))

    class Meta:
        abstract = True


class TitleSlugBodyModelMixin(TitleSlugModelMixin):
    body = models.TextField(blank=True, null=True, verbose_name=_("body"))

    class Meta:
        abstract = True


class TitleSlugRichBodyModelMixin(TitleSlugModelMixin):
    body = RichTextField(blank=True, null=True, verbose_name=_("body"))

    class Meta:
        abstract = True


class NameModelMixin(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("name"))

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class IsActiveModelMixin(models.Model):
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("is active"),
    )

    class Meta:
        abstract = True


class IconModelMixin(models.Model):
    icon = models.ImageField(
        upload_to=model_directory,
        blank=True,
        null=True,
        verbose_name=_("icon"),
    )

    class Meta:
        abstract = True

    @property
    def icon_url(self):
        try:
            return self.icon.url
        except (TypeError, ValueError, AttributeError):
            return str()


class ImageModelMixin(models.Model):
    image = models.ImageField(
        upload_to=model_directory,
        blank=True,
        null=True,
        verbose_name=_("image"),
    )

    class Meta:
        abstract = True

    @property
    def image_url(self):
        try:
            return self.image.url
        except (TypeError, ValueError, AttributeError):
            return str()


class AvatarModelMixin(models.Model):
    avatar = models.ImageField(
        upload_to=model_directory,
        blank=True,
        null=True,
        verbose_name=_("avatar"),
    )

    class Meta:
        abstract = True

    @property
    def avatar_url(self):
        try:
            return self.avatar.url
        except (TypeError, ValueError, AttributeError):
            return str()


class TimeStampedModelMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("created"))
    modified = models.DateTimeField(auto_now=True, verbose_name=_("modified"))

    class Meta:
        abstract = True


@receiver(pre_save)
def populate_slug_from_title(sender, instance, **kwargs):
    if hasattr(instance, "title") and hasattr(instance, "slug"):
        slug = slugify(instance.title, allow_unicode=True)

        count = 0
        new_slug = slug
        while sender.objects.filter(slug=new_slug):
            count += 1
            new_slug = f"{slug}-{count}"
        instance.slug = new_slug
