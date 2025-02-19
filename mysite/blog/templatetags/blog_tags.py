
from django import template
from ..models import Post, CategoryTree

register = template.Library()

@register.inclusion_tag('blog/_lastposts.html')
def show_last_posts():
    last_posts = Post.objects.filter(status='published').order_by('publish')[:3]
    return {
        "last_posts": last_posts,
    }

@register.inclusion_tag('blog/_category.html')
def show_category(*args):
    if len(args) == 1:
        category = args[0]
        print(category, type(category))
        if isinstance(category, CategoryTree):
            subcat = category.get_children() if category.get_children() else category.get_siblings()
        else:
            subcat = CategoryTree.objects.filter(level=0)
    else:
        subcat = CategoryTree.objects.filter(level=0)
    return {
        "category": subcat,
    }

