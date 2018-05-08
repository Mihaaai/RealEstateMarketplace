from django import forms
from ..models import User
# from django.contrib.auth.forms import UserChangeForm

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email', 'first_name', 'last_name', 'phone_number',
        )

    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
