from django.views.generic import ListView
from django.db.models import F

from ..models import Listing


class ListListingsView(ListView):
    template_name = 'list_listings_template.html'
    model = Listing
    context_object_name = 'listings'
    paginate_by = 20

    def get_queryset(self):
        return Listing.objects.filter(is_closed=False).order_by('-ordering')
        #annotate(ordering=F('estate_id.estimated_price') - F('estate_id.price'))
