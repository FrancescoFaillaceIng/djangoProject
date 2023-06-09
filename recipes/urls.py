
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="recipes-home"),
    path('create/', views.RecipeCreateView.as_view(), name="recipe-create"),
    path('list/', views.RecipeListView.as_view(), name="recipes-list"),
    path('detail/<int:pk>/', views.RecipeDetailView.as_view(), name="recipe-detail"),
]