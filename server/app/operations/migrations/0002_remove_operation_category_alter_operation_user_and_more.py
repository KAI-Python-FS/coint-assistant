# Generated by Django 4.1.4 on 2022-12-14 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("operations", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="operation",
            name="category",
        ),
        migrations.AlterField(
            model_name="operation",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="operations",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Покупатель",
            ),
        ),
        migrations.AddField(
            model_name="operation",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="operations",
                to="operations.category",
                verbose_name="Категория операции",
            ),
        ),
    ]
