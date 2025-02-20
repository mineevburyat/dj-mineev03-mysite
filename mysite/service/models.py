from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(verbose_name='название курса',
                             max_length=120)
    description = models.TextField(verbose_name='краткое описание, цель')
    icon = models.ImageField(verbose_name='иконка')
    file = models.FileField(verbose_name='рабочая программа',
                            blank=True,
                            null=True)

    def __str__(self):
        return "курс" + self.title
    
    def lesson_count(self):
        return self.lessons.all().count()

class Lesson(models.Model):
    title = models.CharField(verbose_name='тема урока')
    content = models.TextField(verbose_name='содержимое урока')
    course = models.ForeignKey(Course,
                               on_delete=models.PROTECT,
                               verbose_name='курс',
                               related_name='lessons')
    
class Competetion(models.Model):
    cod = models.CharField(verbose_name='код компетенции',
                           max_length=10,
                           unique=True)
    transcript = models.CharField(verbose_name='расшифровка кода',
                                  max_length=28,
                                  blank=True,
                                  null=True)
    description = models.CharField(verbose_name='описание',
                            max_length=160)
    
