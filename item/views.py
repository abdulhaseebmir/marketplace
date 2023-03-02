from django.shortcuts import render, get_object_or_404
from core.models import Item

def detail_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {
        "item": item
    }
    return render(request, "item/detail.html", context)