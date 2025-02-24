# Generated by Django 5.1.4 on 2024-12-07 17:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ("id",),
                "verbose_name": "категория",
                "verbose_name_plural": "категории",
            },
        ),
        migrations.AlterModelOptions(
            name="post",
            options={
                "ordering": ("-publish",),
                "verbose_name": "статья",
                "verbose_name_plural": "статьи",
            },
        ),
        migrations.AlterField(
            model_name="post",
            name="publish",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Публикация"
            ),
        ),
    ]
