# Generated by Django 4.2.1 on 2023-06-12 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0005_recipe_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="image",
            field=models.ImageField(default="", upload_to="images/"),
        ),
    ]
