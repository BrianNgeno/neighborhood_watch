from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Business,Profile,NeighborHood

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','profile','neighborHood']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','neighborhood','business']

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = NeighborHood
        exclude= ['user']