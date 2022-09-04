from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import NumberInput
from .models import Recept, Course, Tips, TypeOfDiet, Cuisine, Dish


# Create your forms here.


class RegForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ("username", "email", "birth_date", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super(RegForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.birth_date = self.cleaned_data['birth_date']
        if commit:
            user.save()
        return user



class ReceptForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReceptForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Recept
        exclude = ("author",)

class CourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Course
        exclude = ("author",)

class TipsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TipsForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Tips
        exclude = ("author",)

class TypeOfDietForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TypeOfDietForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = TypeOfDiet
        exclude = ("author",)

class CuisineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CuisineForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Cuisine
        exclude = ("author",)

class DishForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DishForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Dish
        exclude = ("author",)
