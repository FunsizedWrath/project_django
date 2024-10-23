from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.indexe, name='indexe'),
    path('', views.index, name='indexe'),
]