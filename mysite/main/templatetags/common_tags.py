# https://gadjimuradov.ru/post/menyu-dlya-django-sajta/
# https://habr.com/ru/sandbox/90175/

from django import template
from ..models import Menu
from taggit.models import Tag 

register = template.Library()


@register.inclusion_tag('main/top.html', takes_context=True)
def show_top_menu(context):
    menu_items = Menu.objects.all()
    return {
        "menu_items": menu_items,
    }

@register.inclusion_tag('main/tags.html')
def show_tags(*args, **kwargs): 
    tags = Tag.objects.all() 
    return {
        "tags": tags
    } 
