from .models import Author
from django.forms import ModelForm
from django import forms

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['username', 'password', 'email']

class LoginForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ("username", "password")