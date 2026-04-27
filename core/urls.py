from django.contrib import admin
from django.urls import path, include  # Обов'язково додаємо include сюди!

urlpatterns = [
    path('admin/', admin.site.urls),
    # Підключаємо всі маршрути з нашого додатка news
    path('news/', include('news.urls')), 
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('auth/', include('accounts.urls')), # Підключаємо маршрути авторизації
]