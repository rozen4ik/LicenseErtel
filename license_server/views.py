from django.shortcuts import render
from license_server.models import Tokes
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect


def index(request):
    tokens = Tokes.objects.all().order_by("-id")
    page_number = request.GET.get("page")
    page_m= Paginator(tokens, 10)
    page_m = page_m.get_page(page_number)

    data = {
        "tokens": tokens,
        "page_m": page_m
    }
    
    return render(request, "license_server/index.html", data)

def create(request):
    if request.method == "POST":
        new_token = Tokes()
        new_token.token = request.POST.get("token")
        new_token.start_date = request.POST.get("start_date")
        new_token.counterparty = request.POST.get("counterparty")
        new_token.end_date = request.POST.get("end_date")
        new_token.tech_support = request.POST.get("tech_support")
        new_token.number_of_activations = request.POST.get("number_of_activations")
        new_token.notes = request.POST.get("notes")
        new_token.save()
    return HttpResponseRedirect("/")
