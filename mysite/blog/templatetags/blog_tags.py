
from django import template
from ..models import Post, CategoryTree

register = template.Library()

@register.inclusion_tag('blog/lastpost.html')
def show_last_posts():
    last_posts = Post.objects.filter(status='published').order_by('publish')[:3]
    return {
        "last_posts": last_posts,
    }

@register.inclusion_tag('blog/category.html')
def show_category():
    category = CategoryTree.objects.all()
    return {
        "category": category,
    }