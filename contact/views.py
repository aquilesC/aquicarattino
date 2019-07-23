from django.urls import reverse_lazy
from django.views.generic import CreateView


from contact.models import ContactMessage


class ContactView(CreateView):
    template_name = 'contact/contact.html'
    model = ContactMessage
    fields = ['email', 'subject', 'text']
    success_url = reverse_lazy('contact.thanks')
