from django.shortcuts import render

def indexe(request):
    return render(request, 'pages/indexe.html.twig')

def index(request):
    return render(request, 'pages/index.html.twig')

def eleveaccueil(request):
    return render(request, 'pages/eleveaccueil.html.twig')

# Create your views here.
