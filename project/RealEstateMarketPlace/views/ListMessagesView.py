from django.views.generic import ListView

from ..models import Message

class ListMessagesView(ListView):
    template_name = 'list_messages_template.html'
    model = Message
    context_object_name = 'messages'
    paginate_by = 20

    def get_queryset(self):
        return Message.objects.filter(receiver_id=self.request.user).order_by('-date')