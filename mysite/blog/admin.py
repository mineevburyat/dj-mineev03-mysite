from django.contrib import admin
from .models import CategoryTree, Post
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from django_mptt_admin.admin import DjangoMpttAdmin

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'publish', 'status')
    list_filter = ('status', 'created', 'publish')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


@admin.register(CategoryTree)
class CategoryAdmin(DraggableMPTTAdmin):
    prepopulated_fields = {"slug": ("title",)}
    mptt_level_indent = 20
    list_display=(
        'tree_actions',
        'indented_title',
        'slug',
        'order',
        'get_posts_count',
        'id',
        'level',
        'parent_id',
        'tree_id',
        'lft',
        'rght',
        'is_description'
        # ...more fields if you feel like it...
    )
    list_display_links=(
        'indented_title',
    )
    sortable_by =('order')

# admin.site.register(
#     CategoryTree,
#     DraggableMPTTAdmin,
#     list_display=(
#         'tree_actions',
#         'indented_title',
#         'get_posts_count'
#         # ...more fields if you feel like it...
#     ),
#     list_display_links=(
#         'indented_title',
#     ),
# )