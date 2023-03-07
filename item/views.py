from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm
from core.models import Item

def detail_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    
    context = {
        "related_items": related_items,
        "item": item
    }
    return render(request, "item/detail.html", context)

@login_required
def new_view(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES) # file to be uploaded
        if form.is_valid():
            item = form.save(commit=False) # don't commit changes to db. Just create object
            item.created_by = request.user # need to add created_by before adding to db
            item.save() # commit to db
            return redirect("item:detail", pk=item.id)
    else:
        form = NewItemForm()
    context = {
        "form": form,
        "title": "New item"
    }
    return render(request, "item/form.html", context)