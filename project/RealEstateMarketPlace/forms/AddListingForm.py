from django import forms
from django.db import transaction
from ..models import Estate, Listing, User, NEIGHBORHOOD_CHOICES, PARTITIONING_CHOICES


class AddListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = (
            'title', 'description',
        )

    address = forms.CharField(max_length=100, required=False)
    image = forms.ImageField(required=False)
    partitioning = forms.ChoiceField(choices=PARTITIONING_CHOICES, required=True)
    neighborhood = forms.ChoiceField(choices=NEIGHBORHOOD_CHOICES, required=True)
    rooms = forms.IntegerField(required=True, min_value=1, max_value=10)
    bathrooms = forms.IntegerField(required=True, min_value=0, max_value=5)
    floor = forms.IntegerField(required=True, min_value=0, max_value=20)
    size = forms.FloatField(required=True, min_value=10, max_value=200)
    year = forms.IntegerField(required=True, min_value=1900, max_value=2018)
    price = forms.FloatField(required=True, min_value=0)

    @transaction.atomic
    def save(self):
        estate = Estate(neighborhood=self.cleaned_data['neighborhood'],
                        partitioning=self.cleaned_data['partitioning'],
                        address=self.cleaned_data['address'],
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
        #listing.save()

        return listing

