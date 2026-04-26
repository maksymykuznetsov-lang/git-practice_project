from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list_view, name='article_list'),
    path('create/', views.article_create_view, name='article_create'),
    path('<int:article_id>/', views.article_detail_view, name='article_detail'),
    path('<int:article_id>/update/', views.article_update_view, name='article_update'),
    path('<int:article_id>/delete/', views.article_delete_view, name='article_delete'),
]