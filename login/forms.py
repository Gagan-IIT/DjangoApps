from django import forms

from .models import Login

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length = 120)
    password = forms.CharField(max_length = 32, widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = [
            'username',
            'password',
        ]

class AddLoginForm(forms.ModelForm):
    username = forms.CharField(max_length = 120)
    password = forms.CharField(max_length = 32, widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = [
            'username',
            'password',
        ]

