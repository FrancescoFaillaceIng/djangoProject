
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="recipes-home"),
    path('create/', views.RecipeCreateView.as_view(), name="recipe-create"),
    path('', views.RecipeListView.as_view(), name="recipes-list"),
]