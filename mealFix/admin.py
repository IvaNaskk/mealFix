from django.contrib import admin
from .models import Recept, Course, Tips, TypeOfDiet, Cuisine, Dish


#
# Register your models here.

# recepti-dodavanje
class ReceptAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    list_filter = ("title",)

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.author):
            return True
        return False


admin.site.register(Recept, ReceptAdmin)

# kursevi-dodavanje
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    list_filter = ("title",)

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.author):
            return True
        return False


admin.site.register(Course, CourseAdmin)

# tips-dodavanje
class TipsAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    list_filter = ("title",)

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.author):
            return True
        return False


admin.site.register(Tips, TipsAdmin)

# tip-dodavanje
class TypeOfDietAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    list_filter = ("title",)

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.author):
            return True
        return False


admin.site.register(TypeOfDiet, TypeOfDietAdmin)

# kujna-dodavanje
class CuisineAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    list_filter = ("title",)

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.author):
            return True
        return False


admin.site.register(Cuisine, CuisineAdmin)

# dish-dodavanje
class DishAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    list_filter = ("title",)

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.author):
            return True
        return False


admin.site.register(Dish, DishAdmin)
