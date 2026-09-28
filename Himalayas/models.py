from django.db import models

# Create your models here.

class TASK(models.Model):
    task_name= models.CharField(max_length=100)
    is_completed= models.BooleanField(default=False)
    due_date= models.DateField()
    created_date= models.DateField(auto_now=True)
