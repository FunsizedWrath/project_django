from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.indexe, name='indexe'),
    path('', views.index, name='indexe'),
    path('eleveaccueil/', views.eleveaccueil, name='eleveaccueil'),
    path('candidater/', views.candidater, name='candidater'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]