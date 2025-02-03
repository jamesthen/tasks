from .models import AddTask
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
