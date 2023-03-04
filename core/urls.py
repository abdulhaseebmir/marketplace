from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginFrom
from .views import (
    index_view, 
    contact_view,
    signup_view
)

app_name = "core"

urlpatterns = [
    path("", index_view, name="index"),
    path("contact/", contact_view, name="contact"),
    path("signup/", signup_view, name="signup"),
    path("login/", auth_views.LoginView.as_view(
        authentication_form=LoginFrom,
        template_name="core/login.html"
    ), name="login")
]