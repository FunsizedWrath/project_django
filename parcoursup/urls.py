from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index/', views.indexe, name='indexe'),
    path('', views.index, name='index'),
    path('eleveaccueil/', views.eleveaccueil, name='eleveaccueil'),
    path('candidater/', views.candidater, name='candidater'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]