from django.shortcuts import redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from ..models import  Listing

class CloseListingAPI(APIView):
    """
    View to list all users in the system.
    
    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, listing_id, format=None):
        """
        Adds or removes a listing from favorites.
        """
        try:
            to_close_listing = Listing.objects.get(id=listing_id)
        except Listing.DoesNotExist:
            to_close_listing = None

        response = {}

        # this should not be necessary since we have declared above that the person who access this url needs IsAuthenticated permission
        # if self.request.user.is_authenticated:
        if to_close_listing:
        	response['status'] = 'ok'
        else:
        	response['status'] = 'error'
        # if the listing is already closed, we open it
        if to_close_listing.is_closed:
            to_close_listing.is_closed = False
            to_close_listing.save()
            response['message'] = 'Listing opened!'
        else:
            to_close_listing.is_closed = True
            to_close_listing.save()
            response['message'] = 'Listing closed!'
        # else:
        #     response['status'] = 'error'
        #     response['message'] = 'You must be authenticated for this.'

        return Response(response)
