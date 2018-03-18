from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def AddListingView(request):
    return render(request, 'add_listing_template.html')  # to be replaced in the near future by Ghido
