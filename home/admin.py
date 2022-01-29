from django.contrib import admin
from .models import Breakfast


class BreakfastAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Breakfast, BreakfastAdmin)

# Register your models here.
