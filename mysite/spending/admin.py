from django.contrib import admin
from .models import Goal, Operation
# Register your models here.
@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    pass

@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    pass