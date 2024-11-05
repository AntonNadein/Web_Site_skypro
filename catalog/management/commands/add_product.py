from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Add test product to the database'

    def handle(self, *args, **kwargs):

        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='Ноутбук', description='Мобильный компьютер')

        products = [
            {'name': 'Acer', 'description': '1904-01-01', 'category': category, 'price': 75000.0},
            {'name': 'MSI', 'category': category, 'price': 75000.0},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Успешно добавлен в БД: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Не смог добавить в БД: {product.name}'))
