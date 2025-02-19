from django.urls import path
from .views import (ListPost, 
                    viewPost,
                    ListCategory, ListPostbyTags)
app_name = 'blog'

urlpatterns = [
    path('', ListCategory.as_view(), name='index'),
    path('category/<slug:slug>', ListPost.as_view(), name='listposts'),
    path('tags', ListPostbyTags, name='listpost_by_tags'),

    # path('add/', AddPost.as_view(), name="add"),
    
    path('category/<slug:cslug>/post/<slug:pslug>', viewPost, name='post'),
    
]