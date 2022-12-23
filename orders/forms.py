from django import forms

from .models import Orders, Wishlist


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ["state", "name", "url", "price", "currency", "date_buy"]


class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ["state", "name", "url", "price", "currency"]
