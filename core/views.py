from django.shortcuts import render, redirect
from .models import Item, Category
from .forms import SignupForm

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

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            
            return redirect("login/")
    else:
        form = SignupForm()

    context = {
        "form": form
    }

    return render(request, "core/signup.html", context)