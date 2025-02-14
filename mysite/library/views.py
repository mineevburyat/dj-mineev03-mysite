from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Book, GenreTree

class ListBooks(ListView):
    template_name = "library/list.html"
    model = Book
    context_object_name = 'books'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = GenreTree.objects.all()
        return context

class DetailBook(TemplateView):
    template_name = 'library/detail.html'

