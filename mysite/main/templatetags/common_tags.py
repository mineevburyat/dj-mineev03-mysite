# https://gadjimuradov.ru/post/menyu-dlya-django-sajta/
# https://habr.com/ru/sandbox/90175/

from django import template
from ..models import Menu
register = template.Library()


@register.inclusion_tag('main/top.html', takes_context=True)
def show_top_menu(context):
    menu_items = Menu.objects.all()
    return {
        "menu_items": menu_items,
    }