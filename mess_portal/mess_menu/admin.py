from django.contrib import admin

from .models import Day, Food


class FoodInline(admin.StackedInline):
    model = Food
    


class DayAdmin(admin.ModelAdmin):
    fieldsets = [
           (None, {'fields': ['day_name']}),
    ]
    inlines = [FoodInline]
        
admin.site.register(Day, DayAdmin)
