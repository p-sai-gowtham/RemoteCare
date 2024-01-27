from django.shortcuts import render
from .models import Appointment


def patientDashboard(request):

    appointments= Appointment.objects.get(ongoing=True)
    return render(request, "doctor/patient dash.html", {'appi' : appointments})