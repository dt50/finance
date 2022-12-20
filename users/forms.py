from django_select2.forms import ModelSelect2Widget
from django.forms import forms
from .models import CustomUser
from django.contrib.auth.models import User
from finances.models import Wallet


class ProcessForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        exclude = ("id",)

        widgets = {
            "user": ModelSelect2Widget(
                model=User,
                queryset=User.objects.filter(),
                search_fields=["username__icontains"],
                attrs={"style": "width: 100%;"},
            ),
            "wallet": ModelSelect2Widget(
                model=Wallet,
                queryset=Wallet.objects.filter(),
                search_fields=["name__icontains"],
                attrs={"style": "width: 100%;"},
            ),
        }
