"""
Serializers for the tasks application.

These classes convert model instances to and from representations such as JSON,
allowing our API to communicate cleanly with clients. They leverage Django
REST Framework's ModelSerializer for brevity and convenience.
"""
from rest_framework import serializers
from .models import Category, Task


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category objects."""

    class Meta:
        model = Category
        fields = ["id", "name", "description"]


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task objects with nested category and owner info."""

    owner = serializers.ReadOnlyField(source="owner.username")
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source="category", write_only=True, allow_null=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "owner",
            "category",
            "category_id",
            "title",
            "description",
            "due_date",
            "status",
            "created_at",
            "updated_at",
        ]
