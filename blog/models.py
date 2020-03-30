from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    Date = models.DateField()
