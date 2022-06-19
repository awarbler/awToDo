from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# migrate database
class Task(models.Model):
    # import django user somany to one relationship 
    
    # this deletes all user and all children if user gets deleted
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank = True)
    # string set to max length 
    title= models.CharField(max_length=200)
    # string set textfield for more data
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    # auto create date time field and auto populate it
    created = models.DateTimeField(auto_now_add=True)

# define a string to print
    def __str__(self) :
        return self.title

    # set default ordering the model by the complete status sent to bottom of list
    class Meta:
        ordering = ['complete']    
