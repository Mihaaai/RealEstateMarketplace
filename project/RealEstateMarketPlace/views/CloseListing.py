from django.shortcuts import redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from ..models import  Listing

class CloseListingAPI(APIView):
	"""
	View to close and open a published listing
	
	* Requires token authentication.
	"""
	authentication_classes = (authentication.SessionAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)

	def get(self, request, listing_id, format=None):
		"""
		Opens or closes a listing
		"""
		try:
			to_close_listing = Listing.objects.get(id = listing_id)
		except Listing.DoesNotExist:
			to_close_listing = None

		owned_listings_ids = [l.id for l in Listing.objects.filter(user_id = request.user)]
		is_listing_owned = int(listing_id) in owned_listings_ids

		response = {}
		
		if to_close_listing and is_listing_owned:
			response['status'] = 'ok'
		else:
			response['status'] = 'error'

		# if the current listing is not owned by the current user, return an error
		if not is_listing_owned:
			response['message'] = "You can close only the listing you own " + listing_id
			return Response(response)

		# if the listing is already closed, we open it
		if to_close_listing.is_closed:
			to_close_listing.is_closed = False
			to_close_listing.save()
			response['message'] = 'Listing opened!'
		else:
			to_close_listing.is_closed = True
			to_close_listing.save()
			response['message'] = 'Listing closed!'
		

		return Response(response)

