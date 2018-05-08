from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from ..forms import UpdateListingForm
from ..models import Listing

class UpdateListingView(LoginRequiredMixin, UpdateView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy('list_listings')
	form_class = UpdateListingForm
	template_name = 'update_listing_template.html'
	model = Listing

	def get_initial(self):

		listing = self.get_object()
		estate = listing.estate_id

		return {
			'user_id': self.request.user.id,
			'neighborhood': estate.neighborhood,
			'partitioning': estate.partitioning,
			'image': estate.image,
			'rooms': estate.rooms,
			'bathrooms': estate.rooms,
			'floor': estate.floor,
			'size': estate.size,
			'year': estate.year,
			'price': estate.price
		}
