from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')


def test(request):
    return render(request, 'core/example.html')


def table(request):
    return render(request, 'core/table.html')
