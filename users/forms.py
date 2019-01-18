from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'middle_name', 'last_name', 'userclass', 'usersection', 'cchandle',
                  'cfhandle', 'kagglehandle', 'phno', 'dept1', 'dept2', 'profilepic']


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'middle_name', 'last_name', 'userclass', 'usersection', 'cchandle',
                  'cfhandle', 'kagglehandle', 'phno', 'dept1', 'dept2', 'profilepic']
