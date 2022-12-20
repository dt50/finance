from django.db import models
from django.contrib.auth.models import User
from finances.models import Wallet


class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, on_delete=models.RESTRICT)
