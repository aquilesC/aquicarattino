from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.views.generic import TemplateView

from events.views_admin import EventCreate


urlpatterns = [
    path('', TemplateView.as_view(template_name='core/coming_soon.html'), name='events.index'),
    path('admin/create', staff_member_required(EventCreate.as_view()), name='events.create'),
]
