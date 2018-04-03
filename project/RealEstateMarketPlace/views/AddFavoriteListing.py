from django.shortcuts import redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from ..models import FavoriteListing, Listing


# def add_favorite_listing(request, listing_id):
#     if request.user.is_authenticated:
#         if listing_id is not None:
#             try:
#                 fav_listing = FavoriteListing.objects.get(user_id=request.user.id, listing_id=listing_id)
#             except FavoriteListing.DoesNotExist:
#                 fav_listing = None

#             if fav_listing is None:
#                 fav_listing = FavoriteListing(user_id=request.user,
#                                               listing_id=Listing.objects.get(id=listing_id))
#                 fav_listing.save()
#             else:
#                 fav_listing.delete()
#         else:
#             return redirect('404.html')
#     else:
#         return redirect('404.html')

#     return redirect('details_listing', pk=listing_id)


class AddFavoriteListingAPI(APIView):
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
            fav_listing = FavoriteListing.objects.get(user_id=request.user.id, listing_id=listing_id)
        except FavoriteListing.DoesNotExist:
            fav_listing = None

        response = {}

        # this should not be necessary since we have declared above that the person who access this url needs IsAuthenticated permission
        # if self.request.user.is_authenticated:
        response['status'] = 'ok'
        if fav_listing:
            fav_listing.delete()
            response['message'] = 'Listing removed from favorites!'
        else:
            fav_listing = FavoriteListing(user_id=request.user,
                                          listing_id=Listing.objects.get(id=listing_id))
            fav_listing.save()
            response['message'] = 'Listing added to favorites!'
        # else:
        #     response['status'] = 'error'
        #     response['message'] = 'You must be authenticated for this.'

        return Response(response)
