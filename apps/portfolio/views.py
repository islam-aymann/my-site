from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View


def index(request):
    return render(request, "portfolio/under-maintenance.html", {})


class RedirectionView(View):
    def get(self, request: HttpRequest, destination: str):
        mapper = {
            "linkedin": "https://www.linkedin.com/in/islam-ayman-176495106/",
            "github": "https://github.com/islamusayman95",
            "twitter": "https://twitter.com/islam_ayman95",
            "instagram": "https://www.instagram.com/islamusayman95/",
            "whatsapp": "https://wa.me/+201003346334",
        }

        return redirect(
            mapper.get(destination, "/"),
            permanent=True,
        )
