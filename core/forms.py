from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginFrom(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Your username",
        "class": "w-full py-2 px-3 rounded-lg"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Your password",
        "class": "w-full py-2 px-3 rounded-lg"
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Your username",
        "class": "w-full py-2 px-3 rounded-lg"
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        "placeholder": "Your email address",
        "class": "w-full py-2 px-3 rounded-lg"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Your password",
        "class": "w-full py-2 px-3 rounded-lg"
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Repeat password",
        "class": "w-full py-2 px-3 rounded-lg"
    }))