from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
import uuid
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

class Genre(models.Model):
    name = models.CharField(max_length=200, 
                            help_text="жанр книги (научпоп, фантастика и пр.)",
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
    title = models.CharField(max_length=120,
                             verbose_name='Название',
                             db_index=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = HTMLField(max_length=1000, 
                        help_text="Краткое описание книги")
    isbn = models.CharField('ISBN',
                            max_length=13, 
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, 
                                   help_text="Выберите подходящие жанры")
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
    class Meta:
        verbose_name = "книга"
        verbose_name_plural = "книги"
        
    
class BookInstance(models.Model):
    """
    существующий экземпляр
    """
    id = models.UUIDField(primary_key=True, 
                          default=uuid.uuid4, 
                          help_text="Уникальный ID")
    book = models.ForeignKey('Book', 
                             on_delete=models.SET_NULL, 
                             null=True)
    imprint = models.CharField(max_length=200,
                               help_text="издательство, год печати, номер издания, переводчик")
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


    def __str__(self):
        return '%s (%s)' % (self.id,self.book.title)
    
class eBookInstance(models.Model):
    """
    существующий электронный экземпляр
    """
    id = models.UUIDField(primary_key=True, 
                          default=uuid.uuid4, 
                          help_text="Уникальный ID")
    book = models.ForeignKey('Book', 
                             on_delete=models.SET_NULL, 
                             null=True)
    imprint = models.CharField(max_length=200,
                               help_text="издательство, год печати, номер издания, переводчик")
    url = models.URLField(help_text="ссылка на яндекс диск", unique=True)
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

    def __str__(self):
        return '%s (%s)' % (self.id,self.book.title)
    
class Author(models.Model):
    name = models.CharField('Полное имя',
                            max_length=150,
                            unique=True,
                            db_index=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s' % (self.name)
    
    class Meta:
        verbose_name = "автор"
        verbose_name_plural = "авторы"
