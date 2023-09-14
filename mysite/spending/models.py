from django.db import models
from datetime import date


class Category(models.Model):

    name = models.CharField(max_length=64, verbose_name="Название категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name}"


class Operation(models.Model):
    name = models.CharField(
        verbose_name="Наименование операции",
        max_length=80
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание операции",
    )
    cost = models.FloatField(
        verbose_name="Стоимость",
    )
    data_created = models.DateTimeField(
        verbose_name='дата и время',
        auto_now_add=True
    )
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="operations",
        verbose_name="Категория операции",
    )

    class Meta:
        verbose_name = "Операция"
        verbose_name_plural = "Операции"

    def __str__(self):
        return f"{self.name}"


class GoalType(models.TextChoices):
    """Тип цели"""
    SPENDING = "Трата"
    REFILL = "Пополнение"


class GoalManager(models.Manager):
    def goals(self):
        return self.filter(goal_type=GoalType.REFILL)

    def budgets(self):
        return self.filter(goal_type=GoalType.SPENDING)


class Goal(models.Model):
    """Модель цели траты или пополнения"""
    name = models.CharField(
        max_length=255,
        verbose_name="Название цели",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
    )
    goal_type = models.CharField(
        choices=GoalType.choices,
        default=GoalType.SPENDING,
        max_length=22,
        verbose_name="Тип операций цели",
    )
    start_date = models.DateField(
        default=date.today,
        verbose_name="Дата начала цели",
    )
    finish_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата окончания цели",
    )
    value = models.FloatField(
        verbose_name="Значение цели",
    )
    objects = GoalManager()

    class Meta:
        verbose_name = "Цель"
        verbose_name_plural = "Цели"
