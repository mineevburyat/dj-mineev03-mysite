from django.db import models

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