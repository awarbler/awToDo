from pickle import FALSE
from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.urls import reverse_lazy #  for model forms 

from django.contrib.auth.views import LoginView


from .models import Task

class CustomLoginView(LoginView):
    template_name = 'awApp/login.html'
    fields = '__all__'
    redirect_authenticated_user: True

    def get_success_url(self) :
        return reverse_lazy ('tasks')
# Create your views here.

class TaskList(ListView):
    model = Task 
    context_object_name= 'tasks'

class TaskDetail (DetailView):
    model = Task    
    context_object_name = 'task'
    template_name= 'awApp/task.html'

class TaskCreate(CreateView):
    model = Task    
    # uses model form from create view 
    # gives us a model form to use createview
    # have all field added  
    fields =  '__all__'
    # redirect user 
    success_url = reverse_lazy ('tasks')

class TaskUpdate(UpdateView):
    model = Task     
    fields =  '__all__'
    success_url = reverse_lazy ('tasks')

class DeleteView(DeleteView):
    model = Task     
    context_object_name = 'task'
    success_url = reverse_lazy ('tasks')    


