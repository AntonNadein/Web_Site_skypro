from django.shortcuts import get_object_or_404

from .models import Category, Product


class CategoryService:

    @staticmethod
    def get_category_products(category_pk):
        category = get_object_or_404(Category, pk=category_pk)
        return Product.objects.filter(category=category)
