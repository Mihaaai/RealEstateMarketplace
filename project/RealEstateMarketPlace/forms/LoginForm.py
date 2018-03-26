from django import forms
from ..models import User


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(), label="Email", required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput(), required=True)

    class Meta:
        model = User
        fields = (
            'email', 'password',
        )
