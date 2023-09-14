from django.urls import path
from .views import goal_list

app_name = 'spending'

urlpatterns = [
    path('', goal_list, name='goal_list'),
]