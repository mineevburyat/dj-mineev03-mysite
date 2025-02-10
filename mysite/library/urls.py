from django.urls import path
from .views import ListBooks, DetailBook

app_name = 'library'

urlpatterns = [
    path('', ListBooks.as_view(), name='index'),
    # path('add/', AddPost.as_view(), name="add"),
    path('<slug:slug>', DetailBook.as_view(), name='detail'),
    
]