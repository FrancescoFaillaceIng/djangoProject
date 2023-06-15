from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.urls import path

from djangoProject import settings
from . import views

urlpatterns = [
    path('', views.home, name="recipes-home"),
    path('create/', login_required(views.RecipeCreateView.as_view()), name="recipe-create"),
    path('list/', views.RecipeListView.as_view(), name="recipes-list"),
    path('detail/<int:pk>/', views.RecipeDetailView.as_view(), name="recipe-detail"),
    path('favorite/', login_required(views.FavoriteListView.as_view()), name="favorite-list"),
    path('search/', views.SearchListView.as_view(), name="search-list"),
    path('my_recipe/', login_required(views.MyRecipeListView.as_view()), name="my-recipes"),
    path('update/<int:pk>/', login_required(views.RecipeUpdateView.as_view()), name="recipe-update"),
    path('delete/<int:pk>/', login_required(views.RecipeDeleteView.as_view()), name="recipe-delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)