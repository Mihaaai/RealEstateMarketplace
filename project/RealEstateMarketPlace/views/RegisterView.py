from ..forms import RegisterForm

from django.shortcuts import reverse
from ..models import User
from django.views.generic import CreateView


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register_template.html'
    model = User

    def get_success_url(self):

        return reverse('homepage')
