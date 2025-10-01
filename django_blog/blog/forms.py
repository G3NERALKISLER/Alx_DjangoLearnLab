from django import forms
from django.contrib.auth.models import User
from .models import Profile

# Allow editing User basic info
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

# Allow editing Profile info
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']
