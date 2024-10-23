from django.shortcuts import render
from parcoursup.models import Formations
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'pages/login.html.twig'

def indexe(request):
    return render(request, 'pages/indexe.html.twig')

def index(request):
    return render(request, 'pages/index.html.twig')

def eleveaccueil(request):
    return render(request, 'accounts/eleveaccueil.html.twig', {'Formations': Formations.objects.all()})

def candidater(request):
    return render(request, 'accounts/candidater.html.twig')

def login(request):
    return render(request, 'pages/login.html.twig')

def register(request):
    return render(request, 'pages/register.html.twig')

def logout(request):
    return render(request, 'pages/logout.html.twig')
# Create your views here.
