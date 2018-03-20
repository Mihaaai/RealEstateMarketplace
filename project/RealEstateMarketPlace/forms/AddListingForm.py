from django import forms
from django.db import transaction
from django.contrib.auth.models import User

from ..models import Estate, Listing

class AddListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = ['title', 'description', 'phone_number', 'user_id', ]

    user_id = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput)

    address = forms.CharField(widget=forms.Textarea, required=True)
    rooms = forms.IntegerField(required=True)
    floor = forms.IntegerField(required=True)
    size = forms.FloatField(required=True)
    year = forms.IntegerField(required=True)
    price = forms.FloatField(required=True)

    @transaction.atomic
    def save(self):
        estate = Estate(address=self.cleaned_data['address'],
                        rooms=self.cleaned_data['rooms'],
                        floor=self.cleaned_data['floor'],
                        size=self.cleaned_data['size'],
                        year=self.cleaned_data['year'],
                        price=self.cleaned_data['price'])
        estate.save()

        listing = super().save(commit=False)
        listing.estate_id = estate
        listing.save()

        return listing


