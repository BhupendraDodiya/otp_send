from django.db import models

# Create your models here.
class reg(models.Model):
    Name = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)