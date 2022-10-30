from django.conf import settings
from django.db import models

class Task(models.Model):
    STATUS_CHOICES = (
        ('todo', 'ToDo'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
