from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

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
    category = TreeForeignKey('CategoryTree', 
                                on_delete=models.PROTECT, 
                                related_name='posts', 
                                verbose_name='Категория') 
    publish = models.DateTimeField(default=timezone.now,
                                   verbose_name="Публикация")
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name="Создано")
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name="Изменено")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')
    tags = TaggableManager()
    class Meta:
        ordering = ('-publish',)
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'slug': self.slug})
    
    def get_tags(self):
        return ''
        # return ', '.join([tag.title for tag in self.category.all()])
        

   
class CategoryTree(MPTTModel):
    title = models.CharField(max_length=30,
                            unique=True,
                            verbose_name='название категории')
    parent = TreeForeignKey('self', 
                            on_delete=models.PROTECT, 
                            null=True, 
                            blank=True, 
                            related_name='children',
                            verbose_name='Родительская категория')
    slug = models.SlugField()
    order = models.IntegerField(verbose_name='сортировка',
                                default=1,
                                help_text='значимость категории')
    description = models.TextField(verbose_name='описание',
                                   max_length=60,
                                   blank=True,
                                   null=True)

    class MPTTMeta:
        order_insertion_by = ('order', )
    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        constraints = [
            UniqueConstraint(
                Lower('title'),
                name='category_title_case_insensitive_unique',
                violation_error_message = "Категория уже существует"
            ),
        ]
        ordering = ('order',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:listposts', args=[str(self.slug)])
    
    def get_posts_count(self):
        sum = self.posts.count()
        for child in self.get_children():
            sum += child.posts.count()
        return sum
    get_posts_count.short_description = 'к-во статей'
    
    def is_description(self):
        return bool(self.description)
    is_description.boolean = True
    is_description.short_description = 'описание'