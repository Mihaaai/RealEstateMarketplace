from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from ..forms import RegisterForm, UpdateProfileForm
from ..models import User

class UpdateProfileView(LoginRequiredMixin, UpdateView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy('list_my_listings')
	form_class = UpdateProfileForm
	template_name = 'update_profile_template.html'
	model = User

	def get_initial(self):

		user = self.request.user

		return {
			'email' : user.email,
			'first_name' : user.first_name,
			'last_name' : user.last_name,
			'phone_number' : user.phone_number
		}

