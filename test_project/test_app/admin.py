from django.contrib import admin

from .models import Advert, Category, City


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ["title"]
