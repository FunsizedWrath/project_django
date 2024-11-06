from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index/', views.indexe, name='indexe'),
    path('', views.index, name='index'),
    path('eleveaccueil/', views.eleveaccueil, name='eleveaccueil'),
    path('candidater/<int:formation_id>/', views.candidater, name='candidater'),
    path('formation/<int:formation_id>/candidater/', views.candidater, name='candidater'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('etablissementaccueil/', views.etablissementaccueil, name='etablissement-accueil'),
    path('candidats/', views.candidats, name='candidats'),
    path('formation/<int:formation_id>/submit_application/', views.submit_application, name='submit_application'),
    path('application_success/', views.application_success, name='application_success')
]