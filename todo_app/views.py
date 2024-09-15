from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from .form import Task_list
from .models import Tasks, CompletedTask
from django.urls import reverse


def get_context():
    tasks = Tasks.objects.all()
    completed_tasks = CompletedTask.objects.all()
    context = {
        "complete": completed_tasks,
        "tasks": tasks,
    }
    return context
    
def view_todo(request):
    task = Task_list()
    tasks = Tasks.objects.all()
    completed_tasks = CompletedTask.objects.all()
    context = {
        "task": task,
        "tasks": tasks,
        "complete": completed_tasks,
    }
    return render(request, "to-do/base.html", context)


@require_POST
def add_task(request):
    task = Task_list(request.POST)
    if task.is_valid():
        task = task.save()
    context = get_context()
    return render(request, "to-do/components/tasks_list.html", context)


def delete_task(request, id):
    task = get_object_or_404(Tasks, id=id)
    task.delete()
    context = get_context()
    return render(request, "to-do/components/tasks_list.html", context)


def add_to_completed(request, id):
    task = get_object_or_404(Tasks, id=id)
    CompletedTask.objects.create(completed_task=task)
    task.delete()
    context = get_context()
    return render(request, "to-do/components/tasks_list.html", context)


def add_to_tasks(request, id):
    comp_task = get_object_or_404(CompletedTask, id=id)
    Tasks.objects.create(task=comp_task)
    comp_task.delete()
    context = get_context()
    return render(request, "to-do/components/tasks_list.html", context)


def delete_completed(request, id):
    task = get_object_or_404(CompletedTask, id=id)
    task.delete()
    context = get_context()
    return render(request, "to-do/components/tasks_list.html", context)

def delete_all_completed(request):
    CompletedTask.objects.all().delete()
    context = get_context()
    return render(request, "to-do/components/tasks_list.html", context)
