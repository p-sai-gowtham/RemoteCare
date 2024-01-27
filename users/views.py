from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .forms import PatientSignupForm, DoctorSignUpForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


class PatientSignUpView(CreateView):  # class based view to register user as patient.
    model = User
    form_class = PatientSignupForm
    template_name = "signup.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "patient"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("/")


class DoctorSignUpView(CreateView):  # class based view to register user as doctor.
    model = User
    form_class = DoctorSignUpForm
    template_name = "signup.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "doctor"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("/")


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You've logged in successfully!")
            if user.ispatient:
                return redirect("/")
            else:
                return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request, "signup.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.success(request, "You've logged out successfully!")
    return redirect("/")
