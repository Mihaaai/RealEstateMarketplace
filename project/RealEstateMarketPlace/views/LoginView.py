from ..forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def LoginView(request):
    context = {}

    if request.method == 'GET':
        form = LoginForm()

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'],
                                password=form.cleaned_data['password'])

            if user:
                login(request=request,
                      user=user)
                return redirect('default')

    context['form'] = form

    return render(request, 'login_template.html', context)
