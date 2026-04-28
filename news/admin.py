from django.contrib import admin
from .models import Category, Article, Comment, ArticleFile

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(ArticleFile)

