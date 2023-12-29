from django.db import models

# Модель Категории Продуктов (ProductCategory):
#   - Поля:
#     - Название категории (CategoryName)
#     - Описание категории (CategoryDescription)

class ProductCategory(models.Model):
    category_name = models.CharField(max_length=200)
    category_description = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

# Модель Продукта (Product):
#   - Поля:
#     - Название (Name)
#     - Описание (Description)
#     - Категория (Category) - связь с моделью Категорий Продуктов
#     - Цена (Price)
#     - Количество на складе (Quantity)
#     - Дата добавления (DateAdded)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name