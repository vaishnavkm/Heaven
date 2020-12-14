from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'bio', 'avatar')

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password1','password2']