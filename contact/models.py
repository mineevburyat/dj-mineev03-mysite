from django.db import models

# Create your models here.
class Lead(models.Model):
    SOURCE_CHOICES = [
        ('button', 'Кнопка на сайте'),
        ('exit_intent', 'Exit Intent (уход с сайта)'),
        ('timeout', 'Автопоказ через 30 сек'),
    ]
    
    # Основные поля
    name = models.CharField('Имя', max_length=100, blank=True)
    email = models.EmailField('Email', blank=True)
    telegram = models.CharField('Telegram', max_length=100)
    # Отслеживание источника
    source = models.CharField('Источник', max_length=20, choices=SOURCE_CHOICES, default='button')
    # Технические поля
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    ip_address = models.GenericIPAddressField('IP адрес', blank=True, null=True)
    url = models.URLField('Страница отправки', max_length=500, blank=True)    
    user_agent = models.TextField('User Agent', blank=True)
    
    class Meta:
        verbose_name = 'Лид'
        verbose_name_plural = 'Лиды'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.telegram} - {self.created_at.strftime('%d.%m.%Y %H:%M')}"