from ..forms import ResetPasswordForm
from ..models import User
from ..utils import token_encoder

from django.views.generic import View
from django.shortcuts import redirect
from django.shortcuts import render

import jwt


class ResetPasswordView(View):

    def get(self, request):

        token = request.GET.get('token', '')
        if token == '':
            return redirect('404.html')

        key = token_encoder.read_key_from_file()
        try:
            jwt.decode(token, key)
        except jwt.ExpiredSignatureError:
            print('expired')
            return redirect('404.html')
        except jwt.InvalidTokenError:
            print('invalid')
            return redirect('404.html')

        context = {}
        form = ResetPasswordForm()
        context['form'] = form
        return render(request, 'reset_password_template.html', context)

    def post(self, request):
        context = {}
        form = ResetPasswordForm(request.POST)

        if form.is_valid():
            token = request.GET.get('token', '')
            password = form.cleaned_data['password']
            return self.update_password(request, token, password)
        else:
            form = ResetPasswordForm()
            context['form'] = form
            context['error'] = 'An error has occured.'
            return render(request, 'reset_password_template.html', context)

    def update_password(self, request, token, password):
        key = token_encoder.read_key_from_file()

        try:
            email = jwt.decode(token, key)['em']
        except jwt.ExpiredSignatureError:
            print('expired')
            return redirect('404.html')
        except jwt.InvalidTokenError:
            print('invalid')
            return redirect('404.html')

        user = User.objects.get(email=email)

        if user is not None:
            user.set_password(password)
            user.save()
            return render(request, 'reset_password_success_template.html', {})
        else:
            return redirect('list_listings')
