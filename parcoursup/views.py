from django.shortcuts import render

def index(request):
    return render(request, 'parcoursup/templates/index.html.twig')

# Create your views here.
