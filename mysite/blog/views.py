from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import CategoryTree, Post
from .forms import AddPostForm
from taggit.models import Tag 



class ListCategory(ListView):
	template_name = "blog/listcategory.html"
	model = CategoryTree
	context_object_name = 'categorys'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Блог'
		context['category'] = CategoryTree.objects.all()
		return context

class ListPost(ListView):
	template_name = "blog/listpost.html"
	model = Post
	context_object_name = 'posts'

	def get_queryset(self):
		self.category = CategoryTree.objects.get(slug=self.kwargs['slug'])
		queryset = list(Post.objects.filter(category=self.category))
		for category in self.category.get_children():
			queryset.extend(list(Post.objects.filter(category=category)))
		return queryset
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Интересы ' + self.category.title
		context['category'] = self.category
		return context

def ListPostbyTags(request):
	if request.GET:
		try:
			tag = Tag.objects.get(name=request.GET.get('q'))
			posts = Post.objects.filter(tags__in=[tag])
			context ={
				"posts": posts,
				'title': 'Тэг ' + tag.name,
				"tagpage": tag.name
			}
			return render(request, 
				 template_name="blog/listpost.html",
				 context=context)
		except:
			return redirect('blog:listcatrgory')
	
	
class DetailPost(DetailView):
	model = Post
	template_name = "blog/detailpost.html"
	


class AddPost(CreateView):
	form_class = AddPostForm
	template_name = 'blog/addpost.html'