from django.shortcuts import render

def index(request):
    return render(request, 'index.html.twig')

# Create your views here.
