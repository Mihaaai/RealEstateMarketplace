from ..models import Listing
from .ListListingsView import ListListingsView


class SearchListListingsView(ListListingsView):
    def __init__(self):
        super(SearchListListingsView, self).__init__()

    def get_queryset(self):
        return Listing.objects.filter(is_closed=False).filter(title__contains=self.request.GET.get('q')).order_by('-created')
