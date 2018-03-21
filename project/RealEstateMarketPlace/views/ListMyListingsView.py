from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import Listing
from .ListListingsView import ListListingsView


class ListMyListingsView(LoginRequiredMixin, ListListingsView):
    def __init__(self):
        super(ListMyListingsView, self).__init__()

    login_url = '/login/'
    paginate_by = 100

    def get_queryset(self):
        return Listing.objects.filter(user_id=self.kwargs['pk']).filter(is_closed=False).order_by('-created')
