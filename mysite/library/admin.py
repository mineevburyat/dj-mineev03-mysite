from django.contrib import admin
from .models import Book, eBookInstance, HardBookInstance, GenreTree
from mptt.admin import DraggableMPTTAdmin



admin.site.register(
    GenreTree,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)


# admin.site.register(GenreTree, MPTTModelAdmin)
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
    list_display = ('title', 'genretree', 'cataloge', 'category', 'authors')
    inlines = (eBookInstaceInLine, HardBookInstaceInLine)
    
