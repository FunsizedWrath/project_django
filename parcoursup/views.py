from django.shortcuts import render

def index(request):
    return render(request, 'parcoursup/index.twig')

# Create your views here.
