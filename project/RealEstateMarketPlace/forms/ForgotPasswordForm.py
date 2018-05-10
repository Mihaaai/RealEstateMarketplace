from django import forms
from ..models import User


class ForgotPasswordForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(), label="Email", required=True)

    class Meta:
        model = User
        fields = (
            'email',
        )
