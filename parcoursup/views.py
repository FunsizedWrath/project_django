from django.shortcuts import render, get_object_or_404
from parcoursup.models import Formations, Applications
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

class CustomLoginView(LoginView):
    template_name = 'pages/login.html.twig'

def indexe(request):
    return render(request, 'pages/indexe.html.twig')

def index(request):
    return render(request, 'pages/index.html.twig')

def eleveaccueil(request):
    # Get the logged-in user
    user = request.user

    # Check if the user is in the 'students' group
    is_student = user.groups.filter(name='Students').exists()
    print(is_student)

    # Pass the result to the template
    return render(request, 'accounts/eleveaccueil.html.twig', {'Formations': Formations.objects.all(), 'is_student': is_student})

def candidater(request, formation_id):
    formation = get_object_or_404(Formations, id=formation_id)
    return render(request, 'accounts/candidater.html.twig', {'formation': formation})

def submit_application(request, formation_id):
    if request.method == 'POST':
        user_id = request.user
        formation_id = get_object_or_404(Formations, id=formation_id)
        application, created = Applications.objects.get_or_create(user_id=user_id, formation_id=formation_id)
        application.status = "A candidater"
        application.save()

        # student_name = request.POST.get('student_name')
        # student_email = request.POST.get('student_email')
        # motivation = request.POST.get('motivation')

        # Get the formation for which the student is applying

        # Save the application to the database
        # application = Applications(
        #     # formation=formation,
        #     # student_name=student_name,
        #     # student_email=student_email,
        #     # motivation=motivation
        # )
        # application.save()

        # Redirect to a confirmation page (you can create one, or just redirect back to a listing)
        return redirect('application_success')

    # return redirect('candidater', formation_id=formation_id)

def login(request):
    return render(request, 'pages/login.html.twig')

def register(request):
    return render(request, 'pages/register.html.twig')

def etablissementaccueil(request):
    return render(request, 'etablissement/etablissement-accueil.html.twig', {'Formations': Formations.objects.all()})

def candidats(request):
    return render(request, 'etablissement/candidats.html.twig', {'Applications': Applications.objects.all()})

def application_success(request):
    return render(request, 'accounts/application_success.html.twig')

# Create your views here.
