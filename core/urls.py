from django.urls import path

from core.views import Index


urlpatterns = [
    path('', Index.as_view(), name='core.index'),
]
