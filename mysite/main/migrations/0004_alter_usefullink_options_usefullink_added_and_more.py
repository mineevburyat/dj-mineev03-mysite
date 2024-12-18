# Generated by Django 5.1.4 on 2024-12-13 09:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_usefullink"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="usefullink",
            options={
                "verbose_name": "Полезная ссылка",
                "verbose_name_plural": "Полезные ссылки",
            },
        ),
        migrations.AddField(
            model_name="usefullink",
            name="added",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usefullink",
            name="usefulness",
            field=models.IntegerField(default=0),
        ),
    ]
