from django.http import HttpResponse
from django.views.generic.list import ListView
from ..models import Listing

# Create your views here.


class ListListingsView(ListView):
    template_name = 'list_listings_template.html'
    model = Listing

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
