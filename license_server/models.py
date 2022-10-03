from django.db import models


# Create your models here.
class TokenErtel(models.Model):
    token = models.CharField(max_length=150)
    start_date = models.DateField()
    counterparty = models.TextField()
    end_date = models.DateField()
    tech_support = models.DateField()
    number_of_activated_devices = models.IntegerField(default=0)
    number_of_activations = models.IntegerField()
    notes = models.TextField(default="")

    def __str__(self):
        return f"id:{self.id} Ключ: {self.token} Дата выдачи: {self.start_date} Контрагент: {self.counterparty} Дата окончания: {self.end_date}"

    class Meta:
        verbose_name = "ключ"
        verbose_name_plural = 'ключи'
