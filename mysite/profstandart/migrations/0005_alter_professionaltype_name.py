# Generated by Django 5.1.4 on 2025-02-24 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profstandart", "0004_alter_professionalarea_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="professionaltype",
            name="name",
            field=models.CharField(
                max_length=500, unique=True, verbose_name="тип профессии"
            ),
        ),
    ]
