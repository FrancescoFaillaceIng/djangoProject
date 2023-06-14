# Generated by Django 4.2.1 on 2023-06-08 14:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("quantity", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Instruction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("passage", models.TextField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name="recipe",
            name="description",
            field=models.TextField(default=datetime.time),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="recipe",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="recipes.category",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="recipe",
            name="ingredients",
            field=models.ManyToManyField(
                related_name="recipes", to="recipes.ingredient"
            ),
        ),
        migrations.AddField(
            model_name="recipe",
            name="instructions",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="recipes", to="recipes.instruction"
            ),
        ),
    ]