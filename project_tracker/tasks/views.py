from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render

from tasks.forms import ProjectForm, TaskForm
from tasks.models import Project, Task

def index(request):
    return render(request, 'tasks/index.html')

def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'tasks/projects_list.html', {'projects_list': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'tasks/project_detail.html', {'project': project})

def task_detail(request, task_id, project_id):
    task = get_object_or_404(Task, id=task_id, project_id=project_id)
    return render(request, 'tasks/task_detail.html', {'task': task})

def another_page(request):
    return HttpResponse('Это другая страница приложения tasks')

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:projects_list')
    else:
        form = ProjectForm()
    return render(request, 'tasks/project_create.html', {'form': form})

def add_task_to_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('tasks:task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form, 'project': project})
