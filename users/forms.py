from django_select2.forms import ModelSelect2Widget
from django import forms
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text="First Name")
    last_name = forms.CharField(max_length=100, help_text="Last Name")
    email = forms.EmailField(max_length=150, help_text="Email")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )
