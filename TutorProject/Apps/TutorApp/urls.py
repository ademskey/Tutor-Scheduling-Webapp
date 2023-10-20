from django.urls import path
from . import views
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('student/', views.student_view, name='student_view'),
    path('tutor/', views.tutor_view, name='tutor_view'),
    path('administrator/', views.admin_view, name = 'admin_view' ),
    path('administrator/createuser', views.createuser, name = 'adminCreateUser'),
    
]
 