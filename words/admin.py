from django.contrib import admin
from words.models import DayNumber, Words, WordLevel

@admin.register(DayNumber)
class DayNumberAdmin(admin.ModelAdmin):
    list_display = ['title', 'view_home']

@admin.register(Words)
class WordAdmin(admin.ModelAdmin):
    list_display = ['get_full_word']

@admin.register(WordLevel)
class WordAdmin(admin.ModelAdmin):
    list_display = ['title', 'view_home']

