from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликован'),
    )
    title = models.CharField(max_length=150,
                            verbose_name='Заголовок', 
                            null=True, 
                            blank=True,
                            db_index=True)
    slug = models.SlugField(max_length=150, 
                            unique=True, 
                            verbose_name='URL', 
                            null=True, 
                            blank=True,
                            db_index=True)
    body = HTMLField(verbose_name='основной текст', 
                            null=True, 
                            blank=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    publish = models.DateTimeField(default=timezone.now,
                                   verbose_name="Публикация")
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name="Создано")
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name="Изменено")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')


    class Meta:
        ordering = ('-publish',)
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})
    
    def get_tags(self):
        return ', '.join([tag.name for tag in self.categories.all()])
        


class Category(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
        ordering = ('id',)
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
    def __str__(self):
        return self.name