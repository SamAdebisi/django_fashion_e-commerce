from django.contrib import admin

from .models import Cloth, Review
# Register your models here.


class ReviewInline(admin.TabularInline):
    model = Review


class ClothAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ("style", "stylist", "price")


admin.site.register(Cloth, ClothAdmin)
