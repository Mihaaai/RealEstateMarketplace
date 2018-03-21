from django.views.generic import CreateView
from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from ..forms import AddListingForm
from ..models import Listing


class AddListingView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    success_url = '/'
    form_class = AddListingForm
    template_name = 'add_listing_template.html'
    model = Listing

    def get_initial(self):
        return {
            'user_id': self.request.user
        }


