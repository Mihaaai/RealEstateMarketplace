from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from ..forms import UpdateListingForm
from ..models import Listing


class UpdateListingView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('list_listings')
    form_class = UpdateListingForm
    template_name = 'update_listing_template.html'
    model = Listing
    context_object_name = 'listing'

    def get_initial(self):
        listing = self.get_object()
        estate = listing.estate_id

        return {
            'neighborhood': estate.neighborhood,
            'partitioning': estate.partitioning,
            'address': estate.address,
            'image': estate.image,
            'rooms': estate.rooms,
            'bathrooms': estate.bathrooms,
            'floor': estate.floor,
            'size': estate.size,
            'year': estate.year,
            'price': estate.price
        }

    # admits only updates regarding the listings owned by the current user
    def get(self, request, *args, **kwargs):
        owned_listings_pk = [
            l.pk for l in Listing.objects.filter(user_id=request.user)]
        if kwargs['pk'] in owned_listings_pk:
            return super().get(request, args, kwargs)
        else:
            return redirect('list_listings')

    def post(self, request, *args, **kwargs):
        owned_listings_pk = [
            l.pk for l in Listing.objects.filter(user_id=request.user)]
        if kwargs['pk'] in owned_listings_pk:
            return super().post(request, args, kwargs)
        else:
            return redirect('list_listings')

    def form_valid(self, form):
        self.object = form.save()
        self.object.save()
        return super(UpdateListingView, self).form_valid(form)
