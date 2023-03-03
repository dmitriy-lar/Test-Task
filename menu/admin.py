from django.contrib import admin
from .models import Menu, MenuItems


class MenuItemsAdmin(admin.ModelAdmin):
    list_display = ("title", "parent", "menu_id")


admin.site.register(Menu)
admin.site.register(MenuItems, MenuItemsAdmin)
