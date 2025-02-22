from django.contrib import admin
from .models import Science, Speciality, GroupScience, FGOS

@admin.register(Science)
class ScienceAdmin(admin.ModelAdmin):
    pass

@admin.register(GroupScience)
class GroupScinceAdmin(admin.ModelAdmin):
    pass

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    pass

@admin.register(FGOS)
class FGOSAdmin(admin.ModelAdmin):
    pass