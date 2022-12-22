from django.db import models


class Orders(models.Model):
    class State(models.TextChoices):
        TO_BUY = "1", "К покупке"
        BOUGHT = "2", "Куплено"
        SCHEDULED = "3", "Запланировано"
        ABADONED = "4", "Заброшено"

    class Currency(models.TextChoices):
        RU = "1", "Рубль"
        USD = "2", "Доллар"
        EUR = "3", "Евро"

    state = models.CharField(
        max_length=2, choices=State.choices, default=State.SCHEDULED
    )

    name = models.CharField(max_length=500)
    url = models.URLField()
    price = models.FloatField()
    currency = models.CharField(
        max_length=2, choices=Currency.choices, default=Currency.RU
    )
    date_buy = models.DateField()
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Товары"
        verbose_name_plural = "Товар"

    def __str__(self):
        return f"{self.name} {self.price}"


class Wishlist(models.Model):
    class State(models.TextChoices):
        PLAN = "1", "В планых"
        ABADONED = "2", "Заброшено"

    class Currency(models.TextChoices):
        RU = "1", "Рубль"
        USD = "2", "Доллар"
        EUR = "3", "Евро"

    state = models.CharField(max_length=2, choices=State.choices, default=State.PLAN)

    name = models.CharField(max_length=500)
    url = models.URLField()
    price = models.FloatField()
    currency = models.CharField(
        max_length=2, choices=Currency.choices, default=Currency.RU
    )
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Желаемое"
        verbose_name_plural = "Желаемое"

    def __str__(self):
        return f"{self.name} {self.price}"
