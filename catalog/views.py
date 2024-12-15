from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from catalog.forms import AddProductForm
from catalog.models import Category, Product


class ModerationProductView(LoginRequiredMixin, View):

    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if not request.user.has_perm("catalog.can_unpublish_product"):
            return HttpResponseForbidden("У вас нет прав для снятия публикации.")

        product.is_published = False
        product.save()

        return redirect("catalog:product_info", pk=pk)


class ProductListView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "catalog/product_list.html"


class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "catalog/product_info.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = AddProductForm
    template_name = "catalog/add_product.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        if request.user != product.owner and not request.user.has_perm("catalog.delete_product"):
            return HttpResponseForbidden("У вас нет прав для удаления данного продукта.")

        return super().post(request, *args, **kwargs)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = AddProductForm
    template_name = "catalog/add_product.html"
    success_url = reverse_lazy("catalog:product_list")

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        if request.user != product.owner:
            return HttpResponseForbidden("У вас нет прав для редактирования продукта.")

        return super().post(request, *args, **kwargs)


class ContactsView(LoginRequiredMixin, TemplateView):
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
