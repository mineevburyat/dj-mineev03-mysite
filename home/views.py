from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, DetailView
from .forms import ContactForm


class HomePage(View):
    template_name = 'home/index.html'
    context = {
        'title': 'Главная',
        'work_years': '8',
        'email': 'alex@mineev-03.ru',
        'phone': '+7 (924) 5555 937',
        'form': ContactForm()}
    def get(self, request):
        return render(request, template_name=self.template_name, context=self.context)
    
    def post(self, request):
        print(request)