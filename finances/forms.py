from django import forms

from .models import Finance


class FinanceForm(forms.ModelForm):
    class Meta:
        model = Finance
        fields = ["name", "budget", "currency", "type"]
