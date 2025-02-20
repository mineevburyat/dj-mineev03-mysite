from django.urls import path
from .views import IndexView, CourseView

app_name = 'service'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detail/', CourseView.as_view(), name='detail'),
]