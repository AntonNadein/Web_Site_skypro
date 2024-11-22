from django.urls import path

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product_list"),
    path("product_info/<int:pk>/", views.ProductDetailView.as_view(), name="product_info"),
    path("product/new/", views.ProductCreateView.as_view(), name="add_product"),
    path("product/update/<int:pk>/", views.ProductUpdateView.as_view(), name="update_product"),
    path("product/delete/<int:pk>/", views.ProductDeleteView.as_view(), name="delete_product"),
    path("product/contacts/", views.ContactsView.as_view(), name="contacts"),
    path("category/<int:pk>/", views.CategoryListView.as_view(), name="category"),
]
