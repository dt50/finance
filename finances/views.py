from django.shortcuts import render
from users.models import CustomUser
from django.contrib.auth.decorators import login_required
from finances.models import Finance, Wallet


@login_required(login_url="/users/sign/")
def index(request):
    photo = CustomUser.objects.get(user=request.user)
    return render(
        request,
        "finances/index.html",
        {"url_photo": photo.avatar.url},
    )
