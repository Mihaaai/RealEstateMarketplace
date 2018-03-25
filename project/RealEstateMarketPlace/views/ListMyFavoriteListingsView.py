from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from ..models import FavoriteListing, Listing
from .ListListingsView import ListListingsView


class ListMyFavoriteListingsView(LoginRequiredMixin, ListListingsView):
    def __init__(self):
        super(ListMyFavoriteListingsView, self).__init__()

    login_url = reverse_lazy('login')

    def get_queryset(self):
        ids = FavoriteListing.objects.values_list('listing_id', flat=True).filter(user_id=self.request.user.id)
        return Listing.objects.filter(id__in=set(ids)).order_by('-created')
