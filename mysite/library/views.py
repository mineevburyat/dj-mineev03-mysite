from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Book, BookInstance, eBookInstance, Author, Genre

class ListBooks(ListView):
    template_name = "library/list.html"
    model = eBookInstance
    context_object_name = 'ebooks'

class DetailBook(TemplateView):
    template_name = 'library/detail.html'

