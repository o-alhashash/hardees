from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
        'description',
    ]
    ordering = [
        'name',
    ]
    list_display = [
        'id',
        'name',
        'description',
        'price',
    ]
