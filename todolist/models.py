from django.db import models
from datetime import date

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = (
        ('1','tO DO'),
        ('2', 'Completed'),
    )
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    registry_date = models.DateField(default=date.today)
    state = models.CharField(max_length=1, choices=STATUS_CHOICES, default= '1')
