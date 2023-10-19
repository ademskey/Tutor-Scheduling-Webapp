from django.urls import path
from . import views
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path('student/', views.student_view, name='student_view_name'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/profile/', views.student_view, name='logged in'),
    path('administrator/createuser', views.createuser),
    path('administrator/', views.adminpage),
]
 