from django.http import HttpResponse
from django.shortcuts import redirect, render

from catalog.forms import AddProductForm
from catalog.models import Category, Product


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "catalog/product_list.html", context=context)


def product_info(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    context = {"product": product}
    return render(request, "catalog/product_info.html", context=context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"Сообщение: {message} от {name}. Почта для обратной связи: {email}")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "catalog/contacts.html")


def category_list(request, category_pk):
    category = Category.objects.get(pk=category_pk)
    products = Product.objects.filter(category=category)
    context = {"category": category, "products": products}
    return render(request, "catalog/category_list.html", context=context)


def add_product(request):
    form = AddProductForm(request.POST)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, "catalog/add_product.html", context=context)
