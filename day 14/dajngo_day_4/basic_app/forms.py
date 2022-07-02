from dataclasses import fields
from django import forms
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProFileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProFileInfo
        fields = ('protfolio_site', 'profiles_pic')

