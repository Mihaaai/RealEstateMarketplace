from django.shortcuts import redirect
from django.contrib.auth import logout


def LogoutView(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')
