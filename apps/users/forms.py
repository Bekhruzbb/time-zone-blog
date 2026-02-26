from django import forms
from apps.users.models import CustomUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username: '
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password: '
    }))

    class Meta:
        model = CustomUser


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username: '
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password1: '
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password2: '
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email: '
    }))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

