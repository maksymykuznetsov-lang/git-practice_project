from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    description = models.TextField(blank=True, verbose_name="Опис")

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст новини")
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles', verbose_name="Категорія")
    
    is_published = models.BooleanField(default=True, verbose_name="Опубліковано")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name="До статті")
    author_name = models.CharField(max_length=100, verbose_name="Ім'я автора")
    text = models.TextField(verbose_name="Текст коментаря")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата написання")

    def __str__(self):
        return f"Коментар від {self.author_name}"