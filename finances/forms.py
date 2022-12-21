from django import forms
from .models import Wallet, Finance


class FinanceForm(forms.ModelForm):
    class Meta:
        model = Finance
        fields = ["budget", "currency"]
