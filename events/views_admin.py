from django.views.generic import CreateView

from events.models import Event


class EventCreate(CreateView):
    model = Event
    fields = ['title', 'start_time', 'end_time', 'description', 'location']
    template_name = 'events/create.html'
