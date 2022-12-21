
from django.core.exceptions import FieldDoesNotExist

from .models import Category, Operation


class CategoryService:
    """Класс описания бизнес логики работы с Категориями покупок"""

    def create(self, **category_data) -> Category:
        """Создание категории"""
        category = Category.objects.create(**category_data)
        return category

    def retrieve_single(self, category_id: int) -> Category | None:
        """Получение одной категории"""
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            return None

        return category

    def update(self, category_id: int, **category_data) -> Category | None:
        """Обновление категории"""
        category = self.retrieve_single(category_id)
        if not category:
            return None

        category.name = category_data.pop("name")
        category.save()

        return category

    def delete(self, category_id: int) -> bool | None:
        """Удаление категории"""
        category = self.retrieve_single(category_id)
        if not category:
            return None

        category.delete()

        return True

    @classmethod
    def retrieve_list(cls, **filters) -> list[Category | None]:
        """Получение списка категорий согласно фильтрам"""
        return Category.objects.filter(**filters).all()


class OperationService:
    """Класс описания бизнес логики работы с операциями пользователя"""

    def __init__(self, user) -> None:
        self.user = user
        self.model = Operation

    def create(self, **operation_data) -> Operation:
        """Создание записи операции пользователя"""
        operation = Operation.objects.create(
            user=self.user,
            **operation_data,
        )

        return operation

    def retrieve_list(self, **filters) -> list[Operation | None]:
        """Возвращает список Операций пользователя"""
        qs = Operation.objects.filter(user=self.user)

        for each_filter_key, each_filter_value in filters.items():
            match each_filter_key:
                case "by_operation_type":
                    qs = qs.filter(operation_type=each_filter_value)
                case "by_categories":
                    qs = qs.filter(category_id__in=each_filter_value)
                case "by_operation_start_date":
                    qs = qs.filter(operation_at__gte=each_filter_value)
                case "by_operation_finish_date":
                    qs = qs.filter(operation_at__lte=each_filter_value)
                case _:
                    raise Exception("Неизвестный фильтр")

        return qs.all()

    def retrieve_single(self, operation_id: int) -> Operation | None:
        """Получение одной операции пользователя"""
        try:
            operation = Operation.objects.get(pk=operation_id, user=self.user)
        except Operation.DoesNotExist:
            return None

        return operation

    def update(self, operation_id: int, **operation_data) -> Operation | None:
        """Обновление одной операции"""
        operation = self.retrieve_single(operation_id)
        if not operation:
            return None

        for update_field, update_value in operation_data.items():
            try:
                model_update_field = self.model._meta.get_field(update_field)
            except FieldDoesNotExist:
                break

            setattr(operation, model_update_field.attname, update_value)
        else:
            operation.save()

        return operation

