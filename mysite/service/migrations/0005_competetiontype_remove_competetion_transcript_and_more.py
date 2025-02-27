# Generated by Django 5.1.4 on 2025-02-22 06:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0004_competetion_transcript"),
    ]

    operations = [
        migrations.CreateModel(
            name="CompetetionType",
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
                    "cod",
                    models.CharField(
                        max_length=10, unique=True, verbose_name="код типа компетенции"
                    ),
                ),
                (
                    "transcript",
                    models.CharField(max_length=28, verbose_name="расшифровка типа"),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="competetion",
            name="transcript",
        ),
        migrations.AlterField(
            model_name="competetion",
            name="cod",
            field=models.CharField(
                max_length=10, unique=True, verbose_name="числовой код компетенции"
            ),
        ),
        migrations.AddField(
            model_name="competetion",
            name="typecompetetion",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="service.competetiontype",
            ),
        ),
    ]
