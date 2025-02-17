from .models import AddTask, AddGoal
from django import forms

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = AddTask  # Link the form to the model
        fields = ['task_name']  # Specify fields to include in the form
        widgets = {
            'task_name': forms.TextInput(attrs={'rows': 1, 'cols': 1, 'placeholder':'Add a new task'}),  # Add custom widget with attributes
        }
        labels = {
            'task_name': ''  # Custom label for title
        }

class AddGoalForm(forms.ModelForm):
    class Meta:
        model = AddGoal
        fields = ['goal_name', 'description', 'due_date', 'completed']
        widgets = {
            'goal_name': forms.TextInput(attrs={'rows': 1, 'cols': 1, 'placeholder':'Add a new goal'}),
            'description': forms.TextInput(attrs={'rows': 1, 'cols': 1, 'placeholder':'Description'}),
            
            'completed': forms.CheckboxInput,
        }