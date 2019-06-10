#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if sys.argv[1] == 'test':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "carton.test_settings")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "carton.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
