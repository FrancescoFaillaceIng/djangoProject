from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView
from . import models
from .forms import RecipeForm, RecipeSearchForm


# Create your views here.

def home(request):
    recipes = models.Recipe.objects.all()
    context = {
       'recipes': recipes
          }

    return render(request, 'Home.html', context)


class RecipeCreateView(CreateView):
    model = models.Recipe
    form_class = RecipeForm
    template_name = 'Recipe_create.html'

    def get_context_data(self, **kwargs):
        context = super(RecipeCreateView, self).get_context_data(**kwargs)
        context['categories'] = models.Category.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = User.objects.get(id=request.user.id)
            recipe.save()
            return redirect('recipes-list')
        else:
            print(form.errors)
            return render(request, self.template_name, {
                "form": form,
                "categories": models.Category.objects.all()
            })


class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'Recipes_list.html'
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = models.Recipe
    template_name = 'Recipe_detail.html'
    context_object_name = 'recipe'

    def post(self, request, *args, **kwargs):
        recipe = models.Recipe.objects.get(id=self.kwargs['pk'])
        favorite, created = models.Favorite.objects.get_or_create(recipe=recipe, user=request.user)
        if not created:
            favorite.delete()
        return redirect('recipe-detail', pk=recipe.id)

    def get_context_data(self, **kwargs):
        context = super(RecipeDetailView, self).get_context_data(**kwargs)
        recipe = models.Recipe.objects.get(id=self.kwargs['pk'])
        context['favorite'] = models.Favorite.objects.filter(recipe=recipe, user=self.request.user).exists()
        return context


class FavoriteListView(ListView):
    model = models.Favorite
    template_name = 'Favorite_list.html'
    context_object_name = 'favorites'

    def get_queryset(self):
        return models.Favorite.objects.filter(user=self.request.user)


class SearchListView(ListView):
    model = models.Recipe
    template_name = 'Search.html'
    form_class = RecipeSearchForm
    context_object_name = 'recipes'

    def get_queryset(self):
        return models.Recipe.objects.filter(title__icontains=self.request.GET.get('search'))

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET)
        recipe = models.Recipe.objects.all()

        if form.is_valid():
            title = form.cleaned_data.get('title')
            category = form.cleaned_data.get('category')
            author = form.cleaned_data.get('author')

            if title:
                recipe = recipe.filter(title__icontains=title)
            if category:
                recipe = recipe.filter(category=category)
            if author:
                recipe = recipe.filter(author=author)

        context = {
            'form': form,
            "recipes": recipe
        }

        return render(request, self.template_name, context)



