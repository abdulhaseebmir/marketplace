"""
Django should not serve static content, i.e. 
static or media files. Some other, like nginx, apache, etc. 
should serve static content in production environment.
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from core.views import index_view, contact_view

urlpatterns = [
    path("", index_view, name="index_view"),
    path("contact/", contact_view, name="contact_view"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
