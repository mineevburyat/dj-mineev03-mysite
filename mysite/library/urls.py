from django.urls import path
from .views import ListBooks, DetailBook, GenreDetail

app_name = 'library'

urlpatterns = [
    path('', ListBooks.as_view(), name='index'),
    # path('add/', AddPost.as_view(), name="add"),
    path('genre/', GenreDetail.as_view(), name='genres'),
    path('post/<slug:slug>', DetailBook.as_view(), name='detail'),
]