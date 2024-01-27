from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.core.exceptions import ValidationError

from .models import User


class DoctorSignUpForm(
    UserCreationForm
):  # creating a custom form on top of the default UserCreationForm (to specify the user type as doctor)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            "username",
            "license_number",
            "phone_number",
            "age",
            "blood_group",
            "gender",
            "department",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.ispatient = False
        # user.license_number = super().save(commit=False)
        if commit:
            user.save()
        return user


class PatientSignupForm(UserCreationForm):  # creating a custom form on top of the default UserCreationForm (to specify the user type as patient)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "phone_number", "age", "blood_group", "gender",]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        if commit:
            user.save()
        return user
