from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import CategoryTree, Post
from .forms import AddPostForm


class ListBlog(ListView):
	template_name = "blog/list.html"
	model = Post
	context_object_name = 'posts'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Блог'
		context['category'] = CategoryTree.objects.all()
		return context

	
class DetailPost(DetailView):
	model = Post
	template_name = "blog/detail.html"
	


class AddPost(CreateView):
	form_class = AddPostForm
	template_name = 'blog/addpost.html'