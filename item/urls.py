from django.urls import path

from .views import detail_view, new_view

app_name = "item"

urlpatterns = [
    path("new/", new_view, name="new"),
    path("<int:pk>/", detail_view, name="detail")
]