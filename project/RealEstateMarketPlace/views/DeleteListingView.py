from django.urls import reverse_lazy
from django.views.generic import DeleteView
from ..models import Listing, Estate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class DeleteListingView(LoginRequiredMixin,DeleteView):
	login_url = reverse_lazy('login')
	model = Listing
	success_url = reverse_lazy('list_listings')
	template_name = 'confirm_delete_listing_template.html'
	context_object_name = 'listing'

	# admits only deletes regarding the listings owned by the current user
	def get(self,request,*args,**kwargs):
		owned_listings_pk = [l.pk for l in Listing.objects.filter(user_id = request.user)]
		if kwargs['pk'] in owned_listings_pk:
			return super().get(request,args,kwargs)
		else:
			return redirect('list_listings')

	def post(self,request,*args,**kwargs):
		owned_listings_pk = [l.pk for l in Listing.objects.filter(user_id = request.user)]
		listing_id = kwargs['pk']
		if listing_id in owned_listings_pk:
			# also delete estate shown in the current listing
			current_listing = Listing.objects.get(id = listing_id)
			estate = Estate.objects.get(id = current_listing.estate_id.id)
			estate.delete()
			return super().post(request,args,kwargs)
		else:
			return redirect('list_listings')		

