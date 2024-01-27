from django import forms


class UploadForm(forms.Form):
    scans = forms.ImageField()
    problem = forms.CharField(max_length=500)
