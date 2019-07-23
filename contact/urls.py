from django.urls import path
from django.views.generic import TemplateView

from contact.views import ContactView

urlpatterns = [
    path('', ContactView.as_view(), name='contact.index'),
    path('thanks', TemplateView.as_view(template_name='contact/contact.html'), name='contact.thanks')
]
