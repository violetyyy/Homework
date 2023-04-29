from django.contrib import admin
from .models import HomeWork, Lesson

# Register your models here.

@admin.register(HomeWork)
class homeworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'deadline', 'created_date', 'updated_date')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', )