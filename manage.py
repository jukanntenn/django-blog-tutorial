#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_blog_project.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_project.settings")
>>>>>>> origin/blog-tutorial

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
