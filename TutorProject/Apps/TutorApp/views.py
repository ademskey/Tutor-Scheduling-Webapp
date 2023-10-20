from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.
def student_view(request):
    return render(request, 'studentPage.html')
def tutor_view(request):
    return render(request, 'tutorPage.html')
def admin_view(request):
    return render(request, 'adminPage.html')
def admin_view_createuser(request):
    return render(request, 'createuser.html')





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
        form = AuthenticationForm(data=request.POST or None)  # Handle the POST data
        if request.method == "POST":
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                if user.is_admin:
                    return redirect('admin_view')
                elif user.is_student:
                    return redirect('student_view')
                elif user.is_tutor:
                    return redirect('tutor_view')
            else:
                messages.error(request, 'Invalid email or password.')

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



def admin_create_user(request):
    if not request.user.is_admin:
        return redirect('home')

    if request.method == 'POST':
        form = AdminCreateUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save yet
            role = form.cleaned_data.get('role')
            if role == 'is_student':
                user.is_student = True
            elif role == 'is_tutor':
                user.is_tutor = True
            elif role == 'is_admin':
                user.is_admin = True
            user.save()
            return redirect('admin_view')
    else:
        form = AdminCreateUser()

    return render(request, 'createuser.html', {'form': form})


