#!/usr/bin/env python
"""
Entry point for Django's command‑line utility for administrative tasks.

This script allows you to interact with the Django project configured in this
repository. If Django is installed, you can run commands such as:

    python manage.py runserver
    python manage.py migrate
    python manage.py createsuperuser

If Django is not installed in your environment, executing commands will raise
an informative error. See the README for instructions on setting up the
development environment.
"""
import os
import sys


def main() -> None:
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_manager.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
