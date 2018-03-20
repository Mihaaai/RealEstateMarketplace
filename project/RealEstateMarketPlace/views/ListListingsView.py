from django.http import HttpResponse
from django.views.generic import ListView

from ..models import Listing


class ListListingsView(ListView):
    template_name = 'list_listings_template.html'
    model = Listing
    context_object_name = 'listings'
