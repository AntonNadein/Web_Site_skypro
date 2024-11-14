from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to="images/product", null=True, blank=True, verbose_name="Изображение")
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="category", verbose_name="Категория"
    )
    price = models.FloatField(verbose_name="Цена за единицу")
    created_at = models.DateField(auto_now=True, verbose_name="Дата создания")
    updated_at = models.DateField(null=True, blank=True, verbose_name="Дата изменения")

    def __str__(self):
        return f"{self.name} {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price", "created_at"]


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
