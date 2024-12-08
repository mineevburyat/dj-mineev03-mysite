from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Index(TemplateView):
    template_name = "main/index.html"
    extra_context = {'sections': [
        'main/slider.html',
        'main/tasks.html',
        'main/about.html',
        'main/hobby.html',
        'main/services.html'
    ]}