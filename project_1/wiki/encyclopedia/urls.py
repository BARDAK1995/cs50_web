from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("newpage", views.new_page, name="new_page"),
    path("edit", views.edit_page, name="edit_page"),
    path("random", views.random_page, name="random_page"),
    path("<str:entry_title>", views.entry_page, name="entry_title"),
]
