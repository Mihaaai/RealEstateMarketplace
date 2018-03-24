from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from ..forms import AddListingForm
from ..models import Listing


class AddListingView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('list')
    form_class = AddListingForm
    template_name = 'add_listing_template.html'
    model = Listing

    def get_initial(self):
        return {
            'user_id': self.request.user
        }
