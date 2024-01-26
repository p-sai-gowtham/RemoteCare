from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ispatient = models.BooleanField(default=True)
    license_number = models.CharField(max_length=50)
    gender = models.CharField(max_length=15)
    department = models.CharField(max_length=30)
    age = models.ImageField()