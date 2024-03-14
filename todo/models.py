from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    completed = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)

def __str__(self):
    return self.title