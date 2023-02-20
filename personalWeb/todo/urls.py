from django.urls import path
from . import views
from .views import list_tasks, create_task

# Assign appname for clarity
app_name = "todo"


urlpatterns = [
    path('', views.list_tasks, name='list_tasks'),
    path('tasks/', views.list_tasks, name='list_tasks'),
    path('create/', views.create_task, name='create_task'),
    path('delete_all/', views.delete_all, name='delete_all'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    #path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]