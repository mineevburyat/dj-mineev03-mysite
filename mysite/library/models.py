from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
import uuid
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from blog.models import CategoryTree
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager


class Genre(models.Model):
    name = models.CharField(max_length=200, 
                            help_text="жанр книги согласно https://blog.selfpub.ru/genresofliterature",
                            unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message = "Жанр уже существует"
            ),
        ]
        verbose_name = "жанр"
        verbose_name_plural = "жанры"

class Book(models.Model):
    """Книга как продукт автора и её описание"""
    title = models.CharField(max_length=120,
                             verbose_name='Название',
                             db_index=True)
    authors = models.CharField(verbose_name='авторы',
                               max_length=100)
    summary = HTMLField(max_length=1000, 
                        help_text="Краткое описание книги")
    genre = models.ForeignKey(Genre,
                              help_text="Выберите жанр",
                              on_delete=models.PROTECT,
                              verbose_name='жанр',
                              related_name='genre_books',
                              )
    cataloge = models.CharField(verbose_name='код каталога',
                                help_text='код каталога или классификатора (ББК, УДК)',
                                blank=True,
                                null=True)
    category = TreeForeignKey(CategoryTree, 
                                on_delete=models.PROTECT, 
                                verbose_name='Категория',
                                related_name='category_books',
                                )
    tags = TaggableManager(blank=True)
    class Meta:
        ordering = ('title',)
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.pk)])
       

class BookInstance(models.Model):
    """
    Абстрактный класс для экземпляра книги (твердой или электронной)
    Связь с книгой.
    Технические характеристики.
    """
    id = models.UUIDField(primary_key=True, 
                          default=uuid.uuid4, 
                          help_text="Уникальный ID")
    book = models.ForeignKey('Book', 
                             on_delete=models.SET_NULL, 
                             null=True)
    publishing_house = models.CharField(verbose_name='издательство',
                                        max_length=25,
                                        blank=True,
                                        null=True)
    publishing_year = models.PositiveIntegerField(verbose_name='год издания',
                                          blank=True, null=True)
    isbn = models.CharField('ISBN',
                            max_length=13, 
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>',
                            blank=True,
                            null=True)
    class Meta:
        abstract = True

    def __str__(self):
        return '%s (%s)' % (self.id,self.book.title)

class HardBookInstance(BookInstance):
    """
    существующий твердый экземпляр.
    на месте ли, когда и кому дан на руки
    """
    date_of_loan = models.DateField(null=True, blank=True,
                                help_text="дата когда взяли почитать")
    LOAN_STATUS = (
        ('site', 'На полке'),
        ('loan', 'на руках'),
        ('lost', 'утерян'),
    )
    status = models.CharField(max_length=5, 
                              choices=LOAN_STATUS, 
                              blank=True, 
                              default='site', 
                              help_text='доступность книги')
    class Meta:
        ordering = ["date_of_loan"]
        verbose_name = "экземпляр книги"
        verbose_name_plural = "экземпляры книг"

   
class eBookInstance(BookInstance):
    """
    существующий электронный экземпляр
    связь с книгой
    ссылка на книгу
    сколько раз скачивали
    """
    url = models.URLField(verbose_name='ссылка на книгу',
                          help_text="ссылка на яндекс диск",
                          unique=True)
    count_load = models.PositiveIntegerField('количество скачиваний', 
                                             default=0)
    class Meta:
        ordering = ["book"]
        verbose_name = "электронный экземпляр"
        verbose_name_plural = "электронные экземпляры"
        constraints = [
            UniqueConstraint(
                Lower('url'),
                name='gurl_to_ebook_unique',
                violation_error_message = "такая электронная книга уже есть"
            ),
        ]

 