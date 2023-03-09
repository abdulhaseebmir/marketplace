from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from .forms import NewItemForm, EditItemForm
from core.models import Item, Category

def items_view(request):
    items = Item.objects.filter(is_sold=False)
    query = request.GET.get("query", "") # Default is empty/""
    categories = Category.objects.all()
    category_id = request.GET.get("category", 0)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        "items": items,
        "query": query,
        "categories": categories,
        "category_id": int(category_id)
    }
    return render(request, "item/items.html", context=context)

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

@login_required
def edit_view(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item) # file to be uploaded
        if form.is_valid():
            form.save()
            return redirect("item:detail", pk=item.id)
    else:
        form = EditItemForm(instance=item) # so the form isn't empty
    context = {
        "form": form,
        "title": "Edit item"
    }
    return render(request, "item/form.html", context)

@login_required
def delete_view(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect("dashboard:index")