# Generated by Django 4.1.4 on 2022-12-13 07:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

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
                (
                    "name",
                    models.CharField(max_length=64, verbose_name="Название категории"),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Operation",
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
                ("name", models.TextField(verbose_name="Наименование операции")),
                (
                    "description",
                    models.TextField(null=True, verbose_name="Описание операции"),
                ),
                (
                    "operation_at",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="Дата операции"
                    ),
                ),
                (
                    "operation_type",
                    models.CharField(
                        choices=[("Трата", "Spending"), ("Пополнение", "Refill")],
                        max_length=64,
                        verbose_name="Тип операции",
                    ),
                ),
                ("cost", models.FloatField(verbose_name="Стоимость")),
                (
                    "category",
                    models.ManyToManyField(
                        null=True,
                        to="operations.category",
                        verbose_name="Категория операции",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Покупатель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Операция",
                "verbose_name_plural": "Операции",
            },
        ),
    ]
