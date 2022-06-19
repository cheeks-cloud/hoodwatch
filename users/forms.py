from django.contrib.auth.forms import UserCreationForm, user
from django.contrib.auth.models import User
from django import forms

from users.models import *
from .forms import *


class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name'
        ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'hood'
        ]