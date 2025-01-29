from django.urls import path
from .views import (ListPost, 
                    DetailPost,
                    ListCategory, ListPostbyTags)
app_name = 'blog'

urlpatterns = [
    path('', ListCategory.as_view(), name='listcatrgory'),
    path('tags', ListPostbyTags, name='listpost_by_tags'),
    # path('add/', AddPost.as_view(), name="add"),
    path('<slug:slug>', ListPost.as_view(), name='listposts'),
    
]