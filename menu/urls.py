from django.urls import path
from .views import home_page_view, content_page_view

urlpatterns = [
    path("", home_page_view, name="home_page"),
    path("category/<int:pk>", content_page_view, name="content_page"),
]
