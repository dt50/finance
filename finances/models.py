from django.db import models


class Wallet(models.Model):
    class Currency(models.TextChoices):
        RU = "1", "Рубль"
        USD = "2", "Доллар"
        EUR = "3", "Евро"

    name = models.CharField(max_length=100)
    finance = models.ForeignKey("Finance", on_delete=models.RESTRICT)
    currency = models.CharField(
        max_length=2, choices=Currency.choices, default=Currency.RU
    )
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Кошелек"
        verbose_name_plural = "Кошельки"


class Finance(models.Model):
    class Currency(models.TextChoices):
        RU = "1", "Рубль"
        USD = "2", "Доллар"
        EUR = "3", "Евро"

    budget = models.FloatField()
    currency = models.CharField(
        max_length=2, choices=Currency.choices, default=Currency.RU
    )
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Финансы"
        verbose_name_plural = "Финансы"
