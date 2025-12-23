from django.urls import path, include
from .views import contact_ajax_form_view

app_name = 'contact'

urlpatterns = [
    path('ajax/', contact_ajax_form_view, name='ajax'),
]