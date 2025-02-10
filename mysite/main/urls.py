from django.urls import path
from .views import Index, SignUpView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView

app_name = 'spending'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('passreset', 
         PasswordResetView.as_view(
             template_name='registration/password_reset_form.html'),
             name='password_reset'),
    path('passreset/done/',
         PasswordResetDoneView.as_view(
             template_name = "registration/password_reset_done.html"),
             name='password_reset_done'),
]