from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile
class Userregisterform(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
     

     class Meta:
        model=User
        fields=['username','email']

class UpdateProfile(forms.ModelForm):
   
    class Meta:
        model=profile
        fields=['image']



