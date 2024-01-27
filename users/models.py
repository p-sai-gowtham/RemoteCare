from email.policy import default
from turtle import back
from django.db import models
from django.contrib.auth.models import AbstractUser

BLOOD_GROUPS = (
    ("A+", "A+"),
    ("A-", "A-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
    ("O+", "O+"),
    ("O-", "O-"),
)


class User(AbstractUser):
    ispatient = models.BooleanField(default=True)
    license_number = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=15, null=True, blank=True)
    department = models.CharField(max_length=30, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    blood_group = models.CharField(max_length=15,choices=BLOOD_GROUPS,default='A+', null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)