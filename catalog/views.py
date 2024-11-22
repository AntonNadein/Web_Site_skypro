from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from catalog.forms import AddProductForm
from catalog.models import Category, Product


class ProductListView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "catalog/product_list.html"


class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "catalog/product_info.html"


class ProductCreateView(CreateView):
    model = Product
    form_class = AddProductForm
    template_name = "catalog/add_product.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = AddProductForm
    template_name = "catalog/add_product.html"
    success_url = reverse_lazy("catalog:product_list")


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"Сообщение: {message} от {name}. Почта для обратной связи: {email}")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class CategoryListView(TemplateView):
    template_name = "catalog/category_list.html"

    def get(self, request, *args, **kwargs):
        category_pk = kwargs.get("pk")
        category = get_object_or_404(Category, pk=category_pk)
        products = Product.objects.filter(category=category)
        context = {"category": category, "products": products}
        return self.render_to_response(context)
