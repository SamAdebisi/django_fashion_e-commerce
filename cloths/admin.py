from django.contrib import admin

from .models import Cloth
# Register your models here.


class ClothAdmin(admin.ModelAdmin):
    list_display = ("style", "stylist", "price")


admin.site.register(Cloth, ClothAdmin)
