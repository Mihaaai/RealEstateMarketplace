from django.views.generic import ListView
from rest_framework import authentication, permissions
from ..models import Message,Listing,User

class ListConversationsView(ListView):
 
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    template_name = 'list_conversations_template.html'
    context_object_name = 'conversations'

    def get_queryset(self):        
        #get each listing for which there is at least a message sent to self
        _listings = Listing.objects.filter(pk__in = Message.objects.filter(receiver_id=self.request.user).values('listing_id').distinct())  

        conversations = {}
        #for each listing, find all users who have sent a message
        for listing in _listings:
            sender_id_list = Message.objects.filter(receiver_id=self.request.user).filter(listing_id = listing).values('sender_id').distinct()
            senders = User.objects.filter(pk__in = sender_id_list)
            conversations[listing] = senders

        return conversations