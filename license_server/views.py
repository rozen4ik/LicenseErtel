from django.shortcuts import render
from license_server.models import TokenErtel
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponseNotFound

from service import Service

service = Service()


def index(request):
    tokens = TokenErtel.objects.all().order_by("-id")
    page_number = request.GET.get("page")
    page_m = Paginator(tokens, 10)
    page_m = page_m.get_page(page_number)

    data = {
        "tokens": tokens,
        "page_m": page_m
    }

    return render(request, "license_server/index.html", data)


def create(request):
    if request.method == "POST":
        service.create_token(request)
    return HttpResponseRedirect("/")
