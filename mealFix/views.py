from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Recept, Course, Tips, TypeOfDiet, Cuisine, Dish
from .forms import ReceptForm, CourseForm, TipsForm, TypeOfDietForm, CuisineForm, DishForm


def register_request(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegForm()
    return render(request=request, template_name="register.html", context={"register_form": form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})

def forgotpasspage(request):
    return render(request, "forgot.html")

def searchpage(request):
    return render(request, "search.html")

def profilepage(request):
    return render(request, "profile.html")

def myrecipespage(request):
    return render(request, "myrecipes.html")

def quiz1page(request, id_course):
    oneCourse = Course.objects.get(id=id_course)
    queryset = Course.objects.all()

    context = {"oneCourse": oneCourse,"courses": queryset, "form": CourseForm}
    return render(request, "quiz1.html", context)

def quiz2page(request, id_course):
    oneCourse = Course.objects.get(id=id_course)

    context = {"oneCourse": oneCourse}
    return render(request, "quiz2.html", context)

def quiz3page(request, id_course):
    oneCourse = Course.objects.get(id=id_course)

    context = {"oneCourse": oneCourse}
    return render(request, "quiz3.html", context)

def quiz4page(request, id_course):
    oneCourse = Course.objects.get(id=id_course)

    context = {"oneCourse": oneCourse}
    return render(request, "quiz4.html", context)

def quiz5page(request, id_course):
    oneCourse = Course.objects.get(id=id_course)

    context = {"oneCourse": oneCourse}
    return render(request, "quiz5.html", context)

def resultpage(request, id_course):
    oneCourse = Course.objects.get(id=id_course)
    queryset = Course.objects.all()

    context = {"oneCourse": oneCourse, "courses": queryset, "form": CourseForm}
    return render(request, "quizresult.html", context)

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("main:login")

def recepti(request):
    queryset = Recept.objects.all()
    context ={"recepti": queryset, "form": ReceptForm}
    return render(request, "home.html", context=context)

def myrecipesappetizerspage(request):
    queryset = Recept.objects.all()
    context = {"recepti": queryset, "form": ReceptForm}
    return render(request, "myrecipes_appetizers.html", context=context)

def myrecipesbreakfastpage(request):
    queryset = Recept.objects.all()
    context = {"recepti": queryset, "form": ReceptForm}
    return render(request, "myrecipes_breakfast.html", context=context)

def myrecipesdessertspage(request):
    queryset = Recept.objects.all()
    context = {"recepti": queryset, "form": ReceptForm}
    return render(request, "myrecipes_desserts.html", context=context)

def myrecipeslunchpage(request):
    queryset = Recept.objects.all()
    context = {"recepti": queryset, "form": ReceptForm}
    return render(request, "myrecipes_lunch.html", context=context)

def under30page(request):
    queryset = Recept.objects.all()
    context = {"recepti": queryset, "form": ReceptForm}
    return render(request, "under30.html", context=context)

def breakfastpage(request):
    queryset = Recept.objects.all()
    context = {"recepti": queryset, "form": ReceptForm}
    return render(request, "breakfast.html", context=context)

def snackspage(request):
    queryset = Recept.objects.all()
    context = {"recepti": queryset, "form": ReceptForm}
    return render(request, "snacks.html", context=context)

def lunchpage(request):
    queryset = Recept.objects.all()
    context = {"recepti": queryset, "form": ReceptForm}
    return render(request, "lunch.html", context=context)

def dinnerpage(request):
    queryset = Recept.objects.all()
    context = {"recepti": queryset, "form": ReceptForm}
    return render(request, "dinner.html", context=context)

def dessertspage(request):
    queryset = Recept.objects.all()
    context = {"recepti": queryset, "form": ReceptForm}
    return render(request, "desserts.html", context=context)

def recept(request, id_recept):
    oneRecept=Recept.objects.get(id=id_recept)
    queryset = Course.objects.all()

    context = {'oneRecept': oneRecept, "courses": queryset}
    return render(request, "recipe_one.html", context)

def coursespage(request):
    queryset = Course.objects.all()
    querysetTips = Tips.objects.all()
    context ={"courses": queryset, "form": CourseForm, "tips": querysetTips}
    return render(request, "courses.html", context=context)

def course(request, id_course):
    oneCourse = Course.objects.get(id=id_course)

    context = {'oneCourse': oneCourse}
    return render(request, "course_one.html", context)

def typeofdietpage(request):
    queryset = TypeOfDiet.objects.all()
    querysetCuisine = Cuisine.objects.all()
    querysetDish = Dish.objects.all()
    context ={"typeofdiet": queryset, "cuisine": querysetCuisine, "dish": querysetDish, "form": TypeOfDietForm}
    return render(request, "search.html", context=context)

def todpage(request, id_tod):
    oneTod = TypeOfDiet.objects.get(id=id_tod)
    queryset = Recept.objects.all()

    context ={"oneTod": oneTod, "recipeT": queryset}
    return render(request, "todpage.html", context=context)

def cuisinepage(request, id_cuisine):
    oneCuisine = Cuisine.objects.get(id=id_cuisine)
    queryset = Recept.objects.all()

    context ={"oneCuisine": oneCuisine, "recipeC": queryset}
    return render(request, "cuisinepage.html", context=context)

def dishpage(request, id_dish):
    oneDish = Dish.objects.get(id=id_dish)
    queryset = Recept.objects.all()

    context ={"oneDish": oneDish, "recipeD": queryset}
    return render(request, "dishpage.html", context=context)




