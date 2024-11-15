from django.urls import path
from .views import task_list, add_task, delete_task, mark_task

urlpatterns = [
    path('', task_list, name='task_list'),
    path('add/', add_task, name='add_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('mark/<int:task_id>/', mark_task, name='mark_task'),
]
