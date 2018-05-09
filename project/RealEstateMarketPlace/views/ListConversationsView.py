from django.views.generic import ListView
from rest_framework import authentication, permissions
from ..models import Message,Listing,User
from django.db.models import Q

class ListConversationsView(ListView):
 
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    template_name = 'list_conversations_template.html'
    context_object_name = 'conversations'

    def get_queryset(self):        
        #get each listing for which there is at least a message by/from logged user
        _listings = Listing.objects.filter(pk__in = Message.objects.filter(Q(receiver_id=self.request.user)|Q(sender_id=self.request.user)).values('listing_id').distinct())  

        conversations = {}
        #for each listing, find all users whom which logged user talked to
        for listing in _listings:
            sender_id_list = Message.objects.filter(receiver_id=self.request.user).filter(listing_id = listing).values('sender_id').distinct()
            receiver_id_list = Message.objects.filter(sender_id=self.request.user).filter(listing_id = listing).values('receiver_id').distinct()

            users = User.objects.filter(Q(pk__in = sender_id_list)| Q(pk__in = receiver_id_list)).distinct()
            conversations[listing] = users
        return conversations