from django.db import models

# Create your models here.

class Newuser(models.Model):
    Username = models.CharField(max_length=150)
    Fullname = models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    Mobile = models.CharField(max_length=12)
    Pwd = models.CharField(max_length=150)
    