from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from ..forms import AddListingForm
from ..models import Listing
from ..ml import retrain
import pdb


class AddListingView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('list_listings')
    form_class = AddListingForm
    template_name = 'add_listing_template.html'
    model = Listing

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user
        self.object.save()

        return super(AddListingView, self).form_valid(form)
