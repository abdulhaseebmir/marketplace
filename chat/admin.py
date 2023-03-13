from django.contrib import admin

from .models import Chat, ChatMessage

class ChatAdmin(admin.ModelAdmin):
    list_display = ["item", "created_at", "modified_at"]
    search_fields = ["created_at", "modified_at"]

class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ["chat", "content", "created_by", "created_at"]
    search_fields = ["content", "created_at"]


admin.site.register(Chat, ChatAdmin)
admin.site.register(ChatMessage, ChatMessageAdmin)
