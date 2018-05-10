from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from ..forms import AddListingForm
from ..models import Listing
from ..ml import retrain
import pdb


class AddListingView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = AddListingForm
    template_name = 'add_listing_template.html'
    model = Listing

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user
        self.object.save()

        return redirect('details_listing',self.object.id)
