from django.contrib import admin
from django.urls import path, include  # Импортируйте функцию include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mysite_ifruit.urls')),  # Подключите маршруты вашего приложения
]