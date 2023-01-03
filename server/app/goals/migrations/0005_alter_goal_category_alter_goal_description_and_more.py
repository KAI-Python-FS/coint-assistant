# Generated by Django 4.1.4 on 2022-12-29 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("operations", "0003_alter_operation_cost"),
        ("goals", "0004_alter_goal_rule_remove_goal_user_goal_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="goal",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="goals",
                to="operations.category",
                verbose_name="Категория операций цели",
            ),
        ),
        migrations.AlterField(
            model_name="goal",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="goal",
            name="finish_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="Дата окончания цели"
            ),
        ),
        migrations.AlterField(
            model_name="goal",
            name="value",
            field=models.FloatField(verbose_name="Значение цели"),
            preserve_default=False,
        ),
    ]
