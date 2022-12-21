from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["user", "wallet"]
    autocomplete_fields = ["user", "wallet"]
