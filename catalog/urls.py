from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('home_page/', views.home_page, name='home_page')
]