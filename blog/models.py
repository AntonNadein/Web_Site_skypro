from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    blog_text = models.TextField(verbose_name="Содержимое статьи")
    image = models.ImageField(upload_to="images/blog", null=True, blank=True, verbose_name="Превью (изображение)")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=True, verbose_name="Опубиковать")
    view_count = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статью"
        verbose_name_plural = "Статьи"
        ordering = ["title", "created_at"]
