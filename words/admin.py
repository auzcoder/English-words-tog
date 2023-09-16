from django.contrib import admin
from words.models import DayNumber

@admin.register(DayNumber)
class DayNumberAdmin(admin.ModelAdmin):
    list_display = ['title', 'view_home']

