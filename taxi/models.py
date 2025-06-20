from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.name} (country: {self.country})"

class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.model


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

