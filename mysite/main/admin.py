from django.contrib import admin
from .models import Menu, UsefulLink
# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'position')

@admin.register(UsefulLink)
class UsefulLinkAdmin(admin.ModelAdmin):
    pass