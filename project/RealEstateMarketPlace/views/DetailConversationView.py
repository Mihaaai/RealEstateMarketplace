from rest_framework.views import APIView
from django.views.generic import DetailView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from ..models import Listing, Message, User
from django.db.models import Q


class DetailConversationView(DetailView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    template_name = 'detail_conversation_template.html'
    context_object_name = 'conversation'
    model = Listing

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        listing_id=self.kwargs['pk']
        user_id=self.kwargs['user_id']
        context['uid']=user_id
        context['listing_id']=listing_id
        listing = Listing.objects.get(id=listing_id)
        user = User.objects.get(id=user_id)
        messages = Message.objects.filter(listing_id = listing).filter((Q(sender_id = user) & Q(receiver_id = self.request.user)) | (Q(sender_id = self.request.user) & Q(receiver_id = user)) )
        context['conversation']=messages
        return context
    
