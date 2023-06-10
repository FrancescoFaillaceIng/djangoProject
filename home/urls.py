from django.urls import path
from . import views
from django.contrib.auth import views as auth


urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', auth.LoginView.as_view(template_name="login.html"),
         name="login"),
    path('logout/', auth.LogoutView.as_view(template_name="logout.html"),
         name="logout"),
    ]

