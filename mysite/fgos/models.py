from django.db import models

# Create your models here.

class Science(models.Model):
    name = models.CharField(verbose_name='название науки')
    class Meta:
        verbose_name = 'наука'
        verbose_name_plural = 'науки'
    def __str__(self):
        return self.name
    


class GroupScience(models.Model):
    cod = models.CharField(verbose_name='код',
                           max_length=9,
                           unique=True)
    title = models.CharField(verbose_name='название группы',
                             unique=True)
    science = models.ForeignKey(Science,
                                verbose_name='наука',
                                on_delete=models.PROTECT,
                                related_name='groups')
    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'

    def __str__(self):
        return f"{self.cod} {self.title}"

class Speciality(models.Model):
    cod = models.CharField(verbose_name='код специальности',
                           max_length=9,
                           unique=True)
    title = models.CharField(verbose_name='название специальности',
                             unique=True)
    group = models.ForeignKey(GroupScience,
                              verbose_name='группа специальностей',
                              on_delete=models.PROTECT,
                              related_name='specialitys')
    class Meta:
        verbose_name = 'специальность'
        verbose_name_plural = 'специальности'

    def __str__(self):
        return f"{self.cod} {self.title} ({self.group.title} - {self.group.science.name})"

class FGOS(models.Model):
    title = models.CharField(verbose_name='название ФГОС',
                             max_length=200)
    file = models.FileField(verbose_name='файл ФГОС',
                            upload_to='fgos/')
    date = models.DateField(verbose_name='дата приказа')
    number = models.CharField(verbose_name='номер приказа',
                              max_length=6)
    speciality = models.ForeignKey(Speciality,
                                   verbose_name='специальность',
                                   on_delete=models.PROTECT,
                                   blank=True,
                                   null=True)
    class Meta:
        verbose_name = 'образовательный стандарт'
        verbose_name_plural = 'образовательные стандарты'

    def __str__(self):
        if self.speciality:
            return f"{self.title} {self.speciality.title}"
        return f"{self.title}"