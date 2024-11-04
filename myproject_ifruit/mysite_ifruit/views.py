from django.shortcuts import render

def index(request):
    return render(request, 'mysite_ifruit/index.html')  # Здесь будет ваш шаблон