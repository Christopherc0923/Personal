from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Task

# Create your views here.
def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'todo/list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        Task.objects.create(title=request.POST['title'])
        return redirect('todo:list_tasks')
    return render(request, 'todo/create.html')

def delete_all(request):
    Task.objects.all().delete()
    return redirect('todo:list_tasks')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('todo:list_tasks')
