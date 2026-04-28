from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required  
from django.http import HttpResponseForbidden  
from .models import Article, Category
from .forms import ArticleForm, CommentForm # Додали імпорт форми коментарів

# 1. Список усіх новин + (фільтрація по категорії)
def article_list_view(request):
    categories = Category.objects.all()

    category_id = request.GET.get('category')
    
    if category_id:
        articles = Article.objects.filter(category_id=category_id)
    else:
        articles = Article.objects.all()
        
    context = {
        "title": "Список новин", 
        "articles": articles,
        "categories": categories
    }
    return render(request, 'news/article_list.html', context=context)

# 2. Перегляд однієї новини + додавання коментаря
def article_detail_view(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('/auth/login/') 
            
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author_name = request.user.username
            comment.save()
            return redirect('article_detail', article_id=article.id)
    else:
        form = CommentForm()

    comments = article.comments.all()

    context = {
        "title": article.title, 
        "article": article,
        "comments": comments,
        "form": form
    }
    return render(request, 'news/article_detail.html', context=context)

# 3. Створення новини (Тільки для авторизованих)
@login_required(login_url='/auth/login/')
def article_create_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save() 
            return redirect('article_list')
    else:
        form = ArticleForm()
    
    context = {"title": "Додати новину", "form": form}
    return render(request, 'news/article_form.html', context=context)

# 4. Редагування новини (Тільки для автора статті)
@login_required(login_url='/auth/login/')
def article_update_view(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    
    if article.author != request.user:
        return HttpResponseForbidden("Помилка 403: Ви не можете редагувати чужу статтю!")
        
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', article_id=article.id)
    else:
        form = ArticleForm(instance=article)
    
    context = {"title": "Редагувати новину", "form": form}
    return render(request, 'news/article_form.html', context=context)

# 5. Видалення новини (Тільки для автора статті)
@login_required(login_url='/auth/login/')
def article_delete_view(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    
    if article.author != request.user:
        return HttpResponseForbidden("Помилка 403: Ви не можете видалити чужу статтю!")
        
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    
    context = {"title": "Видалення новини", "article": article}
    return render(request, 'news/article_confirm_delete.html', context=context)