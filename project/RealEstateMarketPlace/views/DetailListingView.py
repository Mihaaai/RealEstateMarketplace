from django.http import HttpResponse
from django.views.generic import DetailView
from ..models import Listing

class DetailListingView(DetailView):
	template_name = 'detail_listing_template.html'
	model = Listing
	context_object_name = 'listing'