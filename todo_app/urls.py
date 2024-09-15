from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_todo, name="todo_list"),
]


htmxpatterns = [
    path("/post", views.add_task, name="add_tasks"),
    path("<int:id>/delete", views.delete_task, name="delete_task"),
    path("<int:id>/completed", views.add_to_completed, name="add_to_completed"),
    path("<int:id>/tasks", views.add_to_tasks, name="add_to_tasks"),
    path("<int:id>/delete_complete", views.delete_completed, name="delete_completed"),
    path("/deleteAll", views.delete_all_completed, name="delete_all_completed")
]

urlpatterns += htmxpatterns
