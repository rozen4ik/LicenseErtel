from django.contrib import admin
from .models import *


@admin.register(TokenErtel)
class TokesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "token",
        "start_date",
        "counterparty",
        "end_date",
        "tech_support",
        "number_of_activated_devices",
        "number_of_activations",
        "notes",
    )
    list_display_links = (
        "id",
        "token",
        "start_date",
        "counterparty",
        "end_date",
        "tech_support",
        "number_of_activated_devices",
        "number_of_activations",
        "notes",
    )