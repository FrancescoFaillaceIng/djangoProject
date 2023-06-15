from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type


class Ingredient(models.Model):
    name = models.CharField(max_length=2000)


class Instruction(models.Model):
    passage = models.TextField(max_length=2000)


class Image(models.Model):
    image = models.ImageField(upload_to='images/', default='')


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=2000)
    ingredients = models.CharField(max_length=2000, default='')
    instructions = models.CharField(max_length=2000, default='')
    image = models.ImageField(upload_to='images/', default='')

    def __str__(self):
        return self.title


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return "User #" + str(self.user.id) + " --> Recipe #" + str(self.recipe.id)

