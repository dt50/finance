from django.db import models


class Wallet(models.Model):
    class Currency(models.TextChoices):
        RU = "1", "Рубль"
        USD = "2", "Доллар"
        EUR = "3", "Евро"

    name = models.CharField(max_length=100)
    finance = models.ManyToManyField("Finance", blank=True)
    currency = models.CharField(
        max_length=2, choices=Currency.choices, default=Currency.RU
    )
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Кошелек"
        verbose_name_plural = "Кошельки"

    def __str__(self):
        return self.name


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

    def __str__(self):
        return f"{self.budget} {self.currency}"
