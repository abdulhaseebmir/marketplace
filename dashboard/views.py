from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from core.models import Item

@login_required
def index_view(request):
    items = Item.objects.filter(created_by=request.user)
    context = {
        "items": items
    }

    return render(request, "dashboard/index.html", context)