from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "is_published", "title", "view_count", "image", "blog_text")
    list_filter = (
        "title",
        "is_published",
    )
    search_fields = ("title", "blog_text")
