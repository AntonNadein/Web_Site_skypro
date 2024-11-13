from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product, Category


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'catalog/product_list.html', context=context)


def product_info(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    context = {
        'product': product
    }
    return render(request, 'catalog/product_info.html', context=context)


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
    context = {
        'category': category,
        'products': products
    }
    return render(request, "catalog/category_list.html", context=context)
