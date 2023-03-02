from django.urls import path

from .views import detail_view

app_name = "item"

urlpatterns = [
    path("<int:pk>/", detail_view, name="detail")
]