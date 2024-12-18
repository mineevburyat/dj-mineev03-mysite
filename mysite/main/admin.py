from django.contrib import admin
from .models import Menu, UsefulLink
# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass

@admin.register(UsefulLink)
class UsefulLinkAdmin(admin.ModelAdmin):
    pass