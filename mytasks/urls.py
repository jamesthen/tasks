from django.urls import path
from . import views

#TASKS!

urlpatterns = [
    path("", views.index, name="index"),
    path("remove_task/<task_id>", views.remove_task, name="remove_task"),
    path("add_goal", views.add_goal, name="add_goal"),
    path("remove_goal/<goal_id>", views.remove_goal, name="remove_goal"),
]
