from django.shortcuts import render


def home(request):
    context = {
        'title': 'Welcome to Django Demo',
        'message': 'This is a Django web application built with best practices.',
    }
    return render(request, 'core/home.html', context)


def about(request):
    context = {
        'title': 'About',
        'message': 'Learn more about this Django project.',
    }
    return render(request, 'core/about.html', context)
