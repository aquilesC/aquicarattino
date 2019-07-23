"""
    aquicarattino URL Configuration
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('contact/', include('contact.urls')),
    path('blog/', include('blog.urls')),
    path('contacts/', include('contacts.urls')),
    path('events/', include('events.urls')),
    path('resume/', include('resume.urls')),
    path('admin/', admin.site.urls),
]
