from django.shortcuts import render
from django.http import JsonResponse
from django.forms.utils import ErrorDict
import json
from home.forms import ContactForm


def contact_ajax_form_view(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        print('ok post ajax')
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            # Данные формы
            cleaned_data = form.cleaned_data
            
            # Отправка email или сохранение в БД
            try:
                # ... код отправки email ...
                
                return JsonResponse({
                    'success': True,
                    'message': 'Сообщение успешно отправлено!'
                })
            except Exception as e:
                return JsonResponse({
                    'success': False,
                    'message': f'Ошибка отправки: {str(e)}'
                }, status=500)
        else:
            # Формируем ошибки для AJAX
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = error_list
            
            return JsonResponse({
                'success': False,
                'errors': errors,
                'message': 'Пожалуйста, исправьте ошибки в форме'
            }, status=400)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)