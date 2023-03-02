from django.contrib import admin

from .models import Category, Item

class CategoryAdmin(admin.ModelAdmin):
    # list_display = ["id", "name"]
    list_display = ["id", "name"]
    search_fields = ["id", "name"]

class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "is_sold", "price", "created_at"]
    search_fields = ["id", "name"] 

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
