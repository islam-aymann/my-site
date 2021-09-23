from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.mixins import (
    TitleSlugRichBodyModelMixin,
    ImageModelMixin,
    TimeStampedModelMixin,
    AvatarModelMixin,
    NameModelMixin,
    model_directory,
)


class Project(
    TimeStampedModelMixin,
    TitleSlugRichBodyModelMixin,
    ImageModelMixin,
):
    summary = RichTextField(
        blank=True,
        null=True,
        verbose_name=_("summary"),
    )

    start_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=_("start date"),
    )

    end_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=_("end date"),
    )

    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")
        ordering = [
            "-start_date",
            "-end_date",
            "id",
        ]

    def __str__(self):
        return f"Project: #{self.pk}"


class SocialLink(
    TimeStampedModelMixin,
):
    title = models.CharField(
        max_length=128,
        verbose_name=_("title"),
    )

    icon = models.ImageField(
        upload_to=model_directory,
        verbose_name=_("icon"),
    )

    url = models.URLField(
        verbose_name=_("url"),
    )

    class Meta:
        ordering = [
            "title",
            "url",
        ]


class Author(
    TimeStampedModelMixin,
    AvatarModelMixin,
    NameModelMixin,
):
    title = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name=_("title"),
    )

    class Meta:
        verbose_name = _("author")
        verbose_name_plural = _("authors")
        ordering = [
            "name",
            "title",
        ]

    def __str__(self):
        return f"Author: #{self.pk}"


class Testimonial(
    TimeStampedModelMixin,
    TitleSlugRichBodyModelMixin,
):
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name=_("author"),
    )

    class Meta:
        verbose_name = _("testimonial")
        verbose_name_plural = _("testimonials")
        ordering = [
            "author",
            "title",
        ]

    def __str__(self):
        return f"Testimonial: #{self.pk}"
