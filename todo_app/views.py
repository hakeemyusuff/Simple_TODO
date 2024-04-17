from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .form import Task_list
from .models import Tasks, CompletedTask
from django.urls import reverse


# Create your views here.
def view_todo(request):
    task = Task_list()
    completed_tasks = CompletedTask.objects.all()
    tasks = Tasks.objects.all()
    name = request.GET.get("name")
    completed_task = request.GET.get("complete")
    remove = request.GET.get("remove")
    clear_all = request.GET.get("clear")
    original = request.GET.get("original")
    edited = request.GET.get("edited")

    if name:
        task_to_del = Tasks.objects.filter(task=name).first()
        remove_permanent = CompletedTask.objects.filter(completed_task=name).first()
        if task_to_del:
            task_to_del.delete()
        else:
            remove_permanent.delete()
        return HttpResponseRedirect(reverse(view_todo))
    if completed_task:
        task_to_add = Tasks.objects.filter(task=completed_task).first()
        completed = CompletedTask(completed_task=task_to_add)
        completed.save()
        task_to_add.delete()
        return HttpResponseRedirect(reverse(view_todo))
    if remove:
        task_to_add = CompletedTask.objects.filter(completed_task=remove).first()
        completed = Tasks(task=task_to_add)
        completed.save()
        task_to_add.delete()
        return HttpResponseRedirect(reverse(view_todo))
    if clear_all:
        all_tasks = CompletedTask.objects.all().delete()
        return HttpResponseRedirect(reverse(view_todo))
    if original and edited:
        original_task = Tasks.objects.get(task=original)
        original_task.task = edited
        original_task.save()
        return HttpResponseRedirect(reverse(view_todo))
    context = {
        "task": task,
        "tasks": tasks,
        "complete": completed_tasks,
    }
    if request.method == "POST":
        task = Task_list(request.POST)
        if task.is_valid():
            task.save()
        return HttpResponseRedirect(reverse(view_todo))
    else:

        return render(request, "todo.html", context)
