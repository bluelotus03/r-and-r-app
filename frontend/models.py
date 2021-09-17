from django.db import models

# Create your models here.
class Users(models.Model):
    fname = models.CharField(max_length=60)
    lname = models.CharField(max_length=60)
    email = models.CharField(max_length=100, unique=True)
