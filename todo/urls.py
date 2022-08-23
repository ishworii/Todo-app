from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("insert_item", views.insert_item, name="insert_item"),
    path("delete/<int:id>", views.delete_item, name="delete_item"),
]
