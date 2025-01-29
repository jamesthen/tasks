from django.urls import path
from . import views

#TASKS!

urlpatterns = [
    path("", views.index, name="index"),
    path("remove_task/<task_id>", views.remove_task, name="remove_task"),
]
