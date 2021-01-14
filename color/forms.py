from django import forms
from .models import Banner, User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator
from django.forms import ModelForm

class RegisterUser(ModelForm):
    class Meta:
        model = User
        fields = ('phone_number','username','email','first_name',)
