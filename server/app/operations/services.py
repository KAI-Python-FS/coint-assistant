
from server.app.base.exceptions import ValidationException

from .enums import OperationTypeEnum
from .models import Category, Operation


class CategoryService:
    """Класс описания бизнес логики работы с Категориями покупок"""

    @classmethod
    def create(cls, user=None, **category_data) -> Category:
        """Создание категории"""
        category = Category.objects.create(**category_data)
        return category

    @classmethod
    def retrieve_single(cls, category_id: int) -> Category:
        """Получение одной категории"""
        try:
            category = Category.objects.get(category_id)
        except Category.DoesNotExist:
            raise ValidationException(f"Категории с id={category_id} не найдено.")

        return category

    @classmethod
    def update(cls, category_id: int, user=None, **category_data) -> Category:
        """Обновление категории"""
        try:
            category = Category.objects.get(category_id)
        except Category.DoesNotExist:
            raise ValidationException(f"Категории с id={category_id} не найдено.")

        return category

    @classmethod
    def delete(cls, category_id: int) -> bool:
        """Удаление категории"""
        try:
            category = Category.objects.get(category_id)
        except Category.DoesNotExist:
            raise ValidationException(f"Категории с id={category_id} не найдено.")

        category.delete()

        return True

    @classmethod
    def retrieve_list(cls, **filters) -> list[Category | None]:
        """Получение списка категорий согласно фильтрам"""
        return Category.objects.all()


class OperationService:
    """Класс описания бизнес логики работы с операциями пользователя"""

    @classmethod
    def create_operation(cls, user, **operation_data):
        """Создание записи операции пользователя"""

    @classmethod
    def create_spending(cls, user: int, **operation_data):
        """Создание записи траты у пользователя"""
        Operation.objects.create(
            user=user,
            operation_type=OperationTypeEnum.SPENDING,
            **operation_data
        )

    @classmethod
    def create_refill(cls, user: int, **operation_data):
        """Создание записи пополнения у пользователя"""
        Operation.objects.create(
            user=user,
            operation_type=OperationTypeEnum.REFILL,
            **operation_data
        )