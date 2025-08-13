# tasks/views.py
from rest_framework import viewsets, generics, permissions
from django.shortcuts import get_object_or_404
from .models import Task
from .serializers import TaskSerializer, RegisterSerializer
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    """
    list: GET /tasks - list current user's tasks
    retrieve: GET /tasks/{id} - get a specific task (only if you own it)
    create: POST /tasks - create task
    update: PUT /tasks/{id} - update task (owner only)
    destroy: DELETE /tasks/{id} - delete task (owner only)
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        # Short-circuit schema generation to prevent AnonymousUser errors
        if getattr(self, 'swagger_fake_view', False):
            return Task.objects.none()

        user = self.request.user
        if user.is_anonymous:
            return Task.objects.none()
        return Task.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_object(self):
        obj = get_object_or_404(Task, pk=self.kwargs['pk'], owner=self.request.user)
        self.check_object_permissions(self.request, obj)
        return obj


class RegisterView(generics.CreateAPIView):
    """
    POST /auth/register
    """
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
