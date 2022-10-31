from api.serializers import TaskSerialzer
from tasks.models import Task
from rest_framework import generics, permissions
from django.db.models import Q

class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerialzer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        query_set = Task.objects.all()
        if self.request.method not in permissions.SAFE_METHODS:
            query_set = Task.objects.filter(owner=self.request.user.id)
        search_value = self.request.query_params.get('search')
        if search_value:
            query = Q(title__icontains=search_value) 
            query.add(Q(description__icontains=search_value), Q.OR)
            query_set = Task.objects.filter(query).select_related()
        return query_set

class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerialzer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        query_set = Task.objects.all()
        if self.request.method not in permissions.SAFE_METHODS:
            query_set = Task.objects.filter(owner=self.request.user.id)
        return query_set
    lookup_field = 'pk'
