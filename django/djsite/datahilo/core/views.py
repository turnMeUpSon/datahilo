from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def testing(request):
    return render(request, 'core/test.html')