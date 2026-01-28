from django.shortcuts import render


def home(request):
    context = {
        'title': 'Welcome',
        'message': 'This is a web application',
    }
    return render(request, 'core/home.html', context)


def about(request):
    context = {
        'title': 'About',
        'message': 'Learn more',
    }
    return render(request, 'core/about.html', context)
