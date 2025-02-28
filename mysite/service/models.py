from django.db import models

class Course(models.Model):
    title = models.CharField(verbose_name='название курса',
                             max_length=120)
    description = models.TextField(verbose_name='краткое описание, цель',
                                   blank=True,
                                   null=True)
    icon = models.ImageField(verbose_name='иконка')
    file = models.FileField(verbose_name='рабочая программа',
                            blank=True,
                            null=True)
    skills = models.ManyToManyField('Skill',
                                    verbose_name='требуемые результаты')
    
    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"

    def __str__(self):
        return "курс" + self.title
    
    def chapter_count(self):
        return self.chapters.all().count()

    def lesson_count(self):
        return sum([chapter.lesson_count() for chapter in self.chapters.all()])


class ChapterLesson(models.Model):
    number = models.PositiveSmallIntegerField(verbose_name='номер главы')
    title = models.CharField(verbose_name='название раздела',
                             max_length=100)
    course = models.ForeignKey(Course,
                               verbose_name='курс',
                               on_delete=models.PROTECT,
                               related_name='chapters')
    description = models.TextField(verbose_name='описание раздела')

    def __str__(self):
        return f"{self.number} {self.title}"
    
    def lesson_count(self):
        return self.lessons.all().count()
    
class Lesson(models.Model):
    TYPELESSON_CHOICES = (
        ('remember', 'вспомнить материал'),
        ('newskill', 'узнать новое'),
        ('practice', 'практика'),
        ('selfwork', 'самостоятельная работа'),
    )
    num = models.PositiveSmallIntegerField(verbose_name='номер урока',
                                           default=1)
    title = models.CharField(verbose_name='тема урока')
    description = models.TextField(verbose_name='краткое содержимое',
                                   blank=True,
                            null=True)
    content = models.TextField(verbose_name='содержимое урока',
                               blank=True,
                               null=True)
    chapter = models.ForeignKey(ChapterLesson,
                               on_delete=models.PROTECT,
                               verbose_name='раздел курса',
                               related_name='lessons',
                               blank=True,
                            null=True)
    typelesson = models.CharField(verbose_name='тип урока',
                                  max_length=10, 
                                  choices=TYPELESSON_CHOICES, 
                                  default='newskill')
    hour = models.PositiveSmallIntegerField(verbose_name='к-во часов',
                                            default=1)
    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"

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

# #########################################
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
    

