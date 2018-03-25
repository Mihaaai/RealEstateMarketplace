from django import forms
from django.db import transaction

from ..models import Estate, Listing, User, CITY_CHOISES


class AddListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = ['title', 'description', 'user_id', ]

    user_id = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput)

    city = forms.ChoiceField(choices=CITY_CHOISES, required=True)
    image = forms.ImageField(required=False)
    rooms = forms.IntegerField(required=True, min_value=0, max_value=10)
    bathrooms = forms.IntegerField(required=True, min_value=0, max_value=5)
    floor = forms.IntegerField(required=True, min_value=0, max_value=20)
    size = forms.FloatField(required=True, min_value=10, max_value=200)
    year = forms.IntegerField(required=True, min_value=1900, max_value=2018)
    price = forms.FloatField(required=True, min_value=0)

    @transaction.atomic
    def save(self):
        estate = Estate(city=self.cleaned_data['city'],
                        rooms=self.cleaned_data['rooms'],
                        floor=self.cleaned_data['floor'],
                        size=self.cleaned_data['size'],
                        year=self.cleaned_data['year'],
                        price=self.cleaned_data['price'],
                        image=self.cleaned_data['image'],
                        bathrooms=self.cleaned_data['bathrooms'],
                        )
        estate.save()

        listing = super().save(commit=False)
        listing.estate_id = estate
        listing.save()

        return listing
