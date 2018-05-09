from django.shortcuts import redirect

def handler404(request):
	return redirect('list_listings')
