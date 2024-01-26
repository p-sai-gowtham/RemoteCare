from django.db import models

from RemoteCare import department


class Appointment(models.Model):
    problem = models.TextField()
    scan = models.ImageField(upload_to="scans")
    time = models.DateTimeField()
    ongoing = models.BooleanField()