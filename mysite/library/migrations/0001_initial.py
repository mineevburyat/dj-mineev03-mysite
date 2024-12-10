# Generated by Django 5.1.4 on 2024-12-08 23:34

import django.db.models.deletion
import tinymce.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("name", models.CharField(max_length=150, verbose_name="Полное имя")),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                (
                    "date_of_death",
                    models.DateField(blank=True, null=True, verbose_name="Died"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
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
                    "name",
                    models.CharField(
                        help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)",
                        max_length=200,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Book",
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
                        db_index=True, max_length=120, verbose_name="Название"
                    ),
                ),
                (
                    "summary",
                    tinymce.models.HTMLField(
                        help_text="Краткое описание книги", max_length=1000
                    ),
                ),
                (
                    "isbn",
                    models.CharField(
                        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>',
                        max_length=13,
                        verbose_name="ISBN",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="library.author",
                    ),
                ),
                (
                    "genre",
                    models.ManyToManyField(
                        help_text="Выберите подходящие жанры", to="library.genre"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BookInstance",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        help_text="Уникальный ID",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "imprint",
                    models.CharField(
                        help_text="издательство, год печати, номер издания, переводчик",
                        max_length=200,
                    ),
                ),
                (
                    "date_of_loan",
                    models.DateField(
                        blank=True, help_text="дата когда взяли почитать", null=True
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("site", "На полке"),
                            ("loan", "на руках"),
                            ("lost", "утерян"),
                        ],
                        default="site",
                        help_text="доступность книги",
                        max_length=5,
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="library.book",
                    ),
                ),
            ],
            options={
                "ordering": ["date_of_loan"],
            },
        ),
        migrations.CreateModel(
            name="eBookInstance",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        help_text="Уникальный ID",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "imprint",
                    models.CharField(
                        help_text="издательство, год печати, номер издания, переводчик",
                        max_length=200,
                    ),
                ),
                ("url", models.URLField(help_text="ссылка на яндекс диск")),
                (
                    "count_load",
                    models.PositiveIntegerField(
                        default=0, verbose_name="количество скачиваний"
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="library.book",
                    ),
                ),
            ],
            options={
                "ordering": ["book"],
            },
        ),
    ]