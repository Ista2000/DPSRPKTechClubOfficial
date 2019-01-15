from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'userclass', 'usersection', 'cchandle', 'cfhandle',
                  'phno', 'dept1', 'dept2']


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'userclass', 'usersection', 'cchandle', 'cfhandle',
                  'phno', 'dept1', 'dept2']
