from django.shortcuts import render


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def index(request):
    return render(request, 'index.html')


def services(request):
    return render(request, 'services.html')
