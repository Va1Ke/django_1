from django.shortcuts import render
main = {'title': 'Main'}
about1 = {'about': 'About'}

def index(request):
    return render(request, 'main/index.html', main)

def about(request):
    return render(request, 'main/about.html', about1)