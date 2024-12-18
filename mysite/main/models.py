from django.db import models
# from django.date

# Create your models here.
class Menu(models.Model):
    name = models.CharField('Название', max_length=50)
    url = models.CharField('Ссылка', max_length=50)
    position = models.PositiveIntegerField('Позиция', default=1)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('position',)
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

class UsefulLink(models.Model):
    name = models.CharField(max_length=60)
    url = models.URLField()
    description = models.CharField(max_length=300,
                                   blank=True)
    added = models.DateTimeField(auto_now_add=True)
    usefulness = models.IntegerField(default=0)  # Поле полезности

    class Meta:
        verbose_name = 'Полезная ссылка'
        verbose_name_plural = 'Полезные ссылки'

    # def 

    def __str__(self):
        return f"{self.name} ({self.url})"
    