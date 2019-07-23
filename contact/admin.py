from django.contrib import admin

from contact.models import ContactMessage

admin.site.register((ContactMessage,))
