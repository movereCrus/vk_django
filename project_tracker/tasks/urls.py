from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects_list, name='projects_list'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('projects/<int:project_id>/tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('projects/new/', views.create_project, name='create_project'),
    path('projects/<int:project_id>/add_task/', views.add_task_to_project, name='add_task_to_project')
    # path('another/', views.another_page, name='another_page')
]