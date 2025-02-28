from django.contrib import admin
from .models import (Course, Competetion, CompetetionType, 
                     ActiviteType, Skill, ChapterLesson,
                     Lesson)

class LessonAdminInLine(admin.StackedInline):
    extra = 0
    model = Lesson

@admin.register(ChapterLesson)
class ChapterAdmin(admin.ModelAdmin):
    inlines = (LessonAdminInLine, )
    fields = ('title', )

class ChapterLessonInLine(admin.StackedInline):
    extra = 0
    model = ChapterLesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon')
    inlines = (ChapterLessonInLine, )

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

