"""
URL configuration for the tasks API.

This module registers viewsets for categories and tasks with a router, creating
RESTful routes under the ``api/`` prefix defined in the project's root URLs.
"""
from django.urls import include, path
from rest_framework import routers

from .views import CategoryViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("tasks", TaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
