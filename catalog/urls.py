from django.urls import path

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name

urlpatterns = [path("home/", views.home_page, name="home_page"), path("contacts/", views.contacts, name="contacts")]
