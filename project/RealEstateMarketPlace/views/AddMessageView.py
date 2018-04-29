from django.shortcuts import redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from ..models import Message, Listing

class AddMessageAPI(APIView):
    
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, listing_id, format=None):
        """
        Add Message
        """

        response = {}

        try:
            listing = Listing.objects.get(id=listing_id)
        except FavoriteListing.DoesNotExist:
            response['status']= 'error'

        """
        TODO: Check if request.user != listing.user_id
        TODO: Check if request.POST.get('message',"") != null
        """

        response['status'] = 'ok'

        message = Message(sender_id=request.user,
                          listing_id=listing,
                          receiver_id=listing.user_id,
                          message = request.POST.get('message',""))

        message.save()
        response['message'] = 'Message Sent!'

        return Response(response)