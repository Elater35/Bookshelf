from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL-слаг")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        ordering = ["name"]


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Назва книги")
    author = models.CharField(max_length=100, verbose_name="Автор")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    description = models.TextField(null=True, blank=True, verbose_name="Опис")
    stock = models.IntegerField(default=0, verbose_name="Кількість на складі")

    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='books', verbose_name="Категорія")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ["title"]
