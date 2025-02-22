from django.contrib import admin
from .models import Course, Competetion, CompetetionType, ActiviteType, Skill


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon')

@admin.register(Competetion)
class CompetetionAdmin(admin.ModelAdmin):
    list_display = ('cod', 'typecompetetion', 'activite', 'description')
    ordering = ('-pk',)
    # list_editable = ('activite',)

@admin.register(CompetetionType)
class CompetetionTypeAdmin(admin.ModelAdmin):
    list_display = ('cod', 'transcript')

@admin.register(ActiviteType)
class ActiviteTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass