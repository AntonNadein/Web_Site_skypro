from django.urls import path

from . import views
from .apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path("", views.BlogListView.as_view(), name="blog_list"),
    path("detail/<int:pk>/", views.BlogDetailView.as_view(), name="blog_detail"),
    path("create/", views.BlogCreateView.as_view(), name="blog_edit"),
    path("update/<int:pk>/", views.BlogUpdateView.as_view(), name="blog_update"),
    path("delete/<int:pk>/", views.BlogDeleteView.as_view(), name="blog_delete"),
]
