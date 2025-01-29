from django.contrib import admin
from .models import CategoryTree, Post
from mptt.admin import MPTTModelAdmin

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'publish', 'status')
    list_filter = ('status', 'created', 'publish')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


@admin.register(CategoryTree)
class CategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("title",)}