from django.http import HttpResponse
from django.views.generic import DetailView
from ..models import Listing, FavoriteListing


class DetailListingView(DetailView):
    template_name = 'detail_listing_template.html'
    model = Listing
    context_object_name = 'listing'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        listing = Listing.objects.get(id=self.kwargs['pk'])
        context['is_fav'] = FavoriteListing.objects \
            .filter(user_id=self.request.user.id, listing_id=listing.id).count()
        return context
