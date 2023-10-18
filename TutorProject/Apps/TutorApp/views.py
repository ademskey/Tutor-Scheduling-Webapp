from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
# Create your views here.

def home(request):
    return render(request, "register.html")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_student = True
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, "register.html", context)

# Login View
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                if user.is_admin:
                    return redirect('admin_dashboard')
                elif user.is_student:
                    return redirect('student_dashboard')
                elif user.is_tutor:
                    return redirect('tutor_dashboard')
                else:
                    return redirect('dashboard')  # Redirect to a default dashboard or another appropriate URL

    # Handle the case when login fails or for GET requests
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, "login.html", context)

