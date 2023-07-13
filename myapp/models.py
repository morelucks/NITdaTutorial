from django.db import models

# Create your models here.
class Reservation(models.Model):
    name=models.CharField(max_length=100 , blank=True)
    contact=models.CharField('phone number', max_length=100)
    time=models.TimeField()
    count=models.IntegerField()
    note=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()

    def __str__(self):
        return self.first_name