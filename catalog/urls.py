from django.urls import path

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("product_info/<int:product_pk>", views.product_info, name="product_info"),
    path("contacts/", views.contacts, name="contacts"),
    path("category/<int:category_pk>/", views.category_list, name="category"),
    path("add_product/", views.add_product, name="add_product"),
]
