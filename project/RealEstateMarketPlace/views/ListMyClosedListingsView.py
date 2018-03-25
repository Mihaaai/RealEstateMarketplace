from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from ..models import Listing
from .ListListingsView import ListListingsView


class ListMyClosedListingsView(LoginRequiredMixin, ListListingsView):
    def __init__(self):
        super(ListMyClosedListingsView, self).__init__()

    template_name = "list_my_listings_template.html"
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Listing.objects.filter(user_id=self.request.user).filter(is_closed=True).order_by('-created')
