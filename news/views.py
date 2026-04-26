from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm

# 1. Список усіх новин
def article_list_view(request):
    articles = Article.objects.all()
    context = {"title": "Список новин", "articles": articles}
    return render(request, 'news/article_list.html', context=context)

# 2. Перегляд однієї новини
def article_detail_view(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {"title": article.title, "article": article}
    return render(request, 'news/article_detail.html', context=context)

# 3. Створення новини
def article_create_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    
    context = {"title": "Додати новину", "form": form}
    return render(request, 'news/article_form.html', context=context)

# 4. Редагування новини
def article_update_view(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', article_id=article.id)
    else:
        form = ArticleForm(instance=article)
    
    context = {"title": "Редагувати новину", "form": form}
    return render(request, 'news/article_form.html', context=context)

# 5. Видалення новини
def article_delete_view(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    
    context = {"title": "Видалення новини", "article": article}
    return render(request, 'news/article_confirm_delete.html', context=context)