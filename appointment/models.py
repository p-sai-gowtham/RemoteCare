from django.db import models
from users.models import User


class Appointment(models.Model):
    problem = models.TextField()
    scan = models.ImageField(upload_to="scans")
    time = models.CharField(max_length=10, null=True, blank=True)
    ongoing = models.BooleanField(default=True)
    patient = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="patient", null=True, blank=True
    )
    doctor = models.OneToOneField(
        User, on_delete=models.SET_NULL, related_name="doctor", null=True, blank=True
    )
