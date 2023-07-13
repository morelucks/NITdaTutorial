from django.contrib import admin
from .models import Reservation
from .models import Employee
# Register your models here.
admin.site.register(Reservation)
admin.site.register(Employee)