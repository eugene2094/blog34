from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Назва")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Опис")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Дата")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    image = models.URLField(default="http://placehold.it/900x300")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"


class PostPhoto(models.Model):
    post = models.ForeignKey(Post, verbose_name="Пост", on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(verbose_name="Картинка", upload_to="Posts_Photos")

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"
