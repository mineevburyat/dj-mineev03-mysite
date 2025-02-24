# Generated by Django 5.1.4 on 2025-02-22 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0010_alter_skill_unique_together"),
    ]

    operations = [
        migrations.AddField(
            model_name="activitetype",
            name="skills",
            field=models.ManyToManyField(to="service.skill", verbose_name="требования"),
        ),
        migrations.AlterField(
            model_name="skill",
            name="skilltype",
            field=models.CharField(
                choices=[
                    ("knowledge", "знать"),
                    ("ability", "уметь"),
                    ("experience", "навык"),
                ],
                default="knowledge",
                max_length=10,
            ),
        ),
    ]
