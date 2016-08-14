from django.shortcuts import render

from registration.backends.default.views import RegistrationView

from .forms import RegisterForm


# Create your views here.
class RegisterView(RegistrationView):
    form_class = RegisterForm
