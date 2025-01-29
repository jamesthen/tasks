from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddTaskForm
from .models import AddTask


def index(request):
    tasks = AddTask.objects.all()
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddTaskForm()
    return render(request, "mytasks/index.html", {
        "tasks":tasks,
        "form":form
    })

def remove_task(request, task_id):
    if request:
        task_id = AddTask.objects.get(id = task_id)
        if task_id:
            task_id.delete()
        return redirect('index')
