"""
Views for the tasks application.

This module defines API endpoints for managing categories and tasks. It uses
Django REST Framework's viewsets to provide standard CRUD functionality and
ensures that users can only interact with their own tasks.
"""
from rest_framework import permissions, viewsets

from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """API endpoint that allows categories to be viewed or edited."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    """API endpoint that allows tasks to be viewed or edited for the current user."""

    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Return tasks belonging to the authenticated user only."""
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """Persist a new task with the current user as its owner."""
        serializer.save(owner=self.request.user)
