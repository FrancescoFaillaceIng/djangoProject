from django.forms import ModelForm, Textarea, TextInput
from .models import Recipe

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'category', 'ingredients', 'instructions']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'category': TextInput(attrs={'class': 'form-control'}),
            'ingredients': Textarea(attrs={'class': 'form-control'}),
            'instructions': Textarea(attrs={'class': 'form-control'}),
        }