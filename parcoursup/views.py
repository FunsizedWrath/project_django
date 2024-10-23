from django.shortcuts import render

def indexe(request):
    return render(request, 'indexe.html.twig')

def index(request):
    return render(request, 'index.html.twig')

# Create your views here.
