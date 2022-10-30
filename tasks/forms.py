from django import forms
from tasks.models import Task


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

class TaskUpdateForm(forms.ModelForm):
    completed_at = forms.DateTimeInput()
    class Meta:
        model = Task
        fields = ['title', 'status', 'description', 'completed_at']