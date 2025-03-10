from django.test import TestCase

from catalog.models import Category, Product


class ModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Телефоны",
            description="Вы сами знаете что это",
        )

        self.product = Product.objects.create(
            name="Lg 500",
            category=self.category,
            price=200
        )

    def test_category_str(self):
        """ Тест строкового представления категории """
        self.assertEqual(str(self.category), "Телефоны")

    def test_product_str(self):
        """ Тест строкового представления продукта """
        self.assertEqual(str(self.product), "Lg 500 200")

    def test_category_product(self):
        """ Тест связи продукта и категории """
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.category.category.first(), self.product)
