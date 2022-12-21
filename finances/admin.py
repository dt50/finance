from django.contrib import admin
from .models import Finance, Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    search_fields = ["name"]

    class Meta:
        verbose_name = "Кошелек"


@admin.register(Finance)
class FinanceAdmin(admin.ModelAdmin):
    list_display = ["budget", "currency"]
