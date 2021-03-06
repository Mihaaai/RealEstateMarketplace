from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from ..models import Listing
from .ListListingsView import ListListingsView


class ListMyListingsView(LoginRequiredMixin, ListListingsView):
    def __init__(self):
        super(ListMyListingsView, self).__init__()

    login_url = reverse_lazy('login')
    template_name = "list_my_listings_template.html"

    def get_queryset(self):
        return Listing.objects.filter(user_id=self.request.user).filter(is_closed=False).order_by('-created')
