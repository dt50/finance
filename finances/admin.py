from django.contrib import admin
from .models import Finance, Wallet, TypeFinance


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    search_fields = ["name"]

    class Meta:
        verbose_name = "Кошелек"


@admin.register(Finance)
class FinanceAdmin(admin.ModelAdmin):
    list_display = ["budget", "currency"]


@admin.register(TypeFinance)
class TypeFinanceAdmin(admin.ModelAdmin):
    list_display = ["name"]
