from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("snippets/", views.snippet_list, name="list"),
    path("snippets/<int:pk>/", views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
