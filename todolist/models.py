from django.db import models

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = (
        ('1','tO DO'),
        ('2', 'Completed'),
    )
    title = models.CharField(max_length=200)
    description = models.DateField(auto_now_add=True)
    state = models.CharField(max_length=1, choices=STATUS_CHOICES, default= '1')
    