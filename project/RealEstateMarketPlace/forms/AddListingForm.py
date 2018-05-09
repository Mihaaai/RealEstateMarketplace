from django import forms
from django.db import transaction
from ..models import Estate, Listing, User, NEIGHBORHOOD_CHOICES, PARTITIONING_CHOICES
from ..ml import predict, retrain
import pdb


class AddListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = (
            'title', 'description',
        )

    description = forms.CharField(
        widget=forms.Textarea, max_length=1000, required=False)
    address = forms.CharField(max_length=100, required=False)
    image = forms.ImageField(required=False)
    partitioning = forms.ChoiceField(
        choices=PARTITIONING_CHOICES, required=True)
    neighborhood = forms.ChoiceField(
        choices=NEIGHBORHOOD_CHOICES, required=True)
    rooms = forms.IntegerField(required=True, min_value=1, max_value=10)
    bathrooms = forms.IntegerField(required=True, min_value=0, max_value=5)
    floor = forms.IntegerField(required=True, min_value=-1, max_value=14)
    size = forms.FloatField(required=True, min_value=20, max_value=300)
    year = forms.IntegerField(required=True, min_value=1900, max_value=2020)
    price = forms.FloatField(required=True, min_value=0)

    @transaction.atomic
    def save(self, commit=True):
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
        if commit is True:
            raw_info = {
                'year': estate.year,
                'bathrooms': estate.bathrooms,
                'floor': estate.floor,
                'rooms': estate.rooms,
                'size': estate.size,
                'neighborhood': estate.neighborhood,
                'partitioning': estate.partitioning,
            }

            estimated = predict(raw_info)
            estate.estimated_price = estimated
        # pdb.set_trace()
            estate.save()

        listing = super().save(commit=False)

        if commit is True:
            listing.estate_id = estate
            listing.ordering = estimated - estate.price
            listing.save()
            if estate.id % 200 == 0:
                retrain()

        return listing
