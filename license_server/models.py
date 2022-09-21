from django.db import models

# Create your models here.
class Tokes(models.Model):
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

class Device(models.Model):
    token = models.CharField(max_length=150)
    imei_code = models.CharField(max_length=250)
    notes = models.TextField(default="")

    def __str__(self):
        return f"id:{self.id} Ключ: {self.token} IMEI код: {self.imei_code} Примечания: {self.notes}"

    class Meta:
        verbose_name = "устройство"
        verbose_name_plural = 'устройства'