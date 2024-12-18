from django.db import models

from users.models import ModelUser


class Product(models.Model):
    PUBLISH = True
    DRAFT = False

    STATUS = [(PUBLISH, "Опубликовано"), (DRAFT, "Черновик")]

    name = models.CharField(max_length=200, verbose_name="Наименование")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to="images/product", null=True, blank=True, verbose_name="Изображение")
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="category", verbose_name="Категория"
    )
    price = models.FloatField(verbose_name="Цена за единицу")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, null=True, blank=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(choices=STATUS, default=True, verbose_name="Статус")
    owner = models.ForeignKey(
        ModelUser, on_delete=models.CASCADE, null=True, blank=True, related_name="products", verbose_name="Владелец"
    )

    def __str__(self):
        return f"{self.name} {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price", "created_at"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
