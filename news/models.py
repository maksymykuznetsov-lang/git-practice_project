from django.db import models
from django.contrib.auth.models import User # Імпортуємо стандартну таблицю користувачів Django

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    description = models.TextField(blank=True, verbose_name="Опис")

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст новини")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles', verbose_name="Категорія")
    
    # Прив'язування статті до конкретного автора
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', verbose_name="Автор", null=True, blank=True)
    
    image = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Фото статті")
    is_published = models.BooleanField(default=True, verbose_name="Опубліковано")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    def __str__(self):
        return self.title

class ArticleFile(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='files', verbose_name="До статті")
    file = models.FileField(upload_to='files/', verbose_name="Файл (PDF)")
    
    def __str__(self):
        return f"Файл до новини: {self.article.title}"

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name="До статті")
    author_name = models.CharField(max_length=100, verbose_name="Ім'я автора")
    text = models.TextField(verbose_name="Текст коментаря")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата написання")

    def __str__(self):
        return f"Коментар від {self.author_name}"