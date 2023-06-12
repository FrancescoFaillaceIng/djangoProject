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


class RecipeSearchForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'author', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = False
        self.fields['author'].required = False
        self.fields['category'].required = False
