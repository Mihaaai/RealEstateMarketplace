from django import forms
from ..models import User


class ResetPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(), label="Password", required=True)
    retypePassword = forms.CharField(widget=forms.PasswordInput(), label="Retype Password", required=True)

    class Meta:
        model = User
