from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import *

# Create your views here.
def student_view(request):
    return render(request, 'studentPage.html')
def tutor_view(request):
    return render(request, 'tutorPage.html')
def admin_view(request):
    return render(request, 'adminPage.html')
def admin_view_createuser(request):
    return render(request, 'createuser.html')
def admin_view_deleteuser(request):
    return render(request, 'deleteUser.html')




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
                user.save()
                Student.objects.create(user=user)
            elif role == 'is_tutor':
                user.is_tutor = True
                user.save()
                Tutor.objects.create(user=user)
            elif role == 'is_admin':
                user.is_admin = True
                user.save()
                Admin.objects.create(user=user)
            
            return redirect('admin_view')
    else:
        form = AdminCreateUser()

    return render(request, 'createuser.html', {'form': form})




def admin_view_deleteuser(request):
    # Ensure the user is an admin
    if not request.user.is_admin:
        messages.error(request, 'You do not have permission to view this page.')
        return redirect('home')

    # Initialize users 
    users = CustomUser.objects.filter(is_admin=False)

    # If the request method is POST, it means we are trying to delete a user
    if request.method == 'POST':
        user_id = request.POST.get('user_id')  # Assuming the user ID is passed in the POST data
        try:
            user_to_delete = CustomUser.objects.get(pk=user_id)
            if user_to_delete.is_admin:
                messages.error(request, 'Cannot delete another admin.')
            else:
                user_to_delete.delete()
                messages.success(request, 'User deleted successfully.')
        except ObjectDoesNotExist:
            messages.error(request, 'User not found.')

    # Filtering based on role
    role = request.GET.get('role', '')
    if role == 'student':
        users = users.filter(is_student=True)
    elif role == 'tutor':
        users = users.filter(is_tutor=True)

    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        users = users.filter(email__icontains=search_query)

    return render(request, 'deleteUser.html', {'users': users})

    




