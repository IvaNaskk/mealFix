from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "main"

urlpatterns = [
    path("home", views.recepti, name="home"),
    path("recept/<str:id_recept>", views.recept),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("forgot/", views.forgotpasspage, name="forgot"),
    path("profile/", views.profilepage, name="profile"),
    path("course/", views.coursespage, name="course"),
    path("courses/<str:id_course>", views.course, name="course_one"),
    path("search/under30mins", views.under30page, name="under30mins"),
    path("search/breakfast", views.breakfastpage, name="breakfast"),
    path("search/lunch", views.lunchpage, name="lunch"),
    path("search/snacks", views.snackspage, name="snacks"),
    path("search/dinner", views.dinnerpage, name="dinner"),
    path("search/desserts", views.dessertspage, name="desserts"),
    path("myrecipes/appetizers", views.myrecipesappetizerspage, name="appetizers"),
    path("myrecipes/breakfast", views.myrecipesbreakfastpage, name="breakfast"),
    path("myrecipes/desserts", views.myrecipesdessertspage, name="desserts"),
    path("myrecipes/lunch", views.myrecipeslunchpage, name="lunch"),
    path("search/", views.typeofdietpage, name="search"),
    path("search/typeofdiet/<str:id_tod>", views.todpage),
    path("search/cuisine/<str:id_cuisine>", views.cuisinepage),
    path("search/dish/<str:id_dish>", views.dishpage),
    path("myrecipes/", views.myrecipespage, name="myrecipes"),
    path("course/<str:id_course>/quiz1", views.quiz1page, name="quiz1"),
    path("course/<str:id_course>/quiz2", views.quiz2page, name="quiz2"),
    path("course/<str:id_course>/quiz3", views.quiz3page, name="quiz3"),
    path("course/<str:id_course>/quiz4", views.quiz4page, name="quiz4"),
    path("course/<str:id_course>/quiz5", views.quiz5page, name="quiz5"),
    path("course/<str:id_course>/quiz/result", views.resultpage, name="quizresult")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)