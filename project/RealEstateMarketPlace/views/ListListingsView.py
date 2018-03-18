from django.http import HttpResponse
from django.shortcuts import render
from ..models import Listing

# Create your views here.


def ListListingsView(request):
    context = {}
    context['listings'] = Listing.objects.all()
    return render(request, 'list_listings_template.html', context)
