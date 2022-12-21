from django.db import models


class Orders(models.Model):
    class State(models.TextChoices):
        TO_BUY = "1", "К покупке"
        BOUGHT = "2", "Купленно"
        SCHEDULED = "3", "Запланировано"
        ABADONED = "4", "Заброшено"

    state = models.CharField(
        max_length=2, choices=State.choices, default=State.SCHEDULED
    )

    name = models.CharField(max_length=500)
    url = models.URLField()
    price = models.FloatField()
    date_buy = models.DateField()
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Желаемое"
        verbose_name_plural = "Желаемое"
