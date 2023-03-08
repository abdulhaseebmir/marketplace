from django.urls import path

from .views import (
    detail_view, new_view, delete_view, edit_view
)

app_name = "item"

urlpatterns = [
    path("new/", new_view, name="new"),
    path("<int:pk>/", detail_view, name="detail"),
    path("<int:pk>/delete/", delete_view, name="delete"),
    path("<int:pk>/edit/", edit_view, name="edit"),
]