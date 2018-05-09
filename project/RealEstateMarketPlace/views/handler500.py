from django.shortcuts import redirect

def handler500(request):
	return redirect('list_listings')
