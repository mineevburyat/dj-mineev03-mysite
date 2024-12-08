from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Category
from .forms import AddPostForm


class ListBlog(ListView):
	template_name = "blog/list.html"
	model = Post
	context_object_name = 'posts'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Блог'
		context['categorys'] = Category.objects.all()
		return context
	
class DetailPost(DetailView):
	model = Post
	template_name = "blog/detail.html"


class AddPost(CreateView):
	form_class = AddPostForm
	template_name = 'blog/addpost.html'