from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import *
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        # Redirect logged-in users to their respective pages
        if request.user.is_admin:
            return redirect(admin_view)
        elif request.user.is_student:
            return redirect(student_view)
        elif request.user.is_tutor:
            return redirect(tutor_view)

    # Handle the login POST request
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            if user.is_admin:
                return redirect(admin_view)
            elif user.is_student:
                return redirect(student_view)
            elif user.is_tutor:
                return redirect(tutor_view)
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()

    # For non-logged-in users, show the login page with the form
    return render(request, "login.html", {'form': form})




def student_view(request):
    return render(request, 'studentPage.html')
def admin_view(request):
    return render(request, 'adminPage.html')
def tutor_view(request):
    return render(request, 'tutorPage.html')



    

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

def adminpage(request):
    return render(request, 'adminPage.html')

def createuser(request):
    if request.user.is_admin:
        form = AdminCreateUser()
        return render(request, 'createuser.html', {'form': form})


    else:
        return redirect(home) 