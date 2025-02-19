from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from .models import CategoryTree, Post
from .forms import AddPostForm
from taggit.models import Tag 
from django.urls import reverse


class ListCategory(ListView):
	template_name = "blog/listcategory.html"
	model = CategoryTree
	context_object_name = 'categorys'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Блог'
		context['category'] = CategoryTree.objects.all()
		context['breadcrumbs'] = (
        {'name': 'Главная', 'url': '/'},
        {'name': 'Интересы', 'url': ''},
        )
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
		root = self.category.get_root()
		context['breadcrumbs'] = [
        {'name': 'Главная', 'url': '/'},
        {'name': 'Интересы', 'url': reverse('blog:index')}]
		if root:
			context['breadcrumbs'].append(
				{'name': root.title, 
	 			'url': reverse('blog:listposts', kwargs={'slug': root.slug})})
		context['breadcrumbs'].append(
			{'name': self.category.title, 'url': ''})
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
	

def viewPost(request, cslug, pslug):
	category = get_object_or_404(CategoryTree, slug=cslug)
	# CategoryTree.objects.get(slug=cslug)
	post = get_object_or_404(Post, slug=pslug)
	root = category.get_root()
	breadcrumbs = [
        {'name': 'Главная', 'url': '/'},
        {'name': 'Интересы', 'url': reverse('blog:index')}]
	if root:
		breadcrumbs.append(
				{'name': root.title, 
	 			'url': reverse('blog:listposts', kwargs={'slug': root.slug})})
	breadcrumbs.append(
			{'name': category.title, 'url': ''})
	context = {
		'category': category,
		'post': post,
		'breadcrumbs': breadcrumbs
	}
	return render(request, "blog/detailpost.html", context)


class AddPost(CreateView):
	form_class = AddPostForm
	template_name = 'blog/addpost.html'