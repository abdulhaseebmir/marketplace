from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import ChatMessageForm
from core.models import Item
from .models import Chat

@login_required
def new_chat_view(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect("dashboard:index")

    chats = Chat.objects.filter(item=item).filter(members__in=[request.user.id])

    if chats:
        return redirect("chat:detail", pk=chats.first().id)

    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat = Chat.objects.create(item=item)
            chat.members.add(request.user)
            chat.members.add(item.created_by)
            chat.save()

            chat_message = form.save(commit=False)
            chat_message.chat = chat
            chat_message.created_by = request.user
            chat_message.save()

            return redirect("item:detail", pk=item_pk)
    
    else:
        form = ChatMessageForm()

    context = {
        "form": form
    }
    
    return render(request, "chat/new.html", context)


@login_required
def inbox_view(request):
    chats = Chat.objects.filter(members__in=[request.user.id])
    context = {
        "chats": chats
    }

    return render(request, "chat/inbox.html", context)


@login_required
def detail_view(request, pk):
    chat = Chat.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == "POST":
        form = ChatMessageForm(request.POST)

        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.chat = chat
            chat_message.created_by = request.user
            chat_message.save()

            chat.save()

            return redirect("chat:detail", pk=pk)
    
    else:
        form = ChatMessageForm()

    context = {
        "chat": chat,
        "form": form
    }
    return render(request, "chat/detail.html", context)