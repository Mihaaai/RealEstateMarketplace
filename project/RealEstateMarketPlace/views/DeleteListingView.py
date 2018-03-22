from django.urls import reverse_lazy
from django.views.generic import DeleteView
from ..models import Listing

class DeleteListingView(DeleteView):	
	model = Listing
	success_url = reverse_lazy('list_listings')
	template_name = 'confirm_delete_listing_template.html'
	context_object_name = 'listing'
