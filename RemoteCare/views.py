from django.http import HttpResponseRedirect
from django.shortcuts import render
from appointment.forms import UploadForm
from django.views import View
from appointment.models import Appointment


class UploadView(View):
    def get(self, request):
        form = UploadForm()
        return render(request, "home/index.html", {"form": form})

    def post(self, request):
        submited_data = UploadForm(request.POST, request.FILES)
        if submited_data.is_valid():
            upload = Appointment(scan=request.FILES["scans"])
            upload.save()
            return HttpResponseRedirect("/")
