# https://gadjimuradov.ru/post/menyu-dlya-django-sajta/
# https://habr.com/ru/sandbox/90175/

from django import template
from ..models import Menu
from taggit.models import Tag 

register = template.Library()


@register.inclusion_tag('_components/_topmenu.html')
def show_top_menu():
    menu_items = Menu.objects.all()
    return {
        "menu_items": menu_items,
    }

@register.inclusion_tag('_components/_tags.html')
def show_tags(*args):
    if len(args) == 1:
        tags = Tag.objects.all()
    else:
        tags = Tag.objects.all() 
    return {
        "tags": tags
    }


