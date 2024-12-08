# Generated by Django 5.1.4 on 2024-12-07 14:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=150,
                        null=True,
                        verbose_name="Заголовок",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True,
                        max_length=150,
                        null=True,
                        unique=True,
                        verbose_name="URL",
                    ),
                ),
                (
                    "body",
                    models.TextField(
                        blank=True, null=True, verbose_name="основной текст"
                    ),
                ),
                (
                    "publish",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Опубликовать"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создано"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="Изменено"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("draft", "Черновик"), ("published", "Опубликован")],
                        default="draft",
                        max_length=10,
                    ),
                ),
                (
                    "categories",
                    models.ManyToManyField(related_name="posts", to="blog.category"),
                ),
            ],
            options={
                "ordering": ("-publish",),
            },
        ),
    ]
