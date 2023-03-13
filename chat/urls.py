from django.urls import path

from .views import new_chat_view, inbox_view, detail_view

app_name = "chat"

urlpatterns = [
    path("", inbox_view, name="inbox"),
    path("<int:pk>/", detail_view, name="detail"),
    path("new/<int:item_pk>/", new_chat_view, name="new")
]