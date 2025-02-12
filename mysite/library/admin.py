from django.contrib import admin
from .models import Genre, Book, eBookInstance, HardBookInstance


# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(HardBookInstance)
# admin.site.register(eBookInstance)

class eBookInstaceInLine(admin.TabularInline):
    model = eBookInstance
    extra = 0

class HardBookInstaceInLine(admin.TabularInline):
    model = HardBookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'cataloge', 'category', 'authors')
    inlines = (eBookInstaceInLine, HardBookInstaceInLine)
    
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)