from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddTaskForm, AddGoalForm
from .models import AddTask, AddGoal

# def add_items(request):
#     if request.method == "POST":
#         task_form = AddTaskForm(request.POST, prefix="task")
#         goal_form = AddGoalForm(request.POST, prefix="goal")

#         if task_form.is_valid():
#             task_form.save()
#         if goal_form.is_valid():
#             goal_form.save()

#         return redirect("success_url")  # Redirect after submission

#     else:
#         task_form = AddTaskForm(prefix="task")
#         goal_form = AddGoalForm(prefix="goal")

#     return render(request, "add_items.html", {"task_form": task_form, "goal_form": goal_form})

def index(request):
    tasks = AddTask.objects.all()
    if request.method == "POST":
        task_form = AddTaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('index')
    else:
        task_form = AddTaskForm()
    return render(request, "mytasks/index.html", {
        "tasks": tasks,
        "task_form": task_form,
    })

def remove_task(request, task_id):
    if request:
        task_id = AddTask.objects.get(id = task_id)
        if task_id:
            task_id.delete()
        return redirect('index')


def add_goal(request):
    goals = AddGoal.objects.all()
    if request.method == "POST":
        goal_form = AddGoalForm(request.POST)
        if goal_form.is_valid():
            goal_form.save()
            return redirect('add_goal')
    else:
        goal_form = AddGoalForm()
    return render(request, "mytasks/goals.html", {
        "goals": goals,
        "goal_form": goal_form,
    })
    
def remove_goal(request, goal_id):
    if request:
        goal_id = AddGoal.objects.get(id = goal_id)
        if goal_id:
            goal_id.delete()
        return redirect('add_goal')



def task_list(request):
    tasks = Task.objects.all()  # Fetch all tasks
    task_names = ", ".join(str(task) for task in tasks)  # Calls __str__ on each task
    return HttpResponse(f"Tasks: {task_names}")