from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskCreateForm, TaskUpdateForm
from .models import Task
from .owner import OwnerListView, OwnerDetailView, OwnerUpdateView, OwnerDeleteView


class TaskListView(OwnerListView):
    model = Task
    template_name = "tasks/task_list.html"

    def get(self, request) :
        task_list = Task.objects.all()
        search_value =  request.GET.get("search", False)
        if search_value :
            query = Q(title__icontains=search_value) 
            query.add(Q(description__icontains=search_value), Q.OR)
            task_list = Task.objects.filter(query).select_related()
        else :
            task_list = Task.objects.all()
        ctx = {'task_list' : task_list, 'search': search_value}
        return render(request, self.template_name, ctx)


class TaskDetailView(OwnerDetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    def get(self, request, pk) :
        task = Task.objects.get(id=pk)
        context = { 'task' : task }
        return render(request, self.template_name, context)

class TaskCreateView(LoginRequiredMixin, View):
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:all')

    def get(self, request, pk=None):
        form = TaskCreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = TaskCreateForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        inst = form.save(commit=False)
        inst.owner = self.request.user
        inst.save()
        return redirect(self.success_url)

class TaskUpdateView(LoginRequiredMixin, View):
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:all')

    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk, owner=self.request.user)
        form = TaskUpdateForm(instance=task)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        inst = get_object_or_404(Task, id=pk, owner=self.request.user)
        form = TaskUpdateForm(request.POST, None, instance=inst)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        inst = form.save(commit=False)
        inst.owner = self.request.user
        inst.save()

        return redirect(self.success_url)


class TaskDeleteView(OwnerDeleteView):
    model = Task