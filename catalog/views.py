from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, "catalog/home_page.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"Сообщение: {message} от {name}. Почта для обратной связи: {email}")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "catalog/contacts.html")
