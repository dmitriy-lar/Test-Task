from django.shortcuts import render
from .models import MenuItems


def home_page_view(request):
    return render(request, "home_page.html", {'title': 'Home Page'})


def content_page_view(request, pk):
    item = MenuItems.objects.get(pk=pk)
    return render(request, "home_page.html",
                  {"item": item, 'title': 'Content Page'})
