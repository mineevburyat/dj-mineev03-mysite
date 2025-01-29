from django.urls import path
from .views import ListBlog, DetailPost
app_name = 'blog'

urlpatterns = [
    path('', ListBlog.as_view(), name='list'),
    # path('add/', AddPost.as_view(), name="add"),
    path('<slug:slug>', DetailPost.as_view(), name='detail'),
    
]