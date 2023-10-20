from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import *
from django.urls import reverse_lazy



# Create your views here.
def student_view(request):
    return render(request, 'studentPage.html')
def admin_view(request):
    return render(request, 'adminPage.html')
def tutor_view(request):
    return render(request, 'tutorPage.html')





# write your methods below here
def home(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('admin_view')  # Use the name of the URL pattern
        elif request.user.is_student:
            return redirect('student_view')  # Use the name of the URL pattern
        elif request.user.is_tutor:
            return redirect('tutor_view')  # Use the name of the URL pattern
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Log the user in.
            login(request, user)
            
            return redirect(student_view)  # Use the name of the URL pattern
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})



def createuser(request):
    if request.user.is_admin:
        form = AdminCreateUser()
        return render(request, 'createuser.html', {'form': form})


    else:
        return redirect(home) 