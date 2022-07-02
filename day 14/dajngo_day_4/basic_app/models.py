from django.db import models
from basic_app.models import UserProfileInfo
from django import forms 
# Create your models here.

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfo(forms.ModelForm):
    class Meta():
        model = UserProfileInfo