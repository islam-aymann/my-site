from django.contrib import admin

from .models import Project, SocialLink, Author, Testimonial


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "title",
        "start_date",
        "end_date",
    ]


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "title",
        "url",
    ]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "name",
        "title",
    ]


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "title",
        "author",
    ]

    list_select_related = [
        "author",
    ]
