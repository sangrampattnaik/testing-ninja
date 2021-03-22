from django.db import models
from .admin import admin


# Create your models here.


class Employee(models.Model):
    eno = models.PositiveIntegerField()
    ename = models.CharField(max_length=100)
    esal = models.FloatField()
    eadd = models.CharField(max_length=100)


@admin.register(Employee)
class Em(admin.ModelAdmin):
    list_display = [
        "eno",
        "ename",
        "esal",
        "eadd",
    ]