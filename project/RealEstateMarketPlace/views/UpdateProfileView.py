from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect


from ..forms import RegisterForm, UpdateProfileForm
from ..models import User

class UpdateProfileView(LoginRequiredMixin, UpdateView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy('list_my_listings')
	form_class = UpdateProfileForm
	template_name = 'update_profile_template.html'
	model = User
	context_object_name = 'user'

	def get_initial(self):

		user = self.request.user

		return {
			'email' : user.email,
			'first_name' : user.first_name,
			'last_name' : user.last_name,
			'phone_number' : user.phone_number
		}

	# admits only updates regarding the current user
	def get(self,request,*args,**kwargs):
		if kwargs['pk'] == self.request.user.id:
			return super().get(request,args,kwargs)
		else:
			return redirect('list_listings')

	def post(self,request,*args,**kwargs):
		if kwargs['pk'] == self.request.user.id:
			return super().post(request,args,kwargs)
		else:
			return redirect('list_listings')		

