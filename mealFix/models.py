from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Recept(models.Model):
    title = models.CharField(max_length=50)
    time = models.IntegerField()
    tod = models.IntegerField(null=True, blank=True)
    bigsix = models.IntegerField(null=True, blank=True)
    cuisine = models.IntegerField(null=True, blank=True)
    dish_style = models.IntegerField(null=True, blank=True)
    ingredients = models.TextField(blank=True, null=True)
    calories = models.TextField(null=True, blank=True)
    fat = models.TextField(null=True, blank=True)
    carbs = models.TextField(null=True, blank=True)
    fiber = models.TextField(null=True, blank=True)
    sugar = models.TextField(null=True, blank=True)
    protein = models.TextField(null=True, blank=True)
    servings = models.IntegerField(null=True, blank=True)
    step1 = models.TextField(null=True, blank=True)
    step2 = models.TextField(null=True, blank=True)
    step3 = models.TextField(null=True, blank=True)
    step4 = models.TextField(null=True, blank=True)
    step5 = models.TextField(null=True, blank=True)
    step6 = models.TextField(null=True, blank=True)
    step7 = models.TextField(null=True, blank=True)
    step8 = models.TextField(null=True, blank=True)
    step9 = models.TextField(null=True, blank=True)
    step10 = models.TextField(null=True, blank=True)
    myrecipes = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="cover_image", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class Course(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="cover_image", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)

class Tips(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class TypeOfDiet(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class Cuisine(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class Dish(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

