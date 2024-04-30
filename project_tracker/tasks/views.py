from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render

from tasks.models import Project, Task

# def index(request):
#     another_page_url = reverse('tasks:another_page')
#     quality_control_url = reverse('quality_control:index')
#     html = f"""<h1>Страница приложения tasks</h1>
#         <a href='{another_page_url}'>Перейти на другую страницу</a>
#         <a href='{quality_control_url}'>Перейти на главную страницу контроля качеством"""
#     return HttpResponse(html)

def index(request):
    return render(request, 'tasks/index.html')

def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'tasks/projects_list.html', {'project_list': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Task, project_id=project_id)
    return render(request, 'tasks/task_detail.html', {'project': project})

def task_detail(request, task_id, project_id):
    task = get_object_or_404(Task, task_id=task_id, project_id=project_id)
    return render(request, 'tasks/task_detail.html', {'task': task})

def another_page(request):
    return HttpResponse('Это другая страница приложения tasks')
