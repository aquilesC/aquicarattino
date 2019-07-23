from django.contrib import admin

from events.models import Guest, Event

admin.site.register((Event, Guest))
