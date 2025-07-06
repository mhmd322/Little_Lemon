
# Create your models here.
from django.db import models

class Booking(models.Model):
    id = models.AutoField(primary_key=True)   # معرف تلقائي كـ مفتاح أساسي
    name = models.CharField(max_length=100)
    no_of_guests = models.PositiveIntegerField()
    booking_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.booking_date}"


class Menu(models.Model):
    id = models.AutoField(primary_key=True)   # معرف تلقائي كـ مفتاح أساسي
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.title
