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
    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"

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
    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"


class CompetetionType(models.Model):
    cod = models.CharField(verbose_name='код типа компетенции',
                           max_length=10,
                           unique=True)
    transcript = models.CharField(verbose_name='расшифровка типа',
                                  max_length=28)
    class Meta:
        verbose_name = "тип компетенции"
        verbose_name_plural = "типы компетенций"

    def __str__(self):
        return self.transcript

class ActiviteType(models.Model):
    name = models.CharField(verbose_name='вид деятельности',
                            max_length=120)
    skills = models.ManyToManyField('Skill',
                                    verbose_name='требования')
    class Meta:
        verbose_name = "вид деятельности"
        verbose_name_plural = "виды деятельности"

    def __str__(self):
        return self.name
    
    
class Competetion(models.Model):
    cod = models.CharField(verbose_name='числовой код компетенции',
                           max_length=10,
                           unique=True)
    typecompetetion = models.ForeignKey(CompetetionType,
                                        on_delete=models.PROTECT,
                                        verbose_name='вид компетенции',
                                        )
    description = models.CharField(verbose_name='описание',
                            max_length=190)
    activite = models.ForeignKey(ActiviteType,
                                 on_delete=models.PROTECT,
                                 verbose_name='вид деятельности',
                                 blank=True,
                                 null=True)
    class Meta:
        verbose_name = "компетенция"
        verbose_name_plural = "компетенции"
    
    def __str__(self):
        return f"{self.typecompetetion} {self.cod}"
    
class Skill(models.Model):
    TYPESKILL_CHOICES = (
        ('knowledge', 'знать'),
        ('ability', 'уметь'),
        ('experience', 'навык'),
    )
    skilltype = models.CharField(
        max_length=10, choices=TYPESKILL_CHOICES, default='knowledge')
    title = models.CharField(verbose_name='требование к скилу')
    class Meta:
        verbose_name = "скилл"
        verbose_name_plural = "скилы"
        unique_together = [["skilltype", "title"]]

    def __str__(self):
        return f"{self.get_skilltype_display()} '{self.title}'"
