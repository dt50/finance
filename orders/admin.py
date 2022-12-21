from django.contrib import admin
from .models import Orders, Wishlist


@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "price", "url"]
    ordering = ["name"]


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "price", "url"]
    ordering = ["name"]
