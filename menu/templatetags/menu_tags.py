from django import template

from ..models import MenuItems

register = template.Library()


@register.inclusion_tag("menu.html", takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItems.objects.filter(menu_id__title=menu_name)
    list_items = []

    for item in menu_items:
        if item.parent is None:
            list_items.append(item)
    request = context["request"]

    curr_path = request.path.split("/")[-1]

    return {"list_items": list_items, "path": curr_path}


@register.filter()
def to_int(value):
    return int(value)
