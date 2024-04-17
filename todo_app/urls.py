from django.urls import path
from . import views

urlpatterns = [
    path("todo-list/", views.view_todo, name="todo_list"),
]
