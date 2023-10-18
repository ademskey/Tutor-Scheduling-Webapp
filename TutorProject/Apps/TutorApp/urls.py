from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name = "register"),
    path('login/', views.custom_login, name='user_login')
]
 