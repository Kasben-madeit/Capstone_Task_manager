"""
Database models for the tasks application.

This module defines the core data models for the Task Manager API: a Category
model for organizing tasks and a Task model to represent individual tasks.
Each task belongs to a user (the ``owner``) and can be optionally assigned
to a category. Tasks track their title, description, due date and current
status. See the README for additional context and usage instructions.
"""
from django.conf import settings
from django.db import models


class Category(models.Model):
    """A logical grouping to which tasks can belong."""

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    """Represents a single task owned by a user."""

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tasks")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title} ({self.owner})"
