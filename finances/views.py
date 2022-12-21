from django.shortcuts import render
from users.models import CustomUser


def index(requests):
    photo = CustomUser.objects.get(user=requests.user)
    return render(requests, "finances/index.html", {"url_photo": photo.avatar.url})
