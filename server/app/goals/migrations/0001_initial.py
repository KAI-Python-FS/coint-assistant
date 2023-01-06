# Generated by Django 4.1.4 on 2022-12-09 11:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Goal",
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
                        max_length=255, verbose_name="Название цели"
                    ),
                ),
                (
                    "user",
                    models.ManyToManyField(
                        to=settings.AUTH_USER_MODEL, verbose_name="Покупатель"
                    ),
                ),
            ],
            options={
                "verbose_name": "Цель",
                "verbose_name_plural": "Цели",
            },
        ),
    ]
