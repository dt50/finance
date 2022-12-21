from django.contrib.auth.models import User
from django.db import models

from finances.models import Wallet


class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, on_delete=models.RESTRICT)
    avatar = models.ImageField(upload_to="avatar/", null=True, blank=True)

    class Meta:
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.wallet.name}"
