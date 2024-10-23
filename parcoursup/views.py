from django.shortcuts import render
from parcoursup.models import Formations

def indexe(request):
    return render(request, 'pages/indexe.html.twig')

def index(request):
    return render(request, 'pages/index.html.twig')

def eleveaccueil(request):
    return render(request, 'pages/eleveaccueil.html.twig', {'Formations': Formations.objects.all()})
    

# Create your views here.
