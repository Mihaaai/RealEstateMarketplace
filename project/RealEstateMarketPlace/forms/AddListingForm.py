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
    image = forms.ImageField(required=False)
    rooms = forms.IntegerField(required=True, min_value=0, max_value=10)
    floor = forms.IntegerField(required=True, min_value=0, max_value=20)
    size = forms.FloatField(required=True, min_value=10, max_value=200)
    year = forms.IntegerField(required=True, min_value=1900, max_value=2018)
    price = forms.FloatField(required=True, min_value=0)


    @transaction.atomic
    def save(self):
        estate = Estate(address=self.cleaned_data['address'],
                        rooms=self.cleaned_data['rooms'],
                        floor=self.cleaned_data['floor'],
                        size=self.cleaned_data['size'],
                        year=self.cleaned_data['year'],
                        price=self.cleaned_data['price'],
                        image=self.cleaned_data['image'],
                        )
        estate.save()

        listing = super().save(commit=False)
        listing.estate_id = estate
        listing.save()

        return listing


