from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')


class AdminCreateUser(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'is_student', 'is_tutor', 'is_admin')