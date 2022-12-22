from django import forms

from .models import Orders


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ["state", "name", "url", "price", "currency", "date_buy"]
