from django.db import models

# Create your models here.
class AddTask(models.Model):
    task_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.task_name
    
class AddGoal(models.Model):
    goal_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # Larger text
    due_date = models.DateField()  # Date picker
    completed = models.BooleanField(default=False)  # Checkbox
    
    def __str__(self):
        return self.goal_name