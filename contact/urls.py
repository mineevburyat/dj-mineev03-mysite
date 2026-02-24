from django.urls import path, include
from .views import contact_ajax_form_view, refresh_captcha, save_lead
# from captcha.views import captcha_image

app_name = 'contact'

urlpatterns = [
    path('ajax/', contact_ajax_form_view, name='ajax'),
    path('refresh-captcha/', refresh_captcha, name='refresh_captcha'),
    # path('captcha/image/<key>/', captcha_image, name='captcha_image'),
    path('save-lead/', save_lead, name='save_lead'),
]