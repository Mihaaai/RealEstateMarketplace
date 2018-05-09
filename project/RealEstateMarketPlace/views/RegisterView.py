from django.shortcuts import reverse
from django.contrib.auth import authenticate, login
from ..models import User
from django.views.generic import CreateView

from ..forms import RegisterForm



class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register_template.html'
    model = User

    def get_success_url(self):
        return reverse('list_listings')

    # INFO currently not working properly
    # login user after completing the form
    # def form_valid(self, form):
    #   #save the new user first
    #   self.object = form.save()
    #   #get the username and password
    #   email = self.request.POST['email']
    #   password = self.request.POST['password1']
    #   #authenticate user then login
    #   user = authenticate(username = email, password = password)
    #   if user is not None:
    #   	login(self.request, user)

    #   return super().form_valid(form)

