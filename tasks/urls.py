from django.urls import path, reverse_lazy
from . import views

app_name='tasks'
urlpatterns = [
    path('', views.TaskListView.as_view(), name='all'),
    path('task/<int:pk>', views.TaskDetailView.as_view(), name='task_detail'),
    path('task/create',
        views.TaskCreateView.as_view(success_url=reverse_lazy('tasks:all')), name='task_create'),
    path('task/<int:pk>/update',
        views.TaskUpdateView.as_view(success_url=reverse_lazy('tasks:all')), name='task_update'),
    path('task/<int:pk>/delete',
        views.TaskDeleteView.as_view(success_url=reverse_lazy('tasks:all')), name='task_delete'),
]