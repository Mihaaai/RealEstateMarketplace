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
			'neighborhood': estate.neighborhood,
			'partitioning': estate.partitioning,
			'address': estate.address,
			'image': estate.image,
			'rooms': estate.rooms,
			'bathrooms': estate.rooms,
			'floor': estate.floor,
			'size': estate.size,
			'year': estate.year,
			'price': estate.price
		}


	def form_valid(self, form):
		self.object = form.save()
		self.object.save()
		return super(UpdateListingView, self).form_valid(form)

