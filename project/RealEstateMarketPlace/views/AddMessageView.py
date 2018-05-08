from django.shortcuts import redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from ..models import User, Message, Listing

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

        if "" == request.POST.get('message',"").strip():
            response['status'] = 'error'
            response['message'] = 'You can\'t send empty messages'
            return Response(response)

        if request.user == listing.user_id:
            response['status'] = 'error'
            response['message'] = 'You can\'t send messages to yourself'
            return Response(response)

        if request.POST.get('receiver_id',"") != '' :
            receiver_id = User.objects.get(id = request.POST.get('receiver_id',""))
        else:
            receiver_id = listing.user_id

        response['status'] = 'ok'

        message = Message(sender_id=request.user,
                          listing_id=listing,
                          receiver_id=receiver_id,
                          message = request.POST.get('message',""))

        message.save()
        response['message'] = 'Message Sent!'

        return Response(response)