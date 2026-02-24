from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.conf import settings
# from django.core.validators import validate_email
# from django.core.exceptions import ValidationError
import re
from django.forms.utils import ErrorDict
import json
from home.forms import ContactForm
from .models import Lead
from .forms import LeadForm

@csrf_exempt
@require_POST
def save_lead(request):
    """Сохранение лида из попапа"""
    try:
        # Парсим JSON из запроса
        data = json.loads(request.body)
        
        # Добавляем технические данные
        data['ip_address'] = request.META.get('REMOTE_ADDR')
        data['user_agent'] = request.META.get('HTTP_USER_AGENT', '')
        
        # Сохраняем через форму
        form = LeadForm(data)
        if form.is_valid():
            lead = form.save()

            # Можно отправить уведомление в Telegram
            # send_telegram_notification(lead)
            
            return JsonResponse({
                'success': True,
                'message': 'Спасибо! Проверьте почту.'
            })
        else:
            return JsonResponse({
                'error': 'Ошибка валидации',
                'details': form.errors
            }, status=400)
            
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Неверный формат JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def send_telegram_notification(lead):
    """Отправка уведомления в Telegram"""
    bot_token = 'YOUR_BOT_TOKEN'  # Замени на свой
    chat_id = 'YOUR_CHAT_ID'      # Замени на свой
    
    message = f"""
    🔔 <b>Новый лид!</b>

    👤 Имя: {lead.name or 'Не указано'}
    📧 Email: {lead.email or 'Не указано'}
    📱 Telegram: {lead.telegram}
    📌 Источник: {lead.get_source_display()}
    🕐 Время: {lead.created_at.strftime('%d.%m.%Y %H:%M')}
    🌐 Страница: {lead.url or 'Не указана'}

    🖥 IP: {lead.ip_address or 'Не определен'}
    """
    
    # Асинхронная отправка (чтобы не тормозить ответ)
    import threading
    import requests
    
    def send():
        try:
            requests.post(
                f'https://api.telegram.org/bot{bot_token}/sendMessage',
                json={
                    'chat_id': chat_id,
                    'text': message,
                    'parse_mode': 'HTML'
                },
                timeout=5
            )
        except:
            pass
    
    threading.Thread(target=send).start()

@require_POST
def contact_ajax_form_view(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Данные формы
            cleaned_data = form.cleaned_data
            name = cleaned_data.get('name')
            email = cleaned_data.get('email')
            subject = cleaned_data.get('subject')
            message = cleaned_data.get('message')
            phone = cleaned_data.get('phone')
            # Проверка телефона (если указан)
            if phone and not re.match(r'^[\d\s\-\+\(\)]{10,20}$', phone):
                # errors['phone'] = ['Пожалуйста, введите корректный номер телефона']
                print('Пожалуйста, введите корректный номер телефона')
            # Также можно сохранить в базу данных
            # ContactMessage.objects.create(
            #     name=name,
            #     email=email,
            #     phone=phone,
            #     message=message
            # )
            # проверить отправлял ли этот браузер письма уже ил нет
            if request.session.get('email_sent'):
                return JsonResponse({
                    'status': 'error',
                    'message': 'Письмо уже отправлено (сессии)'
                    })
            if request.COOKIES.get('email_sent'):
                return JsonResponse({
                    'status': 'error',
                    'message': 'Письмо уже отправлено (cookie)'
                    })
            # Отправка email или сохранение в БД
            try:
                 # Формируем текст письма
                email_subject = f'Новое сообщение от {name}'
                body = f"""
                Имя: {name}
                Email: {email}
                Телефон: {phone if phone else 'Не указан'}
                Тема: {subject}
                Сообщение:
                {message}
                
                ---
                Это сообщение отправлено с сайта через AJAX форму.
                """
                
                # Отправляем email
                send_mail(
                    subject=email_subject,
                    message=body,
                    from_email=settings.EMAIL_FROM,
                    recipient_list=[settings.CONTACT_EMAIL],  # Укажите email получателя
                    fail_silently=False,
                )
                request.session['email_sent'] = True
                response = JsonResponse({
                    'success': True,
                    'message': 'Сообщение успешно отправлено!'
                })
                response.set_cookie('email_sent', 'true', max_age=int(settings.SESSION_COOKIE_AGE))
                return response
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
    
    return JsonResponse({'error': 'Invalid request'}, status=405)

def refresh_captcha(request):
    """Генерация новой капчи"""
    from captcha.models import CaptchaStore
    from captcha.helpers import captcha_image_url
    
    new_key = CaptchaStore.generate_key()
    new_image_url = captcha_image_url(new_key)
    
    return JsonResponse({
        'key': new_key,
        'image_url': new_image_url
    })