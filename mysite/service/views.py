from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Course

# Create your views here.
class IndexView(ListView):
    template_name = 'service/index.html'
    model = Course
    context_object_name = 'courses'

class CourseView(TemplateView):
    template_name = 'service/detail.html'