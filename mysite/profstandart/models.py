from django.db import models

# Create your models here.
class ProfessionalArea(models.Model):
    name = models.CharField(verbose_name='сфера деятельности',
                            max_length=164,
                            unique=True)
    
    def __str__(self):
        return f'сфера деятельности {self.name}'
    
class ProfessionalType(models.Model):
    name = models.CharField(verbose_name='тип профессии',
                            max_length=700,
                            unique=True)
    
    def __str__(self):
        return f'тип профессии {self.name}'
    
class ProfStandart(models.Model):
    regnum = models.PositiveIntegerField(verbose_name='регистрационный номер')
    cod = models.CharField(verbose_name='код профстандарта',
                           unique=True)
    title = models.CharField(verbose_name='название профессии',
                             unique=True,
                             max_length=250)
    numorder = models.CharField(verbose_name='номер приказа',
                                max_length=25)
    dateorder = models.DateField(verbose_name='дата приказа')
    proftype = models.ForeignKey(ProfessionalType,
                                 verbose_name='тип профессии',
                                 on_delete=models.PROTECT,
                                 related_name='profstandarts')
    profarea = models.ForeignKey(ProfessionalArea,
                                 verbose_name='сфера деятельности',
                                 on_delete=models.PROTECT,
                                 related_name='profstandarts')
    
    def __str__(self):
        return self.title