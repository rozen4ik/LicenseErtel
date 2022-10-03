from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path("api/drf-auth", include("rest_framework.urls")),
    path("api/tokens/<str:token_mobile>/", views.api_post_token),
]


urlpatterns = format_suffix_patterns(urlpatterns)