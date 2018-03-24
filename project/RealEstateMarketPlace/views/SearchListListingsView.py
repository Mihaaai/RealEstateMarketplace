from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import Listing
from . import ListListingsView


class SearchListListingsView(ListListingsView):
    template_name = 'list_listings_template.html'
    model = Listing
    context_object_name = 'listings'

    def get_queryset(self):
        return Listing.objects.filter(is_closed=False) \
            .filter(title__contains=self.request.GET.get('q')) \
            .order_by('-created')
