from django.db import models

# Create your models here.
from .admin import admin

class Student(models.Model):
    sname = models.CharField(max_length=100)
    sroll = models.PositiveIntegerField()
    smarks = models.FloatField()

@admin.register(Student)
class sdjv(admin.ModelAdmin):
    list_display = [
        'sname',
        'sroll',
        'smarks',
    ]