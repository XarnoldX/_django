from django.shortcuts import render
from django.http import Http404

def index(request):
    return render(request, 'myapp/index.html')

def test(request):
    return render(request, 'myapp/test.html')
