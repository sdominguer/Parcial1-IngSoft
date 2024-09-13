from django.db import models

# Create your models here.

from django.db import models

class Flight(models.Model):
    FLIGHT_TYPE_CHOICES = [
        ('Nacional', 'Nacional'),
        ('Internacional', 'Internacional'),
    ]

    name = models.CharField(max_length=100)
    flight_type = models.CharField(max_length=20, choices=FLIGHT_TYPE_CHOICES)
    price = models.IntegerField()

    def __str__(self):
        return self.name
