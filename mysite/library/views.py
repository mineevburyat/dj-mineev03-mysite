from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Book, BookInstance, eBookInstance, Genre

class ListBooks(ListView):
    template_name = "library/list.html"
    model = Book
    context_object_name = 'books'

class DetailBook(TemplateView):
    template_name = 'library/detail.html'

