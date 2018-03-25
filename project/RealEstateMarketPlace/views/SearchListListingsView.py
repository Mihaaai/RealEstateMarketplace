from ..models import Listing
from .ListListingsView import ListListingsView


class SearchListListingsView(ListListingsView):
    def __init__(self):
        super(SearchListListingsView, self).__init__()

    def get_queryset(self):

        # http://127.0.0.1:8000/list/search/?rooms=5&minPrice=200&maxPrice=300&minYear=1997&maxYear=2018&city=Bucuresti
        rooms = self.request.GET.get('rooms') if self.request.GET.get('rooms') else 0
        minPrice = self.request.GET.get('minPrice') if self.request.GET.get('minPrice') else 0
        maxPrice = self.request.GET.get('maxPrice') if self.request.GET.get('maxPrice') else 99999999
        minYear = self.request.GET.get('minYear') if self.request.GET.get('minYear') else 0
        maxYear = self.request.GET.get('maxYear') if self.request.GET.get('maxYear') else 9999
        city = self.request.GET.get('city') if self.request.GET.get('city') else ""
        search_keyword = self.request.GET.get('q') if self.request.GET.get('q') else ""

        return Listing.objects.filter(is_closed=False) \
            .filter(estate_id__rooms=rooms) \
            .filter(estate_id__price__range=(minPrice, maxPrice)) \
            .filter(estate_id__year__range=(minYear, maxYear)) \
            .filter(estate_id__city__contains=city) \
            .filter(title__contains=search_keyword) \
            .order_by('-created')
