from django.shortcuts import render
from .models import Item, Category

# Create your views here.

def index_view(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    context = {
        "items": items,
        "categories": categories
    }
    return render(request, "core/index.html", context)

def contact_view(request):
    return render(request, "core/contact.html")