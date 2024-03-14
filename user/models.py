from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    age = models.CharField(max_length=250, null=False, blank=False)
    marital_status = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)

def __str__(self) :
    return self.name