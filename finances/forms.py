from django import forms

from .models import Finance, Wallet


class FinanceForm(forms.ModelForm):
    class Meta:
        model = Finance
        fields = ["budget", "currency"]
