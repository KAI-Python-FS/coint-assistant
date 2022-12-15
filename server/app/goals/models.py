from datetime import date

from django.contrib.auth import get_user_model
from django.db import models

from server.app.goals import enums


User = get_user_model()


class Goal(models.Model):
    """Модель Цели"""

    name = models.CharField(
        max_length=255,
        verbose_name="Название цели"
    )
    description = models.TextField(
        null=True,
        verbose_name="Описание",
    )
    user = models.ManyToManyField(
        User,
        verbose_name="Покупатель",
    )
    goal_type = models.CharField(
        choices=enums.GoalTypeEnum.choices,
        default=enums.GoalTypeEnum.SPENDING,
        max_length=32,
        verbose_name="Категория операций цели",
    )
    category = models.ForeignKey(
        "operations.Category",
        null=True,
        on_delete=models.CASCADE,
        related_name="goals",
        verbose_name="Категория операций цели",
    )
    start_date = models.DateField(
        default=date.today,
        verbose_name="Дата начала цели",
    )
    finish_date = models.DateField(
        null=True,
        verbose_name="Дата окончания цели",
    )
    state = models.CharField(
        choices=enums.GoalStateEnum.choices,
        default=enums.GoalStateEnum.unknown,
        max_length=32,
        verbose_name="Состояние цели"
    )
    value = models.FloatField(
        null=True,
        verbose_name="Значение цели",
    )
    rule = models.CharField(
        choices=enums.GoalRuleEnum.choices,
        default=enums.GoalRuleEnum.lte,
        max_length=16,
        verbose_name="Правило достижения цели",
    )

    class Meta:
        verbose_name = "Цель"
        verbose_name_plural = "Цели"
