from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Business,Profile,NeighborHood

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','profile']