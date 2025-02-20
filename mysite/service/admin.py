from django.contrib import admin
from .models import Course, Competetion

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon')

@admin.register(Competetion)
class CompetetionAdmin(admin.ModelAdmin):
    list_display = ('cod', 'description')